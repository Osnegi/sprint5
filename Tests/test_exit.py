
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Data
from locators import Locators

class TestStellarBurgersExit:
    def test_exit(self, driver, login):

        # переход в личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))
        driver.find_element(*Locators.PASS_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.SAVE_BUTTON))

        #выход из личного кабинета
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
        assert driver.find_element(*Locators.HEADER_ENTER)


