
import subprocess
from e2e_cli.core import show_messages
from e2e_cli.faas.constants import SETUP
from e2e_cli.faas.faas_service import FaaSServices
from e2e_cli.faas.setup_service import SetupService


class FaasRouting:
    def __init__(self, arguments):
        self.arguments = arguments

    def route(self, parsing_errors):
        if self.arguments.args.faas_commands is None:
            show_messages.show_parsing_error(parsing_errors)
            # subprocess.call(['e2e_cli', 'faas', '-h'])
        
        # if not (self.arguments.args.lang and self.arguments.args.name):
        #     print("Please provide the language and name for e2e functions")
        #     subprocess.call(['e2e_cli', 'faas', '-h'])
        #     return
        
        setup_service = SetupService(alias=self.arguments.args.alias, arguments=self.arguments)
        method = setup_service.caller(self.arguments.args.faas_commands)
        if not method:
            method = FaaSServices(alias=self.arguments.args.alias, 
                                  arguments=self.arguments).caller(self.arguments.args.faas_commands)
        method()
        

        

        
