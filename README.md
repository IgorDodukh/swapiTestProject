## Preconditions
Make sure you have `git`, `python3` and `pip3` installed. If not, please do so by googling and following the instructions on the official resources.

## Prepare environment
* Clone the project to your local machine and navigate to the project directory:
```shell
git clone git@github.com:IgorDodukh/swapiTestProject.git
cd swapiTestProject
```
* Install and setup virtualenv for the project:
```shell
pip install virtualenv
virtualenv --python python3 venv
source venv/bin/activate
```
* Install all packages required for the tests run:
```shell
pip install -r requirements.txt
```

## Run tests
Once the environment is ready the tests can be executed. Run the following command to do so:
```shell
pytest tests
```
By default, tests are running on the environment: https://swapi.dev/api
To run tests on the another env. add the argument: `--env_url` with your environment value.
```shell
pytest tests --env_url=https://swapi.dev/api
```
To run tests with Allure reporting add the argument `--alluredir=allure-results` to the command.
```shell
pytest tests --alluredir=allure-results
```

## View report
If the tests were executed with `--alluredir` argument, allure results will be stored in the defined directory. To view allure results run the following command:
```shell
allure serve allure-results
```
