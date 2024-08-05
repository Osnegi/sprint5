
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Data
from locators import Locators


class TestStellarBurgersConstructor:
    def test_pass_constructor_from_cainet(self, driver, login):
        #переход в личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))
        driver.find_element(*Locators.PASS_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.SAVE_BUTTON))

        #переход в конструктор
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        #проверка, что переход в конструктор выполнен успешно
        assert driver.find_element(*Locators.GET_BURGER_HEADER)

