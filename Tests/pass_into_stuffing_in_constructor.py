
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestStellarBurgersLogin:
    def test_stuffing(self, driver):
        #переход в начинки
        driver.find_element(By.XPATH, ".//div/main/section[1]/div[1]/div[3]/span").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//img[@alt = 'Филе Люминесцентного тетраодонтимформа']")))

        #проверка, что переход в раздел Начинки выполнен успешно
        assert (driver.find_element(By.XPATH, ".//div/main/section[1]/div[2]/h2[3]").get_attribute('innerHTML')) == 'Начинки'


