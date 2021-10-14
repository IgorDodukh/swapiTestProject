import allure
import pytest

from helpers.api_helper import ApiHelper
from helpers.datasets import PlanetDataset


@allure.feature("/planets/:id")
class TestSpecificPlanet:

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.api_helper = ApiHelper()
        self.endpoint = "/planets/"

    @allure.title('GET /planets/:id with existing id')
    def test_get_existing_planet(self):
        self.api_helper.get(endpoint=self.endpoint + "1")
        self.api_helper.check_status_code(200)
        self.api_helper.check_response_schema("specific_planet.json")

    @allure.title('GET /planets/?search=name with existing name')
    def test_get_existing_planet_by_search(self):
        self.api_helper.get(endpoint=self.endpoint + "?search=Tatooine")
        self.api_helper.check_status_code(200)
        self.api_helper.check_response_schema("planets.json")
        self.api_helper.check_response_field(field_name="count", expected_value=1)

    @allure.title('GET /planets/?search=name with not existing name')
    def test_get_not_existing_planet_by_search(self):
        self.api_helper.get(endpoint=self.endpoint + "?search=Blablabla")
        self.api_helper.check_status_code(200)
        self.api_helper.check_response_schema("planets.json")
        self.api_helper.check_response_field(field_name="count", expected_value=0)

    @allure.title('GET /planets/:id with invalid id')
    @pytest.mark.parametrize("planet_id", PlanetDataset.invalid_planet_id)
    def test_get_not_existing_planet(self, planet_id):
        self.api_helper.get(endpoint=self.endpoint + planet_id)
        self.api_helper.check_status_code(404)
        self.api_helper.check_response_schema("error.json")
        self.api_helper.check_response_field(field_name="detail", expected_value="Not found")

    @allure.title('POST /planets/:id')
    def test_post_specific_planet(self):
        self.api_helper.post(endpoint=self.endpoint + "1")
        self.api_helper.check_status_code(405)
        self.api_helper.check_response_schema("error.json")
        self.api_helper.check_response_field(field_name="detail", expected_value="Method 'POST' not allowed.")

    @allure.title('PUT /planets/:id')
    def test_put_specific_planet(self):
        self.api_helper.put(endpoint=self.endpoint + "1")
        self.api_helper.check_status_code(405)
        self.api_helper.check_response_schema("error.json")
        self.api_helper.check_response_field(field_name="detail", expected_value="Method 'PUT' not allowed.")

    @allure.title('DELETE /planets/:id')
    def test_delete_specific_planet(self):
        self.api_helper.delete(endpoint=self.endpoint + "1")
        self.api_helper.check_status_code(405)
        self.api_helper.check_response_schema("error.json")
        self.api_helper.check_response_field(field_name="detail", expected_value="Method 'DELETE' not allowed.")
