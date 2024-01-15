from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 





class Homepage:
    def __init__(self, driver):
        self.driver = driver
        
        #Elements Button
        self.elements = "//*[@class='card-body']//h5[text()='Elements']"
        
        #Forms button
        self.forms = "//*[@class='card-body']//h5[text()='Forms']"
        
        #Alerts Frames and Windows Button
        self.alertsFrameWindows = "//*[@class='card-body']//h5[text()='Alerts, Frame & Windows']"
        
        #Widgets button
        self.widgets = "//*[@class='card-body']//h5[text()='Widgets']"
        
        #Interactions button
        self.Interactions = "//*[@class='card-body']//h5[text()='Interactions']"
        
        #Bookstore Application button
        self.bookStore = "//*[@class='card-body']//h5[text()='Book Store Application']"
        
        #Alerts, Frame & Windows button
        self.alertsFrameWindows = "//*[@class='card-body']//h5[text()='Alerts, Frame & Windows']"
        
        #Widgets button
        self.widgets = "//*[@class='card-body']//h5[text()='Widgets']"
        
        #Interactions button
        self.interactions = "//*[@class='card-body']//h5[text()='Interactions']"
        
        #Book Store App button
        self.bookStoreApp = "//*[@class='card-body']//h5[text()='Book Store Application']"
        
        #Left Nav Bar
        self.navBar = "//*[contains(@class, 'left-menu-nav-bar')]"
        
        #Elements Landing Page Ad
        self.elementsHeader = "//*[contains(@class, 'pattern-backgound playgound-header')]"
        
        #wait
        self.wait = WebDriverWait(self.driver, 20)
        

        
    def clickElements(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.elements)))
        self.driver.find_element(By.XPATH, self.elements).click()
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.elementsHeader)))
        
            
    def clickForms(self):
        self.driver.find_element(By.XPATH, self.forms).click()
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.elementsHeader)))
        
    def clickAlertsFrameWindows(self):
        self.driver.find_element(By.XPATH, self.alertsFrameWindows).click()
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.elementsHeader)))
        
    def clickWidgets(self):
        self.driver.find_element(By.XPATH, self.widgets).click()
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.elementsHeader)))
        
    def clickInteractions(self):
        self.driver.find_element(By.XPATH, self.interactions).click()
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.elementsHeader)))
        
    def clickBookStoreApp(self):
        
        bookStoreAppBtn = self.driver.find_element(By.XPATH, self.bookStoreApp)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", bookStoreAppBtn);
        bookStoreAppBtn.click()
    
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.elementsHeader)))