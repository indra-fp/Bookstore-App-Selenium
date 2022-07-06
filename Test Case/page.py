import time
from element import BasePageElement,StripePageElement
from locators import MainPageLocators, OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginUsername(BasePageElement):

    locator = "//input[@placeholder='email@address.com']"

class LoginPassword(BasePageElement):

    locator = "//input[@placeholder='password']"  



class InputEmail(BasePageElement):

    locator = "//input[@type='email']"

class InputPwd(BasePageElement):

    locator = "//input[@jsname='YPqjbf']"



class InputForgotEmail(BasePageElement):

    locator = "//input[@placeholder='email@address.com']"



class SignUpUsername(BasePageElement):

    locator = "//input[@placeholder='address@example.com']"

class SignUpPassword(BasePageElement):

    locator = "//input[@placeholder='password']"

class SignUpRetype(BasePageElement):

    locator = "//input[@placeholder='repeat password']" 



class StripeInputEmail(StripePageElement):

    locator = "email"

class StripeInputCCNumber(StripePageElement):

    locator = "card_number"

class StripeInputDate(StripePageElement):

    locator = "cc-exp" 

class StripeInputCVC(StripePageElement):

    locator = "cc-csc" 



class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    inputusername = LoginUsername()
    inputpassword = LoginPassword()

    inputemail = InputEmail()
    inputpwd = InputPwd()

    inputforgotemail = InputForgotEmail()

    signupusername = SignUpUsername()
    signuppassword = SignUpPassword()
    signupretype = SignUpRetype()

    

    def error_text_master(self):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH,"//div[contains(@style,'color: red')]")
        if "disabled" in element.text:
            time.sleep(5)
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_3)
            return True
        elif "Incorrect" in element.text:
            time.sleep(5)
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT)
            return True
        elif "reset" in element.text:
            time.sleep(5)
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_2) #error reset must change
            return True
        elif "confirmed" in element.text:
            time.sleep(5)
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_4)
            return True
        elif "exist" in element.text:
            time.sleep(5)
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_5)
            return True
        elif "Enter" in element.text:
            time.sleep(5)
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_6)
            return True
        elif "characters" in element.text:
            time.sleep(5)
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_7)
            return True
        elif "match" in element.text:
            time.sleep(5)
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_8)
            return True
        elif "leaked" in element.text:
            time.sleep(5)
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_9)
            return True
        else:
            return False

    def confirm_text_master(self):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH,"//h4[contains(text(),'Confirm your Email')]")
        if "Confirm your Email" in element.text:
            element = self.driver.find_element(*MainPageLocators.CONFIRM_TEXT)
            return True
        else:
            return False

    def click_signin_button(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.SIGNIN_BUTTON)
        #element = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.to-disable") #<<< ini jadi cok
        element.click()

    def click_login_button_inside(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON_INSIDE)
        element.click()

    def wait_element_present(self):
        wait = WebDriverWait(self.driver, 2)
        #wait.until(EC.presence_of_element_located(MainPageLocators.EMAIL_PRESENT))
        wait.until(EC.visibility_of_element_located(MainPageLocators.EMAIL_PRESENT))
        return True


    def click_sign_in_google(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.GOOGLE_SIGNIN)
        element.click()
        time.sleep(5)

    def click_next_google(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.POPUP_NEXT_GOOGLE)
        element.click()

    def click_forgot_password(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.FORGOT_PASSWORD)
        element.click()

    def click_OK_forgot_password(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.OK_FORGOT_PASSWORD)
        element.click()


    def click_new_account(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.NEW_ACCOUNT)
        element.click()

    def click_signup_button(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.SIGNUP_BUTTON)
        element.click()




    def click_view_pdf_button(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.VIEW_PDF_BUTTON)
        element.click()

    def check_inside_booklist(self):
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.visibility_of_element_located(MainPageLocators.TITLE_BOOKLIST))
        time.sleep(3)
        return True


    def click_mybooks(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.MYBOOKS_BUTTON)
        element.click()

    def check_inside_mybooks(self):
        wait = WebDriverWait(self.driver, 8)
        element = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span[contains(@class,'label-text')]")

        if "inventory" in element.text: 
            wait.until(EC.visibility_of_element_located(MainPageLocators.TITLE_MYBOOKS_2))
            return True
        elif "Booklist" in element.text:
            wait.until(EC.visibility_of_element_located(MainPageLocators.TITLE_MYBOOKS_1))
            return True
        else:
            return False

    def logout(self):
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.EMAIL_PRESENT)
        element.click()
        time.sleep(5)
        element = self.driver.find_element(*MainPageLocators.LOGOUT_Y)
        element.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(MainPageLocators.SIGNIN_BUTTON))
        time.sleep(2)
        return True



