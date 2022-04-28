import pickle
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://pvc-ch16-deployment.herokuapp.com/")

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.get("http://pvc-ch16-deployment.herokuapp.com/")
# time.sleep(10)
# driver.quit()
