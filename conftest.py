import pytest
from selenium import webdriver
from constants import Data
from locators import Locators

@pytest.fixture (scope = 'function')
def driver():
    browser = webdriver.Chrome()
    browser.get(Data.STELLARBURGERS_URL)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    # авторизация через вход в аккаунт
    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.AUTH_EMAIL)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.AUTH_PASSWORD)
    driver.find_element(*Locators.ENTER_BUTTON).click()
    return driver