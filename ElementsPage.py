from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Elementspage:
    def __init__(self, driver):
        self.driver = driver
        
        #Element menu options:
        self.text = "//li//*[text()='Text Box']"
        
        self.checkBox = "//li//*[text()='Check Box']"
        
        self.radioButton = "//li//*[text()='Radio Button']"
        
        self.webTables = "//li//*[text()='Web Tables']"
        
        self.buttons = "//li//*[text()='Buttons']"
        
        self.links = "//li//*[text()='Links']"
        
        self.brokenLinksImages = "//li//*[text()='Broken Links - Images']"
        
        self.uploadAndDownload = "//li//*[text()='Upload and Download']"
        
        self.dynamicProperties = "//li//*[text()='Dynamic Properties']"
        
        #Textbox elements
        
        self.userForm = "[id = 'userForm']"
        
        self.fullNamelocator = "[id = 'userName']"
        
        self.emailLocator = "[id = 'userEmail']"
        
        self.currentAddressLocator = "[id = 'currentAddress']"
        
        self.permanentAddressLocator = "[id = 'permanentAddress']"
        
        self.submitBtn = "[id = 'submit']"
        
        #wait
        self.wait = WebDriverWait(self.driver, 20)
        
    def clickTextBox(self):
        self.driver.find_element(By.XPATH, self.text).click()
        element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.userForm)))
        
    def fillOutForm(self, fullName, email, currentAddress, permAddress):
        self.driver.find_element(By.CSS_SELECTOR, self.fullNamelocator).send_keys(fullName)
        self.driver.find_element(By.CSS_SELECTOR, self.emailLocator).send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, self.currentAddressLocator).send_keys(currentAddress)
        self.driver.find_element(By.CSS_SELECTOR, self.permanentAddressLocator).send_keys(permAddress)
        
        self.driver.find_element(By.CSS_SELECTOR, self.submitBtn).click()
        
        
    