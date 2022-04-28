# test trang sinhvien.edu


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://sinhvien.donga.edu.vn/Sinh-vien/dang-nhap?ReturnUrl=%2f")

user_input = driver.find_element_by_name("UserName")
user_input.send_keys("47983")

password_input = driver.find_element_by_name("Password")
password_input.send_keys("vulieu474")

sign_up_button = driver.find_element_by_xpath(
    "/html/body/div[2]/div/div[2]/div[2]/div/form/div[3]/button")
sign_up_button.click()



