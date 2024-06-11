import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in checkboxes:
    # <input id="checkBoxOption1" value="option1" name="checkBoxOption1" type="checkbox" xpath="1" style="">
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()   #da li je selektovan?
        break
time.sleep(2)
radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
radiobuttons[2].click()         #ne mora proveriti jer ne mzoe da se odcekira
assert radiobuttons[2].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(2)
driver.find_element(By.ID,"hide-textbox").click()
time.sleep(2)
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
