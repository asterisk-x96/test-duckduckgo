import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config_data = json.load(config_file)
    return config_data

def test_config_implicit_wait(config):
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

@pytest.fixture
def browser():
    # Initialize the ChromeDrive instance
    b = selenium.webdriver.Chrome()

    # Make it calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(10)

    # Return the WebDrive instance for the setup
    yield b

    # Quit the WebDrive instance for the cleanup
    b.quit()
