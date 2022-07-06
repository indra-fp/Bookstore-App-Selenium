 def test_signup002(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = "gegise3765@chokxus.com"
        main_page.signuppassword = "gegise3765"
        main_page.signupretype = "gegise3765"
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.confirm_text_master()


    def test_signup003(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = "xeked26444@abincol.com"
        main_page.signuppassword = "xeked26444"
        main_page.signupretype = "xeked26444"
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.error_text_master()

    def test_signup004(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = ""
        main_page.signuppassword = ""
        main_page.signupretype = ""
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.error_text_master()


    def test_signup005_1(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = "hijoba3528abincol.com"
        main_page.signuppassword = "hijoba3528"
        main_page.signupretype = "hijoba3528"
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.error_text_master()


    def test_signup005_2(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = "hijoba3528@abincol"
        main_page.signuppassword = "hijoba3258"
        main_page.signupretype = "hijoba3258"
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.error_text_master()

    def test_signup006(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = "hijoba3528@abincol"
        main_page.signuppassword = ""
        main_page.signupretype = ""
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.error_text_master()

    def test_signup007(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = "hijoba3528@abincol.com"
        main_page.signuppassword = ""
        main_page.signupretype = ""
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.error_text_master()

    def test_signup008(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = "hijoba3528@abincol.com"
        main_page.signuppassword = "zxcpo"
        main_page.signupretype = "zxcpo"
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.error_text_master()

    def test_signup009(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = "hijoba3528@abincol.com"
        main_page.signuppassword = "zxcpo123"
        main_page.signupretype = "zxcpoqwerty"
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.error_text_master()


    def test_signup010(self):
        main_page = page.MainPage(self.driver)
        main_page.click_signin_button()
        time.sleep(3)
        main_page.click_new_account()
        time.sleep(3)
        main_page.signupusername = "hijoba3528@abincol.com"
        main_page.signuppassword = "12345678"
        main_page.signupretype = "12345678"
        time.sleep(3)
        main_page.click_signup_button()
        time.sleep(3)
        assert main_page.error_text_master()


    def test_homepage003(self):
        main_page = page.MainPage(self.driver)
        time.sleep(5)
        main_page.click_view_pdf_button()
        time.sleep(2)
        assert main_page.check_inside_booklist()

    def test_homepage004(self):
        classlogin.loginrepeatable(self)
        main_page = page.MainPage(self.driver)
        main_page.click_mybooks()
        time.sleep(5)
        assert main_page.check_inside_mybooks()


    def test_homepage007(self):
        classlogin.loginrepeatable(self)
        main_page = page.MainPage(self.driver)
        time.sleep(2)
        assert main_page.logout()

    
    def test_purchase002_1(self):
        classlogin.loginrepeatable(self)
        order_page = page.MainPage(self.driver)
        time.sleep(2)
        order_page.click_view_pdf_button()
        time.sleep(5)

        order_page = page.OrderPage(self.driver)
        time.sleep(5)
        order_page.orderbooksC()
        assert order_page.ordercheck()
        
    def test_purchase002_2(self):
        classlogin.loginrepeatable(self)
        order_page = page.MainPage(self.driver)
        time.sleep(2)
        order_page.click_view_pdf_button()
        time.sleep(5)

        order_page = page.OrderPage(self.driver)
        time.sleep(5)
        order_page.orderbooksPY()
        assert order_page.ordercheck()
        
    def test_purchase002_3(self):
        classlogin.loginrepeatable(self)
        order_page = page.MainPage(self.driver)
        time.sleep(2)
        order_page.click_view_pdf_button()
        time.sleep(5)

        order_page = page.OrderPage(self.driver)
        time.sleep(5)
        order_page.orderbooksJS()
        assert order_page.ordercheck()
        

    def test_purchase003_1(self):
        TestCase.test_purchase002_1(self)
        order_page = page.OrderPage(self.driver)
        time.sleep(3)
        order_page.click_back()
        order_page = page.MainPage(self.driver)
        assert order_page.check_inside_booklist()

    def test_purchase003_2(self):
        TestCase.test_purchase002_2(self)
        order_page = page.OrderPage(self.driver)
        time.sleep(3)
        order_page.click_back()
        order_page = page.MainPage(self.driver)
        assert order_page.check_inside_booklist()

    def test_purchase003_3(self):
        TestCase.test_purchase002_3(self)
        order_page = page.OrderPage(self.driver)
        time.sleep(3)
        order_page.click_back()
        order_page = page.MainPage(self.driver)
        assert order_page.check_inside_booklist()

    def test_purchase004_1(self):
        TestCase.test_purchase002_1(self)
        order_page = page.OrderPage(self.driver)
        assert order_page.ordercheck()

    def test_purchase004_2(self):
        TestCase.test_purchase002_2(self)
        order_page = page.OrderPage(self.driver)
        assert order_page.ordercheck()

    def test_purchase004_3(self):
        TestCase.test_purchase002_3(self)
        order_page = page.OrderPage(self.driver)
        assert order_page.ordercheck()

    def test_purchase005_1(self):
        order_page = page.MainPage(self.driver)
        time.sleep(5)
        order_page.click_view_pdf_button()
        order_page = page.OrderPage(self.driver)
        time.sleep(2)
        order_page.orderbooksC()
        self.assertTrue(order_page.ordercheck())
        assert order_page.buy_now()

    def test_purchase005_2(self):
        order_page = page.MainPage(self.driver)
        time.sleep(5)
        order_page.click_view_pdf_button()
        order_page = page.OrderPage(self.driver)
        time.sleep(2)
        order_page.orderbooksPY()
        self.assertTrue(order_page.ordercheck())
        assert order_page.buy_now()

    def test_purchase005_3(self):
        order_page = page.MainPage(self.driver)
        time.sleep(5)
        order_page.click_view_pdf_button()
        order_page = page.OrderPage(self.driver)
        time.sleep(2)
        order_page.orderbookJS()
        self.assertTrue(order_page.ordercheck())
        assert order_page.buy_now()


    def test_purchase006_1(self):
        classlogin.loginrepeatable(self)
        TestCase.test_purchase005_1(self)
        assert True 
        #order_page = page.OrderPage(self.driver)

    def test_purchase006_2(self):
        classlogin.loginrepeatable(self)
        TestCase.test_purchase005_2(self)
        assert True 

    def test_purchase006_3(self):
        classlogin.loginrepeatable(self)
        TestCase.test_purchase005_3(self)
        assert True 

    def test_purchase007_1(self):
        classlogin.loginrepeatable2(self)
        TestCase.test_purchase005_1(self)
        

    def test_purchase007_2(self):
        classlogin.loginrepeatable2(self)
        TestCase.test_purchase005_2(self)
        

    def test_purchase007_3(self):
        classlogin.loginrepeatable2(self)   
        TestCase.test_purchase005_3(self)
        
    
    def test_purchase008_1(self):
        classlogin.loginrepeatable(self)
        TestCase.test_purchase005_1(self)
        time.sleep(2)
        order_page = page.OrderPage(self.driver)
        time.sleep(5)
        order_page.stripeinputemail = "email@email.com"
        time.sleep(3)
        order_page.stripeinputccnumber = "4242"
        order_page.stripeinputccnumber = "4242"
        order_page.stripeinputccnumber = "4242"
        order_page.stripeinputccnumber = "4242"
        time.sleep(3)
        order_page.stripeinputdate = "11"
        order_page.stripeinputdate = "23"
        time.sleep(3)
        order_page.stripeinputcvc = "111"
        time.sleep(3)
        order_page.paybutton() 
        assert order_page.stripe_payment_check()

    def test_purchase008_2(self):
        classlogin.loginrepeatable(self)
        TestCase.test_purchase005_2(self)
        time.sleep(2)
        order_page = page.OrderPage(self.driver)
        time.sleep(5)
        order_page.stripeinputemail = "email@email.com"
        time.sleep(3)
        order_page.stripeinputccnumber = "4242"
        order_page.stripeinputccnumber = "4242"
        order_page.stripeinputccnumber = "4242"
        order_page.stripeinputccnumber = "4242"
        time.sleep(3)
        order_page.stripeinputdate = "11"
        order_page.stripeinputdate = "23"
        time.sleep(3)
        order_page.stripeinputcvc = "111"
        time.sleep(3)
        order_page.paybutton() 
        assert order_page.stripe_payment_check()

    def test_purchase008_3(self):
        classlogin.loginrepeatable(self)
        TestCase.test_purchase005_3(self)
        time.sleep(2)
        order_page = page.OrderPage(self.driver)
        time.sleep(5)
        order_page.stripeinputemail = "email@email.com"
        time.sleep(3)
        order_page.stripeinputccnumber = "4242"
        order_page.stripeinputccnumber = "4242"
        order_page.stripeinputccnumber = "4242"
        order_page.stripeinputccnumber = "4242"
        time.sleep(3)
        order_page.stripeinputdate = "11"
        order_page.stripeinputdate = "23"
        time.sleep(3)
        order_page.stripeinputcvc = "111"
        time.sleep(3)
        order_page.paybutton() 
        assert order_page.stripe_payment_check()
