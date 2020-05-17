
import pytest
import json
import os.path
from fixture.application import Aplication
from fixture.db import Dbfixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as config_file:
            target = json.load(config_file)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    global target
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Aplication(browser=browser, base_url=web_config['baseUrl'])
    return fixture


@pytest.fixture(scope='session')
def db(request):
    global target
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = Dbfixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope='session', autouse=True)
def stoop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='firefox')
    parser.addoption("--target", action='store', default='target.json')