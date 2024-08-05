
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import Data
from locators import Locators

class TestStellarBurgersSauces:
    def test_pass_into_sauces(self, driver):
        #переход в соусы
        driver.find_element(*Locators.SAUCES_TO_SELECT).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(EC.element_to_be_clickable(Locators.SAUCES_IMAGE))

        #проверка, что переход в раздел Соусы выполнен успешно
        assert driver.find_element(*Locators.SAUCES_HEADER_SELECTED)