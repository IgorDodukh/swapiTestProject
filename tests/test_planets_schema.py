import allure
import pytest

from helpers.api_helper import ApiHelper


@allure.feature('/planets/schema/')
class TestPlanetsSchema:

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.api_helper = ApiHelper()
        self.endpoint = "/planets/schema/"

    @allure.title('GET /planets/schema/')
    @pytest.mark.skip("Request to /schema/ endpoint responds with 404")
    def test_get_planets_schema(self):
        self.api_helper.get(endpoint=self.endpoint)
        self.api_helper.check_status_code(200)
        self.api_helper.check_response_schema("planets.json")

    @allure.title('POST /planets/schema/')
    def test_post_planets(self):
        self.api_helper.post(endpoint=self.endpoint)
        self.api_helper.check_status_code(405)
        self.api_helper.check_response_schema("error.json")
        self.api_helper.check_response_field(field_name="detail", expected_value="Method 'POST' not allowed.")

    @allure.title('PUT /planets/schema/')
    def test_put_planets(self):
        self.api_helper.put(endpoint=self.endpoint)
        self.api_helper.check_status_code(405)
        self.api_helper.check_response_schema("error.json")
        self.api_helper.check_response_field(field_name="detail", expected_value="Method 'PUT' not allowed.")

    @allure.title('DELETE /planets/schema/')
    def test_delete_planets(self):
        self.api_helper.delete(endpoint=self.endpoint)
        self.api_helper.check_status_code(405)
        self.api_helper.check_response_schema("error.json")
        self.api_helper.check_response_field(field_name="detail", expected_value="Method 'DELETE' not allowed.")
