from selenium.webdriver.common.by import By
from PageObject.ConfirmPage import ConfirmPage

class ChekOutPage:
    ProductTitle = (By.XPATH, "//div[@class='card h-100']")
    #self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    Producttext = (By.XPATH, "div/h4/a")
    #product.find_element_by_xpath("div/h4/a")
    CardButton = (By.XPATH, "div/button")
    #find_element_by_xpath("div/button")
    ChekoutButton1 = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    ChekoutButton2 = (By.CSS_SELECTOR, "button[class='btn btn-success']")


    def __init__(self, driver):
        self.driver = driver

    def getProductTitles(self):
        return self.driver.find_elements(*ChekOutPage.ProductTitle)

    def getProductText(self,product):
        return product.find_element(*ChekOutPage.Producttext)

    def getButton(self,product):
        return product.find_element(*ChekOutPage.CardButton)

    def ProceedChekout(self):
        self.driver.find_element(*ChekOutPage.ChekoutButton1).click()
        self.driver.find_element(*ChekOutPage.ChekoutButton2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage




