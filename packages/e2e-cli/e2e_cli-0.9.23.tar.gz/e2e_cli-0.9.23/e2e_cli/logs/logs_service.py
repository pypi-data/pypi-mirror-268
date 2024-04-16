import os
import platform
from datetime import datetime
import logging

from prettytable import PrettyTable

from e2e_cli.core.py_manager import Py_version_manager


__home_directory = os.path.expanduser("~")
if platform.system() == "Windows":
        __logs_file = __home_directory + "\.E2E_CLI\cli_logs.log"
elif platform.system() == "Linux" or platform.system() == "Darwin":
        __logs_file = __home_directory + "/.E2E_CLI/cli_logs.log"


# open to all for logging records
def save_to_logs(arguments, response_traceback):
    logging.basicConfig(filename=__logs_file)
    logger = logging.getLogger("E2E_CLI LOGGER")
    logger.error("ERROR IN COMMAND, : {}, {}".format( str(datetime.now()), arguments))
    logger.error(response_traceback)


def caller(method):
    function_set = {"view": view_logs,
                    "clear": clear_logs,
                    }
    return function_set.get(method)

def view_logs():
    try:
        with open(__logs_file, 'r+') as file_reference:
                    read_string = file_reference.read()
        print(read_string)
    except:
        print("Error : logs not found")

def clear_logs():
    try:
        with open(__logs_file, 'w') as file_reference:
              file_reference.write("")
    except:
        print("Error : logs not found")
