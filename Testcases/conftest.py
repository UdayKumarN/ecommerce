from selenium import webdriver
import pytest

@pytest.fixture()

def setup():
    driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    return driver