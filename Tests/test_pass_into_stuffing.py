
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Data
from locators import Locators

class TestStellarBurgersStuffing:
    def test_pass_into_stuffing(self, driver):
        #переход в начинки
        driver.find_element(*Locators.STUFFING_TO_SELECT).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.STUFFING_HEADER))

        # проверка, что переход в раздел Начинки выполнен успешно
        assert driver.find_element(*Locators.STUFFING_HEADER_SELECTED)
