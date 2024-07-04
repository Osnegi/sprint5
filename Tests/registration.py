import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestStellarBurgersLogin:
    def test_registration(self, driver):
        # регистрация
        driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
        driver.find_element(By.XPATH, ".//a[text() = 'Зарегистрироваться']").click()

        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("Dan")
        email = f"OSneg7_{random.randint(100, 999)}@gmail.com"
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(email)
        driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys("Privet12")
        driver.find_element(By.XPATH, ".//button").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Войти']")))

        #авторизация

        driver.find_element(By.XPATH, ".//input[@name = 'name']").send_keys("OLgaSnegireva7@gmail.com")
        driver.find_element(By.XPATH, ".//input[@name = 'Пароль']").send_keys("Privet12")
        driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Оформить заказ']")))

        #переход в личный кабинет
        driver.find_element(By.XPATH, ".//div/header/nav/a").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Сохранить']")))

        #проверка, что регистрация прошла успешно и по этим данным можно зайти в личный аккаунт и найти кнопку Выход
        assert driver.find_element(By.XPATH, ".//button[text() = 'Выход']")

