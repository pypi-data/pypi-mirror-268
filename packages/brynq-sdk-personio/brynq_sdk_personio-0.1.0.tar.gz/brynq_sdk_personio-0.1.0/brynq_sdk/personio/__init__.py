import requests
import json
from typing import List, Union
from brynq_sdk.brynq import BrynQ
from brynq_sdk.personio.employees import Employees


# Set the base class for Persinio. This class will be used to set the credentials and those will be used in all other classes.
class Personio(BrynQ):
    def __init__(self, label: Union[str, List], debug: bool = False):
        """"
        For the documentation of Personio, see: https://developer.personio.de/reference/auth
        """
        super().__init__()
        base_url = 'https://api.personio.de/v1/'
        headers = self._set_credentials(label, base_url)
        self.employees = Employees(headers, base_url)

    def _set_credentials(self, label, base_url):
        """
        Sets the credentials for the SuccessFactors API.
        :param label (str): The label for the system credentials.
        :returns: headers (dict): The headers for the API request, including the access token.
        """
        credentials = self.get_system_credential(system='personio', label=label)
        payload = json.dumps({
            "client_id": f"{credentials['client_id']}",
            "client_secret": f"{credentials['client_secret']}"
        })
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        response = requests.post(f'{base_url}auth', headers=headers, data=payload)
        access_token = response.json()['data']['token']
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        return headers