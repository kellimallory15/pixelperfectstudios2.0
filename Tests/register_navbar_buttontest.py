import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        driver = self.driver
        driver.maximize_window()

        driver.get("http://127.0.0.1:8000")
        time.sleep(2)
        try:
            # Find and click the 'Account' button
            account_dropdown_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Account')]")
            account_dropdown_button.click()
            time.sleep(1)

            # Click the 'Register' button
            register_button = driver.find_element(By.LINK_TEXT, "Register")
            register_button.click()

            time.sleep(3)

            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("User is unable to press the 'Register' button in the navbar and be taken to the 'Register' page that allows people to create an account")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()