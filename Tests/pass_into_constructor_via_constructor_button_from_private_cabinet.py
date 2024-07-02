import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#авторизация
driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
driver.find_element(By.XPATH, ".//input[@name = 'name']").send_keys("OLgaSnegireva7@gmail.com")
driver.find_element(By.XPATH, ".//input[@name = 'Пароль']").send_keys("Privet12")
driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()

WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Оформить заказ']")))

#переход в личный кабинет
driver.find_element(By.XPATH, ".//div/header/nav/a").click()

WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Сохранить']")))

#переход в конструктор
driver.find_element(By.XPATH, ".//p[text() = 'Конструктор']").click()

#проверка, что переход в конструктор выполнен успешно
assert (driver.find_element(By.XPATH, ".//div/main/section[1]/h1").get_attribute('innerHTML')) == 'Соберите бургер'

driver.quit()
