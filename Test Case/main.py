import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import page
from selenium.webdriver.support import expected_conditions as EC
import time
from locators import MainPageLocators, OrderPageLocators
from selenium.common.exceptions import NoSuchElementException  


#import undetected_chromedriver as uc

# pip install undetected_chromedriver     
# more code needed if using proxy to access UC

#login-logout per section

class classlogin(object):
    def loginrepeatable(self):
        main_page = page.MainPage(self.driver)
        time.sleep(3)
        main_page.click_signin_button()
        time.sleep(2)
        main_page.inputusername = "xeked26444@abincol.com"
        main_page.inputpassword = "xeked26444"
        time.sleep(5)
        main_page.click_login_button_inside()
        time.sleep(5)
        assert main_page.wait_element_present()

    def loginrepeatable2(self):
        main_page = page.MainPage(self.driver)
        time.sleep(3)
        main_page.click_signin_button()
        time.sleep(2)
        main_page.inputusername = "sikika3561@hbehs.com"
        main_page.inputpassword = "sikika3561"
        time.sleep(5)
        main_page.click_login_button_inside()
        time.sleep(5)
        assert main_page.wait_element_present()

class TestCase(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        #self.driver = uc.Chrome()
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://partial-tense-thrasher.anvil.app/")
       #driver = uc.Chrome()

    def test_login002(self):

        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        main_page.inputusername = ""
        main_page.inputpassword = ""
        time.sleep(5)
        main_page.click_login_button_inside()
        time.sleep(5)
        assert main_page.error_text_master()

    def test_login003(self):

        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        main_page.inputusername = "xeked26444@abincol.com"
        main_page.inputpassword = "xeked26444"
        time.sleep(5)
        main_page.click_login_button_inside()
        time.sleep(5)
        assert main_page.wait_element_present()
         

    def atest_login004_1(self):

        #wrong password
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        main_page.inputusername = "xeked26444@abincol.com"
        main_page.inputpassword = "12345"
        time.sleep(5)
        main_page.click_login_button_inside()
        time.sleep(5)
        assert main_page.error_text_master()

    def atest_login004_2(self):

        #wrong email
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        main_page.inputusername = "xeked26444@abincol."
        main_page.inputpassword = "xeked26444"
        time.sleep(5)
        main_page.click_login_button_inside()
        time.sleep(5)
        assert main_page.error_text_master()

    def atest_login004_3(self):

        #both incorrect
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        main_page.inputusername = "12"
        main_page.inputpassword = "a"
        time.sleep(5)
        main_page.click_login_button_inside()
        time.sleep(5)
        assert main_page.error_text_master()

    def atest_login005(self):

        #will not worked properly
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(5)

        window_before = self.driver.window_handles[0]

        main_page.click_sign_in_google()
        time.sleep(5)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        try:
            self.driver.find_element(*MainPageLocators.POPUP_INPUT_GOOGLE)
            main_page.inputemail = "iid.mailed@gmail.com"
            time.sleep(5)
            main_page.click_next_google()
            main_page.inputpwd = "testingpasswordforanvil"
            time.sleep(5)
            main_page.click_next_google()
            time.sleep(5)
            assert True
        except NoSuchElementException:
            assert False
        
    
    def atest_login008(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(5)
        main_page.click_forgot_password()
        main_page.inputforgotemail = 'xeked26444@abincol.com'
        time.sleep(5)
        main_page.click_OK_forgot_password()
        time.sleep(5)
        assert main_page.error_text_master()

    def atest_login009(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(5)
        main_page.click_forgot_password()
        main_page.inputforgotemail = 'xeked26@abincol.com'
        time.sleep(5)
        main_page.click_OK_forgot_password()
        time.sleep(5)
        assert main_page.error_text_master()

    def test_login010(self):

        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        main_page.inputusername = "hijoba3528@abincol.com"
        main_page.inputpassword = "hijoba3528"
        time.sleep(5)
        main_page.click_login_button_inside()
        time.sleep(5)
        assert main_page.error_text_master()

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()