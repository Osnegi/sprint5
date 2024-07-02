import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переход в соусы
driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click()
time.sleep(10)

#переход в булки
driver.find_element(By.XPATH, ".//span[text() = 'Булки']").click()
time.sleep(10)

#проверка, что переход в раздел булки выполнен успешно
assert (driver.find_element(By.XPATH, ".//div/main/section[1]/div[2]/h2[2]").get_attribute('innerHTML')) == 'Булки'

driver.quit()
