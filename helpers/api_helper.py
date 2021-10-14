import json
from pathlib import Path

import allure
import requests
from cerberus import Validator

from helpers.singleton import Singleton


class ApiHelper(metaclass=Singleton):

    def __init__(self, base_url: str = None):
        super().__init__()
        self.__session = requests.session()
        self.schema_endpoint = "/planets/schema/"
        self.__json_headers = {'Content-Type': 'application/json'}
        self.__base_url = base_url
        self.__response = None

    @allure.step
    def get(self, endpoint):
        self.__response = self.__session.get(url=self.__base_url + endpoint, headers=self.__json_headers)

    @allure.step
    def post(self, endpoint, body=None):
        self.__response = self.__session.post(url=self.__base_url + endpoint, data=body, headers=self.__json_headers)

    @allure.step
    def delete(self, endpoint, body=None):
        self.__response = self.__session.delete(url=self.__base_url + endpoint, data=body, headers=self.__json_headers)

    @allure.step
    def put(self, endpoint, body=None):
        self.__response = self.__session.put(url=self.__base_url + endpoint, data=body, headers=self.__json_headers)

    @allure.step
    def check_status_code(self, expect_code: int = 200):
        actual_code = self.__response.status_code
        assert actual_code == expect_code, f"Status code is not expected.\n" \
                                           f'Request URL: {self.__response.request.url}\n' \
                                           f"Expected status code: {expect_code}\n" \
                                           f"Actual status code: {actual_code}\n" \
                                           f'Reason: {self.__response.reason}\n' \
                                           f'Text: {self.__response.text}'

    @allure.step
    def check_response_field(self, field_name, expected_value):
        json_response = json.loads(self.__response.text)
        actual_message = json_response[field_name]
        assert actual_message == expected_value, f"Invalid [{field_name}] field value." \
                                                 f'Request URL: {self.__response.request.url}\n' \
                                                 f"Expected message: {expected_value}" \
                                                 f"Actual message: {actual_message}" \
                                                 f'Reason: {self.__response.reason}\n' \
                                                 f'Text: {self.__response.text}'

    @staticmethod
    def parse_json(filename):
        base_dir = Path(__file__).parent.parent.joinpath("schemas").joinpath(filename)
        with open(base_dir) as schema_file:
            return json.loads(schema_file.read())

    @allure.step
    def check_response_schema(self, schema_name):
        schema = self.parse_json(schema_name)
        json_response = json.loads(self.__response.text)
        validator = Validator(schema)
        is_valid = validator.validate(json_response)
        assert is_valid, validator.errors
