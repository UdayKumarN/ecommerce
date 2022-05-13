from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class loginpage:
    #locators of all elemnets
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    button_logout_linktext="Logout"

    def __init__(self, driver):      #python constructor,"__init__" is a reseved method in python classes. It is known as a constructor
        self.driver= driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    def clickLogout(self):
        #self.driver.find_element_by_link_text(self.button_logout_linktext).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT,"Logout"))).click()