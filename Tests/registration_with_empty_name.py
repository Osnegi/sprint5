import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# регистрация
driver.find_element(By.XPATH, ".//button[text() = 'Войти в аккаунт']").click()
time.sleep(3)
driver.find_element(By.XPATH, ".//a[text() = 'Зарегистрироваться']").click()
time.sleep(3)

driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("")
email = f"OSneg7_{random.randint(100, 999)}@gmail.com"
driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(email)
driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys("Privet12")
driver.find_element(By.XPATH, ".//button").click()
time.sleep(3)

#проверка, что регистрация НЕ прошла успешно (не произошло перехода на форму авторизации)
assert not ((driver.find_element(By.XPATH, ".//div/main/div/h2").get_attribute('innerHTML')) == 'Вход')

driver.quit()

