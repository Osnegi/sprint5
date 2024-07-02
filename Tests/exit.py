import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
driver.find_element(By.XPATH, ".//input[@name = 'name']").send_keys("OLgaSnegireva7@gmail.com")
driver.find_element(By.XPATH, ".//input[@name = 'Пароль']").send_keys("Privet12")
driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Оформить заказ']")))

#вход в личный аккаунт
driver.find_element(By.XPATH, ".//div/header/nav/a").click()

WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Сохранить']")))

#выход из личного кабинета
driver.find_element(By.XPATH, ".//button[text() = 'Выход']").click()

WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Войти']")))

assert (driver.find_element(By.XPATH, ".//div/main/div/h2").get_attribute('innerHTML')) == 'Вход'
driver.quit()