class OrderPage(BasePage):

    stripeinputemail = StripeInputEmail()
    stripeinputccnumber = StripeInputCCNumber()
    stripeinputdate = StripeInputDate()
    stripeinputcvc = StripeInputCVC()
        

    def orderbooksC(self): 
        time.sleep(5)
        element  = self.driver.find_element(*OrderPageLocators.ORDER_C)
        element.click()
        return True

    def orderbooksPY(self):
        time.sleep(5)
        element  = self.driver.find_element(*OrderPageLocators.ORDER_PY)
        element.click()
        return True

    def orderbooksJS(self):
        time.sleep(5)
        element  = self.driver.find_element(*OrderPageLocators.ORDER_JS)
        element.click()
        return True        


    def ordercheck(self):
        wait = WebDriverWait(self.driver, 5)
        time.sleep(5)
        element = self.driver.find_element(By.XPATH,"//span[contains(text(),'Rp')]")
        print(element.text)
        if "100000" in element.text:
            wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_TITLE_C))
            wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_DESC_C))
            wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_PRICE_C))
            return True
        elif "150000" in element.text:
            wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_TITLE_PY))
            wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_DESC_PY))
            wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_PRICE_PY))
            return True
        elif "200000" in element.text:
            wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_TITLE_JS))
            wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_DESC_JS))
            wait.until(EC.visibility_of_element_located(OrderPageLocators.ORDER_PRICE_JS))
            return True
        else:
            return False


    def click_back(self):
        time.sleep(5)
        element = self.driver.find_element(*OrderPageLocators.BACK_BUTTON)
        element.click()



    def check_login(self):
        time.sleep(5)
        #debatable and maybe will not work for some other things
        user = self.driver.get_cookies()
        print(len(user))
        if len(user) > 3:
            return True
        else:
            return False


    def buy_now(self):
        time.sleep(2)
        element = self.driver.find_element(*OrderPageLocators.BUY_NOW_BUTTON)
        element.click()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        if OrderPage.check_login(self) is False:
            wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_LABEL))
            return True    
        elif OrderPage.check_login(self) is True:
            time.sleep(5)
            try : 
                iframe = self.driver.find_element(*OrderPageLocators.IFRAME_PAYMENT)
                self.driver.switch_to.frame(iframe)
                wait.until(EC.visibility_of_element_located(OrderPageLocators.STRIPE_PAYMENT))
                return True
            except NoSuchElementException:
                wait.until(EC.visibility_of_element_located(OrderPageLocators.BOOK_EXIST))
                return True
        else:
            return False    

    def paybutton(self):
        time.sleep(5)
        element = self.driver.find_element(*OrderPageLocators.PAY_RP)
        element.click()
           
    def stripe_payment_check(self):
        wait = WebDriverWait(self.driver, 10)
        try :
            wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_EXIST))
            return True
        except NoSuchElementException:
            return False

            

"""def error_text(self):
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.presence_of_element_located(MainPageLocators.ERROR_TEXT))
        return True

    def error_text_2(self):
        try:
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_2)
            return True
        except AssertionError:
            return False

    def error_text_3(self):
        try:
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_3)
            return True
        except AssertionError:
            return False

    def error_text_4(self):
        try:
            element = self.driver.find_element(*MainPageLocators.ERROR_TEXT_4)
            return True
        except AssertionError:
            return False"""