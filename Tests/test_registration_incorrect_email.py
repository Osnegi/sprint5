from constants import Data
from helpers import Help
from locators import Locators

class TestStellarBurgersIncorrectEmail:
    def test_reg_incorrect_email(self, driver):
        # регистрация
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_LINK).click()

        driver.find_element(*Locators.REG_NAME).send_keys(Data.REG_NAME)
        email = Help.generate_incorrect_email()
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*Locators.REG_BUTTON).click()

        #проверка, что регистрация НЕ прошла успешно (не произошло перехода на форму авторизации)
        assert driver.find_element(*Locators.REG_BUTTON)


