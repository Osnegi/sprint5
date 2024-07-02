import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#идем в авторизацию
driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
time.sleep(2)

#идем на регистрацию
driver.find_element(By.XPATH, ".//a[text() = 'Зарегистрироваться']").click()
time.sleep(2)

#оказывается, мы уже зарегистрированы, идем в форму входу для авторизации
driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
driver.find_element(By.XPATH, ".//input[@name = 'name']").send_keys("OLgaSnegireva7@gmail.com")
driver.find_element(By.XPATH, ".//input[@name = 'Пароль']").send_keys("Privet12")
driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()time.sleep(3)

#переход в личный кабинет
driver.find_element(By.XPATH, ".//div/header/nav/a").click()
time.sleep(3)

#проверка, что вход в аккаунт выполнен успешно и по этим данным можно зайти в личный аккаунт и найти кнопку Выход
assert driver.find_element(By.XPATH, ".//button[text() = 'Выход']")

driver.quit()

