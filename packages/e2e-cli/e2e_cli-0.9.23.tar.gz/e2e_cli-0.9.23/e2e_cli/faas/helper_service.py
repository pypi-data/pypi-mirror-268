import os
import codecs
from e2e_cli.faas.constants import LANGUAGE_REQUIREMENT_MAPPING

class HelperService:
    @classmethod
    def create_file_with_template_code(cls, name, boiler_code):
        file = open(name, "w")
        if boiler_code:
            file.writelines(boiler_code)
        file.close()

    @classmethod
    def get_function_details(cls, function_path, language):
        if not os.path.exists(function_path):
            print("CLI can not locate function. kindly check weather this function exists in current directory.")
            return
        code = None; requirement = None; env_var = None

        with open(f"{function_path}/code.txt",'r') as code_file:
            code = code_file.read()

        with open(f"{function_path}/{LANGUAGE_REQUIREMENT_MAPPING.get(language)}", 'r') as requirement_file:
            requirement = requirement_file.read()
        
        with open(f"{function_path}/environment_variable.txt", 'r') as env_file:
            env_var = list()
            for variable in env_file:
                key, value = variable.strip().split(':')
                env_var.append({"Key": key, "Value": value})

        return code, requirement, env_var
