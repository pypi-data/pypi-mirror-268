import subprocess

from e2e_cli.core.py_manager import Py_version_manager
from e2e_cli.core import show_messages
from e2e_cli.bucket_store.bucket_crud.bucket_storage import BucketCrud
from e2e_cli.bucket_store.bucket_actions.bucket_actions import BucketActions

class BucketRouting:
    def __init__(self, arguments):
        self.arguments = arguments
        
        
    def route(self, Parsing_Errors):
        if (self.arguments.args.bucket_commands is None) and (self.arguments.args.action is None):
            show_messages.show_parsing_error(Parsing_Errors)
            subprocess.call(['e2e_cli', 'bucket', '-h'])


        elif (self.arguments.args.bucket_commands is not None) and (self.arguments.args.action is not None):
              print("Only one action at a time !!")


        elif(self.arguments.args.bucket_commands is not None):
            bucket_operations = BucketCrud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
            if bucket_operations.possible:
                operation = bucket_operations.caller(
                    self.arguments.args.bucket_commands)
                if operation:
                    try:
                        operation()
                    except KeyboardInterrupt:
                        print(" ")


        elif(self.arguments.args.action is not None):
            bucket_operations=BucketActions(alias=self.arguments.args.alias, inputs=self.arguments.inputs)     
            if bucket_operations.possible:
                operation = bucket_operations.caller(
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