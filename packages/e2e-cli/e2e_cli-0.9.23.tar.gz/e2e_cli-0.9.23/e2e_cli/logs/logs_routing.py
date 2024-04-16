import subprocess

from e2e_cli.core.py_manager import Py_version_manager
from e2e_cli.core import show_messages
from e2e_cli.logs import logs_service

class LogRouting:
    def __init__(self, arguments):
        self.arguments = arguments

    def route(self, Parsing_Errors):
        if (self.arguments.args.log_commands is None) :
            show_messages.show_parsing_error(Parsing_Errors)
            subprocess.call(['e2e_cli', 'logs', '-h'])


        elif (self.arguments.args.log_commands is not None):
            logs_operations = logs_service.caller(
                    self.arguments.args.log_commands)
            if logs_operations:
                    logs_operations()


        else:
            print("command not found")
            show_messages.show_parsing_error(Parsing_Errors)
