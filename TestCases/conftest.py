import pytest
from  selenium import webdriver

from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture(scope="class")
def setup(request, baseurl=ReadConfig.getApplicationUrl()):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        print("IE driver")
    else:
        driver = webdriver.Chrome()

    driver.get(baseurl)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


#  it is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['project name']="nope commerce"
    config._metadata['module name']="customer"
    config._metadata['Tester']="Pratik"




#  it is hook for modifying/deleting environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Plugins',None)





# @pytest.fixture()
# def setup(browser):
#    if browser=="firefox":
#      driver= webdriver.Firefox()
#      driver.implicitly_wait(60)
#    elif browser == "chrome":
#       driver = webdriver.Chrome()
#       driver.implicitly_wait(60)
#    else:
#      driver = webdriver.Firefox()
#    return driver
#
#
#
# def pytest_addoption(parser): # this will get the value from command line input call hook
#    parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request): # this will return browser value to set up method
#    return request.config.getoption("--browser")



