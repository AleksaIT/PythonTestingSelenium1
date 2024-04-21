import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/client/auth/login")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("123456789")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()


