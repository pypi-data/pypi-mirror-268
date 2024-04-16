import json
import os
import re

from e2e_cli.core.alias_service import get_user_cred
from e2e_cli.faas.constants import (LANGUAGE_OPTIONS, RUNTIME_LANGUAGE_MAPPING,
                                    RUNTIME_API_ENDPOINT, VALIDATE_NAME_REGEX,
                                    NAME_VALIDATION_MESSAGE)
from e2e_cli.core.apiclient import ApiClient
from e2e_cli.core.helper_service import Checks
from e2e_cli.faas.helper_service import HelperService

class SetupService:
    def __init__(self, **kwargs):
        self.user_creds = get_user_cred(kwargs.get("alias"))
        self.api_key = self.user_creds[1]
        self.auth_token = self.user_creds[0]
        self.arguments = kwargs.get("arguments")
    
    def caller(self, method):
        allowed_method = {
            "setup": self.setup
        }
        return allowed_method.get(method)
        
    def format_runtimes(self, response):
        runtimes = response.get("data")
        language_templates = dict()
        for runtime_detail in runtimes:
            language_templates.update({
                RUNTIME_LANGUAGE_MAPPING.get(runtime_detail.get("runtime")) : runtime_detail
            })
        return language_templates

    def get_runtimes(self):
        response = ApiClient(self.api_key, self.auth_token).get_response(RUNTIME_API_ENDPOINT, "GET")
        if not response:
            print("There is some error on our end in fetching runtime. kindly try after some time.")
        if response.get("code") != 200:
            Checks.status_result(response)
        return self.format_runtimes(response)
        
    def setup(self):
        language = self.arguments.args.lang
        function_name = self.arguments.args.name
        available_runtime = self.get_runtimes()
        if not available_runtime.get(language):
            print("Currently e2e functions does not allow this language. Please try after some time.")
        setup_details = available_runtime.get(language)
        valid_pattern = re.compile(VALIDATE_NAME_REGEX)

        if not re.fullmatch(valid_pattern, function_name):
            print(f"Please enter the valid function name.{NAME_VALIDATION_MESSAGE}")
        current_working_directory = os.getcwd()
        os.mkdir(f"{current_working_directory}/{function_name}")
        if os.path.exists(f"{current_working_directory}/{function_name}"):
            os.chdir(f"{current_working_directory}/{function_name}")
            HelperService.create_file_with_template_code("code.txt", setup_details.get("boiler_code"))
            HelperService.create_file_with_template_code(setup_details.get("label"), setup_details.get("requirements_code"))
            HelperService.create_file_with_template_code("environment_variable.txt", None)
        else:
            print("Error -- Can not able to locate the setup directory.")
        print(f"Setup is successfully completed. kindly check folder {function_name} in current directory.")

        