import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#авторизация
driver.find_element(By.XPATH, ".//div/main/section[2]/div/button").click()
driver.find_element(By.XPATH, ".//div/main/div/form/fieldset[1]/div/div/input").send_keys("OLgaSnegireva7@gmail.com")
driver.find_element(By.XPATH, ".//div/main/div/form/fieldset[2]/div/div/input").send_keys("Privet12")
driver.find_element(By.XPATH, ".//div/main/div/form/button").click()
time.sleep(3)

#переход в личный кабинет
driver.find_element(By.XPATH, ".//div/header/nav/a").click()
time.sleep(3)

#переход в конструктор
driver.find_element(By.XPATH, ".//p[text() = 'Конструктор']").click()
time.sleep(3)

#проверка, что переход в конструктор выполнен успешно
assert (driver.find_element(By.XPATH, ".//div/main/section[1]/h1").get_attribute('innerHTML')) == 'Соберите бургер'

driver.quit()
