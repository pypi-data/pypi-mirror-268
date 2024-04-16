import subprocess

from e2e_cli.core.py_manager import Py_version_manager
from e2e_cli.core import show_messages
from e2e_cli.config.config import AuthConfig
from e2e_cli.core.alias_service import get_user_cred

class ConfigRouting:
    def __init__(self, arguments):
        self.arguments = arguments

    def route(self, Parsing_errors):

        if self.arguments.args.alias_commands == 'add':
            try:
                api_key = input("Enter your api key: ")
                auth_token = input("Enter your auth token: ")
                auth_config_object = AuthConfig(alias=input("Input name of alias you want to add : "),
                                                    api_key=api_key,
                                                    api_auth_token=auth_token)
                auth_config_object.add_to_config()
            except KeyboardInterrupt:
                print(" ")
                pass


        elif self.arguments.args.alias_commands == 'add_file':
                path=input("input the file path : ")
                auth_config_object = AuthConfig()
                auth_config_object.adding_config_file(path)
                return
            

        elif self.arguments.args.alias_commands == 'delete':  
            delete_alias=input("Input name of alias you want to delete : ")          
            confirmation =input("are you sure you want to delete press y for yes, else any other key : ")
            if(confirmation.lower()=='y'):
                auth_config_object = AuthConfig(alias=delete_alias)
                try:
                    auth_config_object.delete_from_config()
                except:
                    pass  


        elif self.arguments.args.alias_commands == 'view':
                for item in list(get_user_cred("all", 1)):
                    print(item)
            
        
        elif self.arguments.args.alias_commands == 'set':
                default_name=input("Enter name of the alias you want to set as default : ")
                get_user_cred(default_name)  
                if(input("are you sure you want to proceed (y/n): ").lower()=="y"):
                    try:
                        AuthConfig(alias="default").delete_from_config(x=1)
                        auth_config_object = AuthConfig(alias="default",
                                                        api_key=default_name,
                                                        api_auth_token=default_name)
                        auth_config_object.set_default()
                        print("Default alias set to ", default_name)
                    except KeyboardInterrupt:
                        print(" ")
                        pass


        else:
            print("Command not found!!")
            show_messages.show_parsing_error(Parsing_errors)                           