import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#переход в начинки
driver.find_element(By.XPATH, ".//div/main/section[1]/div[1]/div[3]/span").click()
time.sleep(8)

#проверка, что переход в раздел Начинки выполнен успешно
assert (driver.find_element(By.XPATH, ".//div/main/section[1]/div[2]/h2[3]").get_attribute('innerHTML')) == 'Начинки'

driver.quit()
