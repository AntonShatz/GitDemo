from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homePage = HomePage(self.driver)
        chekOutPage = homePage.shopItems()
        log.info("Getting all the Product Titles")
        products = chekOutPage.getProductTitles()# 4 diffrent names
        for product in products:
            proname = chekOutPage.getProductText(product).text
            log.info(proname)
            if proname == "Blackberry":
                chekOutPage.getButton(product).click()
        confirmPage = chekOutPage.ProceedChekout()
        confirmPage.CountryText()
        self.verifyLinkPresence("India")
        successtext = confirmPage.EndingMethod()
        assert "Success! Thank you!" in successtext
        log.info("Text recived was matching")
        print(successtext)
