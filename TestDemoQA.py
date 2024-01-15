from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from Homepage import Homepage
from ElementsPage import Elementspage


service = Service(executable_path="C:\Program Files (x86)\chromedriver-win64/chromedriver.exe")

def setup():
    options  = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    #options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches',['enable-logging'])
    options.add_argument('--log-level=3')

    return webdriver.Chrome(service=Service(), options = options)
    
driver = setup()

def test_navigate():
    
    driver.get("https://demoqa.com/")
    
    
def test_navigateElements():
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    homepage = Homepage(driver)
    homepage.clickElements()
    
def test_navigateForms():
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    homepage = Homepage(driver)
    homepage.clickForms()
    
def test_navigateAlertsFrameWindow():
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    homepage = Homepage(driver)
    homepage.clickAlertsFrameWindows()
    
def test_navigateWidgets():
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    homepage = Homepage(driver)
    homepage.clickWidgets()
    
def test_navigateInteractions():
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    homepage = Homepage(driver)
    homepage.clickInteractions()
    
def test_navigateBookStoreApp():
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    homepage = Homepage(driver)
    homepage.clickBookStoreApp()
    
def test_elementsClickTextBoxNavItem():
    driver.maximize_window()
    elements = Elementspage(driver)
    elements.clickTextBox()
    
def test_elementsFillOutForm():
    driver.maximize_window()
    elements = Elementspage(driver)
    elements.fillOutForm('James Watkins', 'james@test.com', '123 current address st. Test City, ST. 12345', '456 Perm Address Rd. Test Place, St. 45678') 
    
if __name__ == "__main__":
    #test_navigate()
    test_navigateElements()
    test_elementsClickTextBoxNavItem()
    test_elementsFillOutForm()
    #test_navigateForms()
    #test_navigateAlertsFrameWindow()
    #test_navigateWidgets()
    #test_navigateInteractions()
    #test_navigateBookStoreApp()

    
