from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Data
from locators import Locators

class TestStellarBurgersLoginRestore:
    def test_login_button_restore_password(self, driver):
#идем в авторизацию через вход в аккаунт
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()

#идем восстанавливать пароль
        driver.find_element(*Locators.RESTORE_PASSWORD_LINK).click()

#идем в форму входу для авторизации
        driver.find_element(*Locators.ENTER_LINK_IN_RESTORE_PASSWORD).click()

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()

#переход в личный кабинет
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))
        driver.find_element(*Locators.PASS_INTO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.SAVE_BUTTON))

#проверка, что вход в аккаунт выполнен успешно и по этим данным можно зайти в личный аккаунт и найти кнопку Выход
        assert driver.find_element(*Locators.EXIT_BUTTON)


