import os
import sys
from importlib import reload
import pytest
import time
from Pageobjects.Loginpage import loginpage
from Pageobjects.addcustomer import AddCustomer
from utilites.readproperties import ReadConfig
from utilites.customlogger import LogGen
from utilites.emailutil import emailutil
import string
import random

class Test_003_AddCustomer:
    '''baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword() '''
    baseUrl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Vendors")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("UdayN")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("12/12/1997")  # Format: D / MM / YYY
        self.addcust.setCompanyName("UK Company")
        self.addcust.setAdminContent("This is for testing.........")
        time.sleep(2)
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error(f"********* Add customer Test Failed Screenshot captured************")
            raise AssertionError (f"********* Add customer Test Failed Screenshot captured************")
            pass
        self.driver.close()
        time.sleep(2)
        self.logger.info("******* Ending Add customer test **********")
        #reload(emailutil)
        #emailutil.send_email(self)
        self.logger.info("**** Email sent ****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
