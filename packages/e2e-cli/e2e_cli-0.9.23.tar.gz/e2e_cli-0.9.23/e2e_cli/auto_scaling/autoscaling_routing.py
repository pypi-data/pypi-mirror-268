import subprocess

from e2e_cli.core.py_manager import Py_version_manager
from e2e_cli.core import show_messages
from e2e_cli.auto_scaling.auto_scaling import AutoscalingCrud

class AutoscalingRouting:
    def __init__(self, arguments):
        self.arguments = arguments
        
        
    def route(self, Parsing_Errors):
        if (self.arguments.args.autoscaling_commands is None):
            show_messages.show_parsing_error(Parsing_Errors)
            subprocess.call(['e2e_cli', 'autoscaling', '-h'])

        # elif (self.arguments.args.autoscaling_commands is not None) and (self.arguments.args.action is not None):
        #       print("Only one action at a time !!")

        elif(self.arguments.args.autoscaling_commands is not None):
            auto_scaling_operations = AutoscalingCrud(alias=self.arguments.args.alias, inputs=self.arguments.inputs)
            if auto_scaling_operations.possible:
                operation = auto_scaling_operations.caller(
                    self.arguments.args.autoscaling_commands)
                if operation:
                    try:
                        operation()
                    except KeyboardInterrupt:
                        print(" ")
        
            
        else:
            print("command not found")
            show_messages.show_parsing_error(Parsing_Errors)