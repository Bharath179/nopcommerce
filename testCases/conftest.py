from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome browser.............")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching Firefox browser.............")
    else:
        driver=webdriver.Edge()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

"""###################### pyTest HTML Report ########################

#It is hook for Adding Environment info to HTML Report

def pytest_configure(config):
    config.metadata['Project Name']='nop Commerce'
    config.metadata['Module Name'] = 'Customers'
    config.metadata['Tester Name'] = 'Bharath'

#It is hook for delete/Modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)"""
