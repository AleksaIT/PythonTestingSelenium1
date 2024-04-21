import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

#ID, XPath, CSSSelector, Classname, name, linktext
driver.find_element(By.NAME,"email").send_keys("seleniumtester1337@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("IdeGas789&")
driver.find_element(By.ID,"exampleCheck1").click()
time.sleep(2)
#XPATH: //tagname[@atribute='value']  -> //input[@type='submit']
#CSSS: tagname[@atribute='value']  -> //input[@type='submit'] == #ID == .classname
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Tester")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio2").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
time.sleep(2)

assert "Success" in message   # if "Success" is present in message (1 - test pass, 0 - fail)

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("HelloAgain")
#driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()     #CLEAR
time.sleep(2)