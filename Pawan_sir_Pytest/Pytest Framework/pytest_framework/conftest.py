import pytest
from xdist.plugin import pytest_addoption


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service

        svj = Service("")
        driver = webdriver.Chrome(service=svj)
        return driver
    elif browser == "edge":
        from selenium import webdriver
        from selenium.webdriver.edge.service import Service

        svj = Service("")
        driver = webdriver.Edge(service=svj)
        return driver
    elif browser == "firefox":
        from selenium import webdriver
        from selenium.webdriver.firefox.service import Service

        svj = Service("")
        driver = webdriver.Firefox(service=svj)
        return driver

# getting browser value
def pytest_addoption(parser):
    parser.addoption("--browser")
    # parser.addini("metadata", type="args", help="add metadata", default=[])
@pytest.fixture()
def browser(request):
    return  request.config.getoption("--browser")

# customizing reHTML Report
# It is hook for Adding Environment info to HTML Report


# def pytest_configure(config):
#     for name in config.getini("metadata"):
#         config.metadata["Project name"] = 'Demo Site'
#         config.metadata['Module Name'] = 'Login Module'
#         config.metadata['Tester Name'] = 'Ravi Ranjan'

def pytest_configure(config):
    config.metadata={"Project name" : 'Demo Site',
                     'Module Name' : 'Login Module',
                     'Tester Name' : 'Ravi Ranjan'
                     }

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)