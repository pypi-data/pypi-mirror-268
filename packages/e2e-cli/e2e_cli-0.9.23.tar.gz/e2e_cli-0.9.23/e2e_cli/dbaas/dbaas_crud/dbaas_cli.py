import json

from prettytable import PrettyTable


from e2e_cli.core.py_manager import Py_version_manager
from e2e_cli.core.alias_service import get_user_cred
from e2e_cli.core.request_service import Request
from e2e_cli.core.helper_service import Checks
from e2e_cli.dbaas.dbaas_crud.helpers import dbaas_create_helper, dbaas_delete_helper


class DbaaSCrud:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        if (get_user_cred(kwargs['alias'])):
            self.API_key = get_user_cred(kwargs['alias'])[1]
            self.Auth_Token = get_user_cred(kwargs['alias'])[0]
            self.possible = True
        else:
            self.possible = False

    def caller(self, method):
        function_set = {"create": self.create_dbaas,
                        "delete": self.delete_dbaas,
                        "list": self.list_dbaas
                        }
        return function_set.get(method)


    def create_dbaas(self):
        print("Creating")
        API_key = self.API_key
        Auth_Token = self.Auth_Token
        dbaas_create_helper(self.kwargs["inputs"])
        my_payload = {
            "name": self.kwargs["inputs"]["name"],
            "plan_name": self.kwargs["inputs"]["plan_name"],   #ex- DBS.8GB, DBS.16GB 
            "db":  self.kwargs["inputs"]["db"],                #ex- mysql, postgresql, mariadb
            "db_version": self.kwargs["inputs"]["db_version"], #ex- 8, 11, 5.6 
            "group": "Default",
            "database": {
                "name": self.kwargs["inputs"]["name"],
                "user": self.kwargs["inputs"]["user"],
                "password": self.kwargs["inputs"]["password"]
            }
        }
        url = "api/v1/rds/cluster/?apikey=" + API_key+"&location=Delhi"
        req = "POST"
        user_agent = 'cli-e2e'
        
        status = Request(url, Auth_Token, json.dumps(my_payload),
                         req, user_agent).response.json()

        # if Checks.status_result(status,req):
        #     try :
        #         x = PrettyTable()
        #         x.field_names = ["ID", "Name", "Created at", "disk", "Status", "Plan"]
        #         x.add_row([status['data']['id'], status['data']['name'],
        #               status['data']['created_at'], status['data']['disk'], status['data']['status'], status['data']['plan']])
        #         print(x)
        #     except Exception as e:
        #             print("Errors : ", e)

        # if('json' in self.kwargs["inputs"]):
        #     Checks.show_json(status)
        Checks.status_result(status)
        Checks.show_json(status)


    def delete_dbaas(self):
        my_payload = {}
        API_key = self.API_key
        Auth_Token = self.Auth_Token
        dbaas_delete_helper(self.kwargs["inputs"])
        dbaas_id = self.kwargs["inputs"]["dbaas_id"]
        url = "api/v1/rds/cluster/" + \
            str(dbaas_id) + "/?apikey="+API_key
        req = "DELETE"

        confirmation = input(
            "are you sure you want to delete press y for yes, else any other key : ")
        if (confirmation.lower() == "y"):
            status = Request(url, Auth_Token, my_payload, req).response.json()
            if Checks.status_result(status, req):
                print("dbaas Successfully deleted")
                print(
                    "use following command -> e2e_cli <alias> dbaas list to check if dbaas has been deleted")

            # if('json' in self.kwargs["inputs"]):
            #     Checks.show_json(status)
        Checks.show_json(status)


    def list_dbaas(self, parameter=0):
        my_payload = {}
        API_key = self.API_key
        Auth_Token = self.Auth_Token
        url = "api/v1/rds/cluster/?apikey=" + API_key+"&location=Delhi"
        req = "GET"
        status = Request(url, Auth_Token, my_payload,
                         req).response.json()

        if parameter == 0:
            # if Checks.status_result(status, req):
            #     list=status['data']
            #     try:
            #         i = 1
            #         x = PrettyTable()
            #         x.field_names = ["index", "ID", "Name", "Plan", "Status"]
            #         for element in list:
            #             x.add_row([i, element['id'], element['name'],
            #                       element['plan'],  element['status']])
            #             i = i+1
            #         print(x)
            #     except Exception as e:
            #             print("Errors : ", e)

            #     if('json' in self.kwargs["inputs"]):
            #         Checks.show_json(status)
            # Checks.status_result(status)
            Checks.show_json(status)

        elif parameter == 1:
            return status['data']
