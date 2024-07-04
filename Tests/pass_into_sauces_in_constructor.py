
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestStellarBurgersLogin:
    def test_sauces(self, driver):
        #переход в соусы
        driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//img[@alt = 'Соус с шипами Антарианского плоскоходца']")))

        #проверка, что переход в раздел Соусы выполнен успешно
        assert (driver.find_element(By.XPATH, ".//div/main/section[1]/div[2]/h2[2]").get_attribute('innerHTML')) == 'Соусы'

