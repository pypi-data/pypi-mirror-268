import requests


class Employees:

    def __init__(self, headers, base_url):
        self.headers = headers
        self.base_url = base_url

    def get(self, limit=None, offset=None):
        url = f'{self.base_url}company/employees'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def create(self, data):
        url = 'https://api.personio.de/v1/employees'
        response = requests.post(url, json=data)
        return response.json()

    def update(self, employee_id, data):
        url = f'https://api.personio.de/v1/employees/{employee_id}'
        response = requests.put(url, json=data)
        return response.json()

    def get_absence_balance(self, employee_id):
        url = f'https://api.personio.de/v1/employees/{employee_id}/absence_balances'
        response = requests.get(url)
        return response.json()

    def get_attributes(self):
        url = 'https://api.personio.de/v1/employee_attributes'
        response = requests.get(url)
        return response.json()

    def get_custom_attributes(self):
        url = 'https://api.personio.de/v1/employee_custom_attributes'
        response = requests.get(url)
        return response.json()