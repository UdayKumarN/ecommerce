import time
import pytest
import selenium.webdriver.remote.errorhandler
from selenium import webdriver
from Pageobjects.Loginpage import loginpage
from utilites.readproperties  import ReadConfig
from utilites.customlogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilites.emailutil import emailutil

class Test_001_login():

    baseUrl= "https://admin-demo.nopcommerce.com/"
    username= "admin@yourstore.com"
    password= "admin"
    logger = LogGen.loggen()  # calling static method by classname.methodname
    '''baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()'''

    def test_homepagetitle(self , setup):
        #self.driver=webdriver.chrome()
        self.logger.info("*********Test_001_login***********")
        self.logger.info("**********Verify Home Page**********")
        print("logger initiated")
        self.driver= setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        title=self.driver.title
        time.sleep(2)
        #self.assertEqual("Your store. Login", self.driver.title, "webpage title not matched") #assertEqual command works in unittest
        if title =="Your store. Login":
            assert True
            print("title verification ok:", title)
            #self.driver.save_screenshot(".\\screenshots\\test_homepagetitle.png")
            self.logger.info("**********Verify Home Page passed**********")
            self.driver.close()
        else:
            print("title verification failed:", title)
            self.driver.save_screenshot(".\\screenshots\\"+"test_homepage.png")
            self.logger.error("**********Verify Home Page failed & Screen shot captured**********")
            raise AssertionError(f"*****Verify Home Page failed & Screen shot captured******")
            self.driver.close()
            assert False

    def test_login(self, setup):
       #self.driver = webdriver.Chrome()
        self.logger.info("**********Login started**********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp=loginpage(self.driver)  #creating object for loginpage  class to access the methods
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login passed**********")
        #self.driver.close()
        print(self.driver.title)
        time.sleep(20)
        try:
            #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.lp.clickLogout())).click()
            self.lp.clickLogout()
            self.logger.info("**********Logout started**********")
            self.logger.info("**********Logout verified**********")
        except selenium.webdriver.remote.errorhandler.ErrorCode as err:
            self.logger.error(f"Error running logout failed {err}")
        finally:
            #self.driver.close()
            pass

        self.driver.close()
        self.logger.info("*******Email Sent******")
        time.sleep(3)
        emailutil.send_email(self)
        #self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title not matched")