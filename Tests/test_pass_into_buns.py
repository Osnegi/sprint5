from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Data
from locators import Locators


class TestStellarBurgersBuns:
    def test_pass_into_buns(self, driver):
        #переход в начинки
        driver.find_element(*Locators.STUFFING_TO_SELECT).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.STUFFING_HEADER))

        #переход в булки
        driver.find_element(*Locators.BUNS_TO_SELECT).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.BUNS_IMAGE))

        #проверка, что переход в раздел булки выполнен успешно
        assert driver.find_element(*Locators.BUNS_HEADER_SELECTED)


