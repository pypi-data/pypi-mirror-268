import re

from e2e_cli.core.helper_service import ApiFilter


def  dbaas_create_helper(inputs):
    required = {"plan_name": "", "db": "", "db_version": "",
                "name": "", "user": "", "password": __Check.password_validity}
    optional = {}
    ApiFilter(inputs, required, optional)

def  dbaas_delete_helper(inputs):
    required = {"dbaas_id": int, }
    optional = {}
    ApiFilter(inputs, required, optional)


class __Check:
    """Note format for input checks has been defined in this way, so that data type and format both can be handeled by inputs_and_required_check and inputs_and_optional_check"""
    """All checks/validation functions must follow this format/syntax as shown for bucket_name_validity"""

    @classmethod
    def name_user_validity(self, bucket_name):
        valid = not (bool(re.findall('[!@#$%^&*)(_+=}{|/><,.;:"?`~]', bucket_name)) and bool(re.findall("'", bucket_name)) and bool(re.search("]", bucket_name)) or bool(re.search("[[]", bucket_name)))
        if valid :
            return bucket_name
        else :
            raise Exception("Only following chars are supported, Alphabets or numbers(0-9)")

    @classmethod
    def password_validity(self, password):
        valid = True
        if len(password)<16:
            valid = False
        if valid:
            valid = (bool(re.findall('[!@#$%^&*?]', password)) and bool(re.findall("[A-Z]", password)) and bool(re.findall("[a-z]", password)) and bool(re.findall('\d+', password)) and (not bool(re.findall('[-_+=|\}{;:"~`]', password))) )
        if valid :
            return password
        else :
            raise Exception(
                "Password should be of minimum 16 characters long. It should contain a number, an uppercase, a lowercase and a special character")
