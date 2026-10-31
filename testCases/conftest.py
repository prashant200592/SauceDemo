import pytest
from selenium import webdriver
import os
from datetime import datetime

@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_html_report_title(report):
    report.title = "Automation Results"

def pytest_html_results_summary(prefix,summary,postfix):
    prefix.extend([
        "Tester: Prashant"
    ])

def pytest_metadata(metadata,config):
    metadata.pop("JAVA_HOME", None)
    metadata["Project"] = "Sauce Demo"
    metadata["Browser"] = config.getoption("--browser")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir+"\\reports\\"+datetime.now().strftime("%Y%m%d-%H%M%S")+".html")

