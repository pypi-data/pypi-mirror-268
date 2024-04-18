import getpass
import subprocess
from os import path as ospath
from pathlib import Path
from shutil import copyfile

import pykeepass
from click import argument as cargument
from click import echo as cecho
from click import group as cgroup
from click import option as coption
from construct import ChecksumError
from pykeepass import PyKeePass, create_database
from pykeepass import exceptions as pykeepass_exceptions


def path_selection(test=False):
    """Setup path variables for pykeypass

    Normal Operation: pykeypass creates a '.pykeypass' folder in the user's home directory to
    house the Keepass.exe and the app's Keepass database.
    Testing Operation: Similar to nomral option, but the '.pykeypass' folder is created in the
    'test' directory at the root of the application folder.

    Args:
        test (bool, optional): The test directory is set if 'test' is passed in as True. Defaults
        to False.

    Returns:
        [multiple variables]: Returns all three path variables. Populates three comma separated
        variables from the function.
    """
    pykeypass_folder = (
        Path.home() / ".pykeypass" if test is False else Path(__file__).resolve().parent.parent.parent / "test" / ".pykeypass"
    )
    print(pykeypass_folder)
    pykeypass_app = pykeypass_folder / "keepass.exe"
    pykeypass_db = pykeypass_folder / "pykeepass.kdbx"
    return pykeypass_folder, pykeypass_app, pykeypass_db


@cgroup()
def cli():
    """KEEPASS CLI TOOL

    This tool can be configured to launch any number of Keepass databases with a single command
    (and password).
    """


@cli.command("setup", help="Initial setup of pykeypass app database.")
@coption("-t", "--test", "test", is_flag=True, hidden=True)
def pykeypass_setup(test):
    """Intial setup

    - Copies Keepass.exe to .pykeypass folder in home directory
    - Creates pykeypass.kdbx in .pykeypass folder in hom directory
    """
    try:
        pykeypass_folder, pykeypass_app, pykeypass_db = path_selection(test)
        if ospath.exists(pykeypass_app) is False:
            Path(pykeypass_folder).mkdir(parents=True, exist_ok=True)
            copyfile(Path.cwd() / "thirdparty" / "keepass_portable" / "keepass.exe", pykeypass_app)
        if ospath.exists(pykeypass_db):
            confirmation = input(
                "WARNING: If an app database already exists, this process will delete it and "
                "create a fresh one.\nProceed? (y/n) "
            )
        else:
            confirmation = "y"
        if confirmation == "y":
            cecho("STEP 1: Create pykeypass app database.")
            new_password = getpass.getpass(prompt="Create a pykeypass password: ")
            create_database(pykeypass_db, password=new_password)
            PyKeePass(pykeypass_db, password=new_password)
            cecho(
                "DONE: pykeypass app database created.\n"
                "Setup keepass databases by using:\n"
                "- 'pykeypass open <new_name> -s'\n"
            )
        else:
            cecho("pykeypass setup cancelled.")
    except FileNotFoundError:
        cecho(
            """ERROR: pykeypass app not setup. To setup, perform one of the following:
(1) Run 'install.bat' from pykeypass app folder.
(2) Open CMD/terminal in root of pykeypass app directory and run 'pykeypass setup' (all other 
functionality is global)"""
        )


@cli.command("list", help="Lists available databases to open.")
@coption(
    "-i",
    "--input_password",
    "input_password",
    hidden=True,
    help="Reserved for use with 'pykeepass all'",
)
@coption("-t", "--test", "test", is_flag=True, hidden=True)
def keepass_list(test, input_password=None):
    """Lists available Keepass databases to launch."""
    try:
        pykeypass_folder, pykeypass_app, pykeypass_db = path_selection(test)
        kp = PyKeePass(pykeypass_db, password=getpass.getpass(prompt="pykeypass password: "))
        groups = kp.find_groups(name=".", regex=True)
        cecho("ENTRIES AVAILABLE: ")
        for i in groups[1:]:
            if str(i)[8:-2] != "Recycle Bin":
                # print("HEREHEREHERE", str(i))
                print(str(i)[8:-1])
    except pykeepass.exceptions.CredentialsError:
        cecho("ERROR: pykeypass login information invalid.\n")
    except FileNotFoundError:
        cecho("ERROR: pykeepass app database not found. Use 'pykeypass setup' to get started.\n")


