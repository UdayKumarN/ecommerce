from selenium import webdriver
import pytest
from datetime import date


@pytest.fixture()

def setup():
    driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    return driver

def pytest_html_report_title(report):
    ''' modifying the title  of html report'''
    report.title = "Login and Add Customer Test Report:: Test Suite"

def pytest_configure(config):
    config._metadata["Title"] = "Login & Add customer"
    config._metadata["Environment"] = "Test"
    today = date.today()
    config._metadata["Job run Date"] = today