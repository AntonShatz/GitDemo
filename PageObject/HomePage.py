from selenium.webdriver.common.by import By

from PageObject.ChekoutPage import ChekOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT,"Shop")
    name = (By.NAME, "name")
    email = (By.CSS_SELECTOR,"input[name='email']")
    gender = (By.XPATH, "//*[@id='exampleFormControlSelect1']")
    chekbox = (By.ID, "exampleCheck1")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        chekOutPage = ChekOutPage(self.driver)
        return chekOutPage
        #self.driver.find_element_by_link_text("Shop").click()

    def getname(self):
        return self.driver.find_element(*HomePage.name)
    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getchekbox(self):
        return self.driver.find_element(*HomePage.chekbox)