@cli.command("manage", help="Add or replace the requsested database entry.")
@cargument("database", required=True)
@coption(
    "-i",
    "--input_password",
    "input_password",
    hidden=True,
    help="Reserved for use with 'pykeepass all'",
)
@coption("-t", "--test", "test", is_flag=True, hidden=True)
def keepass_manage(database, test, input_password=None):
    """Launches wizard for specified database entry."""
    try:
        pykeypass_folder, pykeypass_app, pykeypass_db = path_selection(test)
        cecho(f"START: Setup {database} keepass.")
        password = getpass.getpass(prompt="pykeypass password: ")
        kp = PyKeePass(pykeypass_db, password=password)
        group = kp.find_groups(kp.root_group, f"{database}")
        entry = kp.find_entries(title=f"{database}", first=True)
        if entry is None:
            confirmation = "y"
        else:
            confirmation = input(
                f"WARNING: An entry for {database} already exists, this process will delete it "
                "and create a fresh one.\nProceed? (y/n) "
            )
            kp.delete_entry(entry)
            try:
                kp.delete_group(group)
            except AttributeError as e:
                if "'NoneType' object has no attribute 'delete'" not in str(e):
                    raise AttributeError(e) from e
            kp.save()
        if confirmation == "y":
            kp = PyKeePass(pykeypass_db, password=password)
            keepass_url = input(f"Set {database} Keepass url: ")
            keepass_pw = getpass.getpass(prompt=f"Set {database} Keepass Password: ")
            group = kp.add_group(kp.root_group, f"{database}")
            kp.add_entry(group, f"{database}", f"{database}", keepass_pw, url=keepass_url)
            kp.save()
            key_question = input("Does this Keepass database use a key file? (y/n) ")
            if key_question == "y":
                kp = PyKeePass(pykeypass_db, password=password)
                entry = kp.find_entries(title=f"{database}", first=True)
                key_file = input("Set key file (file path + file name): ")
                entry.set_custom_property("key", str(key_file))
        kp.save()
        cecho(f"DONE: {database} keepass password setup.")
        cecho(f'Try launching with "pykeypass open {database}", or "pykeypass all"')
    except pykeepass.exceptions.CredentialsError:
        cecho("ERROR: pykeypass login information invalid.\n")
    except FileNotFoundError:
        cecho("ERROR: pykeepass app database not found. Use 'pykeypass setup' to get started.\n")


