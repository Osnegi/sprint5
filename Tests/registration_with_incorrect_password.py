import random
from selenium.webdriver.common.by import By

class TestStellarBurgersLogin:
    def test_incorrect_password(self, driver):# регистрация
        driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
        driver.find_element(By.XPATH, ".//a[text() = 'Зарегистрироваться']").click()

        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("DAN")
        email = f"OSneg7_{random.randint(100, 999)}@gmail.com"
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(email)
        driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys("12345")
        driver.find_element(By.XPATH, ".//button").click()

        #проверка, что регистрация НЕ прошла успешно (не произошло перехода на форму авторизации) и появилась ошибка Некорректный пароль
        assert (not ((driver.find_element(By.XPATH, ".//div/main/div/h2").get_attribute('innerHTML')) == 'Вход')) and (driver.find_element(By.XPATH, ".//div/main/div/form/fieldset[3]/div/p").get_attribute('innerHTML') == 'Некорректный пароль')


