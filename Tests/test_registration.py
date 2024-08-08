
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Data
from helpers import Help
from locators import Locators

class TestStellarBurgersRegistration:
    def test_registration(self, driver):
        # регистрация
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()

        driver.find_element(*Locators.REG_NAME).send_keys(Data.REG_NAME)
        email = Help.generate_email()
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))

        #авторизация

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))

        #переход в личный кабинет
        driver.find_element(*Locators.PASS_INTO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.SAVE_BUTTON))

        #проверка, что регистрация прошла успешно и по этим данным можно зайти в личный аккаунт и найти кнопку Выход
        assert driver.find_element(*Locators.EXIT_BUTTON)