@cli.command("open", help="Launches requested Keepass database.")
@cargument("database", required=True)
@coption(
    "-i",
    "--input_password",
    "input_password",
    hidden=True,
    help="Reserved for use with 'pykeepass all'",
)
@coption("-t", "--test", "test", is_flag=True, hidden=True)
def keepass_open(database, test, input_password=None):
    """Launches requested Keepass database."""
    try:
        pykeypass_folder, pykeypass_app, pykeypass_db = path_selection(test)
        password = (
            getpass.getpass(prompt="pykeepass password: ") if input_password is None else input_password
        )

        kp = PyKeePass(pykeypass_db, password=password)
        entry = kp.find_entries(title=f"{database}", first=True)
        if entry.get_custom_property("key") is not None:
            key_file = entry.get_custom_property("key")
            subprocess.Popen(
                f'{pykeypass_app} "{entry.url}" -pw:{entry.password} -keyfile:"{key_file}"',
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        else:
            subprocess.Popen(
                f'{pykeypass_app} "{entry.url}" -pw:{entry.password}',
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
    except pykeepass_exceptions.CredentialsError:
        cecho("ERROR: pykeypass login information invalid.\n")
    except AttributeError as e:
        cecho(f"ERROR: Setup item for {database} file missing or incorrect")
        if str(e) == "'NoneType' object has no attribute 'url'":
            cecho(
                f"ISSUE: It looks like there is no url configured for the {database} Keepass "
                "database."
            )
        elif entry is None:
            cecho(
                f"ISSUE: All or part of the {database} Keepass entry was not found.\nFIX: Setup "
                f'this entry using: "pykeypass open {database} -s"'
            )
        else:
            cecho(f"Error message: {e}")
    except subprocess.CalledProcessError as e:
        cecho(e)
    except FileNotFoundError:
        cecho("ERROR: pykeepass app database not found. Use 'pykeypass setup' to get started.\n")
    except ChecksumError:
        cecho("ERROR: pykeypass login information invalid.\n")


@cli.command("path", help="Launches functionality for a specific Keepass database.")
@cargument("database", required=True)
@coption(
    "-i",
    "--input_password",
    "input_password",
    hidden=True,
    help="Reserved for use with 'pykeepass all'",
)
@coption("-t", "--test", "test", is_flag=True, hidden=True)
def keepass_path(database, test, input_password=None):
    """Shows file(s) for database entry."""
    try:
        pykeypass_folder, pykeypass_app, pykeypass_db = path_selection(test)
        kp = PyKeePass(pykeypass_db, password=getpass.getpass(prompt="pykeypass password: "))
        entry = kp.find_entries(title=f"{database}", first=True)
        cecho(f"{database.upper()} PATH: {entry.url}")
        if entry.get_custom_property("key"):
            key_name = entry.get_custom_property("key")
            cecho(f"{database.upper()} KEY: {key_name}")
    except pykeepass.exceptions.CredentialsError:
        cecho("ERROR: pykeypass login information invalid.\n")
    except AttributeError:
        cecho(
            f"ISSUE: All or part of the {database} Keepass entry was not found.\nFIX: Setup this "
            f'entry using: "pykeypass open {database} -s"'
        )
    except FileNotFoundError:
        cecho("ERROR: pykeepass app database not found. Use 'pykeypass setup' to get started.\n")


# @cli.command("all", help="Starts all configured Keepass databases.")
# @coption("-t", "--test", "test", is_flag=True, hidden=True)
# def keepass_all(test):
#     """Launches all database entries."""
#     try:
#         mode = "-t" if test is True else ""
#         pykeypass_folder, pykeypass_app, pykeypass_db = path_selection(test)
#         password = getpass.getpass(prompt="pykeepass password: ")
#         kp = PyKeePass(pykeypass_db, password=password)
#         groups = kp.find_groups(name=".", regex=True)
#         if len(groups) > 1:
#             for i in groups[1:]:
#                 database_entry = str(i)[8:-1]
#                 print(database_entry)
#                 pipe_local = subprocess.Popen(
#                     f"pykeypass open {database_entry} -i {password} {mode}",
#                     stdout=subprocess.PIPE,
#                     stderr=subprocess.PIPE,
#                 )
#                 if pipe_local.communicate() and pipe_local.returncode == 0:
#                     cecho(f"STATUS: {database_entry} keypass database launched successfully.")
#         else:
#             cecho(
#                 "NOTICE: No entry created. Use 'pykeypass open <new_name> -s'" + "to get started."
#             )
#     except pykeepass_exceptions.CredentialsError:
#         cecho("ERROR: pykeypass login information invalid.\n")
#     except FileNotFoundError:
#         cecho("ERROR: pykeepass app database not found. Use 'pykeypass setup' to get started.\n")
#     except subprocess.CalledProcessError as e:
#         cecho(e)
#     except Exception as e:
#         raise Exception(e)


if __name__ == "__main__":
    cli()
