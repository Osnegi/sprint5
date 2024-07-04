from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersLogin:
    def test_buns(self, driver):
        #переход в начинки
        driver.find_element(By.XPATH, ".//span[text() = 'Начинки']").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//img[@alt = 'Филе Люминесцентного тетраодонтимформа']")))

        #переход в булки
        driver.find_element(By.XPATH, ".//span[text() = 'Булки']").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")))


        #проверка, что переход в раздел булки выполнен успешно
        assert (driver.find_element(By.XPATH, ".//h2").get_attribute('innerHTML')) == 'Булки'


