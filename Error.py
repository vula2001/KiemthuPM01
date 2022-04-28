# bài phát hiện ra lỗi kí tự đăng nhập

import time
import unittest
from selenium import webdriver


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://pvc-ch16-deployment.herokuapp.com/accounts/signup/")

    def test_title_google(self):
        sign_up_input = self.driver.find_element_by_name("username")
        sign_up_input.send_keys("$$$$")

        password_input = self.driver.find_element_by_name("password1")
        password_input.send_keys("cuongvip007")

        confirm_password_input = self.driver.find_element_by_name("password2")
        confirm_password_input.send_keys("cuongvip007")

        sign_up_button = self.driver.find_element_by_xpath(
            "/html/body/main/div/form/button")
        sign_up_button.click()

        time.sleep(3)
        error_label = self.driver.find_element_by_id("error_1_id_username")

        error_text = error_label.text

        print(error_text)
        self.assertEqual(error_text,
                         "Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.")

    # def test_login(self):
    #     pass

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
