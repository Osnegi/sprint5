from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Data
from locators import Locators

class TestStellarBurgersLoginAccount:
    def test_login_button_account(self, driver, login):

#переход в личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))
        driver.find_element(*Locators.PASS_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.SAVE_BUTTON))

#проверка, что вход в аккаунт выполнен успешно и по этим данным можно зайти в личный аккаунт и найти кнопку Выход
        assert driver.find_element(*Locators.EXIT_BUTTON)


