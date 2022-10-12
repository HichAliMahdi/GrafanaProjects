from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://dashboard.oxxodata.net/d/CgP1keZVk/aymen-promotion?orgId=1&from=now-30d&to=now&inspect=2&inspectTab=data")
driver.implicitly_wait(12.5)
username = driver.find_element_by_class_name("css-yn255a-input-input")
password = driver.find_element_by_id("current-password")
username.send_keys("admin")
password.send_keys("OxxoData2608!")
driver.find_element_by_class_name("css-14g7ilz-button").click()
driver.implicitly_wait(10.0)
driver.find_element_by_class_name("css-obkt16-button").click()
