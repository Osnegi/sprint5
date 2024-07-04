import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersLogin:
    def test_login_button_private_cabinet(self, driver):
        #авторизация
        driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
        driver.find_element(By.XPATH, ".//input[@name = 'name']").send_keys("OLgaSnegireva7@gmail.com")
        driver.find_element(By.XPATH, ".//input[@name = 'Пароль']").send_keys("Privet12")
        driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Оформить заказ']")))

        #переход в личный кабинет
        driver.find_element(By.XPATH, ".//div/header/nav/a").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Сохранить']")))

        #проверка, что вход в аккаунт выполнен успешно и по этим данным можно зайти в личный аккаунт и найти кнопку Выход
        assert driver.find_element(By.XPATH, ".//button[text() = 'Выход']")



