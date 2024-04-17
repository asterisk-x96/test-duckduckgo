"""
This module contains shared fixtures
"""
import pytest
import selenium.webdriver

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
    



