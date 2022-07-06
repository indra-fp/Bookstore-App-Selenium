from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    #GO_BUTTON = (By.ID, 'submit')
    SIGNIN_BUTTON           = (By.XPATH,"//span[text()='Sign In']")
    LOGIN_LABEL             = (By.XPATH,"//h4[text()='Log In']")
    LOGIN_BUTTON_INSIDE     = (By.XPATH,"//button[text()='Log In']")


    EMAIL_PRESENT           = (By.XPATH,"//span[contains(text(),'@')]")
    LOGOUT_Y                = (By.XPATH,"//button[text()='Yes']")

    ERROR_TEXT              = (By.XPATH,"//span[text()='Incorrect email address or password']")
    ERROR_TEXT_2            = (By.XPATH,"//span[contains(text(),'password reset')]")
    ERROR_TEXT_3            = (By.XPATH,"//span[contains(text(),'User disabled')]")
    ERROR_TEXT_4            = (By.XPATH,"//span[contains(text(),'confirmed your email address')]")
    ERROR_TEXT_5            = (By.XPATH,"//span[contains(text(),'This user already exist')]")
    ERROR_TEXT_6            = (By.XPATH,"//span[contains(text(),'Enter an email address')]")
    ERROR_TEXT_7            = (By.XPATH,"//span[contains(text(),'Passwords must be 8 characters or more')]")
    ERROR_TEXT_8            = (By.XPATH,"//span[contains(text(),'Passwords do not match')]")
    ERROR_TEXT_9            = (By.XPATH,"//span[contains(text(),'previously been leaked and posted')]")
    
    CONFIRM_TEXT            = (By.XPATH,"//h4[contains(text(),'Confirm your Email')]")

    GOOGLE_SIGNIN           = (By.XPATH,"//div[contains(@src,'/google-signin-buttons/')]")
    POPUP_INPUT_GOOGLE      = (By.XPATH,"//input[@type = 'email']")
    POPUP_INPUT_GOOGLE_PWD  = (By.XPATH,"//input[@type = 'password']")
    POPUP_NEXT_GOOGLE       = (By.XPATH,"//span[@jsname = 'V67aGc']")

    FORGOT_PASSWORD         = (By.XPATH,"//div[(text()='Forgot your password?')]")
    OK_FORGOT_PASSWORD      = (By.XPATH,"//button[text()='OK']")

    NEW_ACCOUNT             = (By.XPATH,"//div[(text()='Sign up for a new account')]")
    SIGNUP_BUTTON           = (By.XPATH,"//button[text()='Sign Up']")

    VIEW_PDF_BUTTON         = (By.XPATH,"//span[contains(text(),'View ebooks and pdf list')]")
    TITLE_BOOKLIST          = (By.XPATH,"//span[contains(text(),'List of Books and PDF')]")

    MYBOOKS_BUTTON          = (By.XPATH,"//div[contains(text(),'My Books')]")
    TITLE_MYBOOKS_1         = (By.XPATH,"//span[contains(text(),'My Booklist')]")
    TITLE_MYBOOKS_2         = (By.XPATH,"//span[contains(text(),'have books in your inventory')]")


class OrderPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    ORDER_C                 = (By.XPATH,"//span[contains(text(),'100000')]")
    ORDER_JS                = (By.XPATH,"//span[contains(text(),'200000')]") 
    ORDER_PY                = (By.XPATH,"//span[contains(text(),'150000')]")

    ORDER_TITLE_C           = (By.XPATH,"//span[contains(text(),'CCplusplus')]")
    ORDER_TITLE_PY          = (By.XPATH,"//span[contains(text(),'Python')]")
    ORDER_TITLE_JS          = (By.XPATH,"//span[contains(text(),'Javascript')]")

    ORDER_DESC_C            = (By.XPATH,"//span[contains(text(),'shortcourse')]")
    ORDER_DESC_PY           = (By.XPATH,"//span[contains(text(),'guide')]")
    ORDER_DESC_JS           = (By.XPATH,"//span[contains(text(),'ebook')]")

    ORDER_PRICE_C           = (By.XPATH,"//span[contains(text(),'100000')]")
    ORDER_PRICE_PY          = (By.XPATH,"//span[contains(text(),'150000')]")
    ORDER_PRICE_JS          = (By.XPATH,"//span[contains(text(),'200000')]")

    BACK_BUTTON             = (By.XPATH,"//i[contains(@Class, 'fa-arrow-left')]")

    BUY_NOW_BUTTON          = (By.XPATH,"//span[contains(text(), 'Buy NOW')]")

    IFRAME_PAYMENT          = (By.NAME, "stripe_checkout_app")
    STRIPE_PAYMENT          = (By.CLASS_NAME,"brandingLogoView")

    BOOK_EXIST              = (By.XPATH,"//div[contains(text(),'already buy this book')]")

    PAY_RP                  = (By.XPATH,"//span[contains(text(),'Pay')]")

    SUCCESS_EXIST           = (By.XPATH,"//div[contains(text(),'Success')]")

    #unused
    STRIPE_EMAIL            = (By.ID,"email")
    STRIPE_CCNUM            = (By.ID,"card_number")
    STRIPE_EXPDATE          = (By.ID,"cc-exp")
    STRIPE_CVC              = (By.ID,"cc-csc")
