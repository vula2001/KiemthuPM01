# bài dangnhap app

import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://pvc-ch16-deployment.herokuapp.com/")

login_button = driver.find_element_by_link_text("Log In")
login_button.click()

user_input = driver.find_element_by_name("username")
user_input.send_keys("demo")

password_input = driver.find_element_by_name("password")
password_input.send_keys("cuongvip007")

login = driver.find_element_by_xpath("/html/body/main/div/form/button")
login.click()

pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

time.sleep(15)
driver.quit()
