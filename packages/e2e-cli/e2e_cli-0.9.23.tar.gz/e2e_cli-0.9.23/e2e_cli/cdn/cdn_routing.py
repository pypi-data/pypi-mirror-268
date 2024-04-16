import subprocess

from e2e_cli.core.py_manager import Py_version_manager
from e2e_cli.core import show_messages
from e2e_cli.cdn.cdn_crud.cdn import CdnCrud
from e2e_cli.cdn.cdn_actions.cdn_action import CdnActions

class CdnRouting:
    def __init__(self, arguments):
        self.arguments = arguments
        
        
    def route(self, Parsing_Errors):
        if (self.arguments.args.action is None) and (self.arguments.args.cdn_commands is None):
            show_messages.show_parsing_error(Parsing_Errors)
            subprocess.call(['e2e_cli', 'cdn', '-h'])


        elif (self.arguments.args.cdn_commands is not None) and (self.arguments.args.action is not None):
              print("Only one action at a time !!")


        elif(self.arguments.args.cdn_commands is not None):
            cdn_operations = CdnCrud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
            if cdn_operations.possible:
                operation = cdn_operations.caller(
                    self.arguments.args.cdn_commands)
                if operation:
                    try:
                        operation()
                    except KeyboardInterrupt:
                        print(" ")


        elif(self.arguments.args.action is not None):
            cdn_operations = CdnActions(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
            if cdn_operations.possible:
                operation = cdn_operations.caller(
                    self.arguments.args.action)
                if operation:
                    try:
                        operation()
                    except KeyboardInterrupt:
                        print(" ")

                else:
                    print("command not found")
                    show_messages.show_parsing_error(Parsing_Errors)
                

        else:
            print("command not found")
            show_messages.show_parsing_error(Parsing_Errors)