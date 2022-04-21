from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    dellocation = (By.ID, "country")
    findindia = (By.LINK_TEXT, "India")
    Chekbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
    Submit = (By.CSS_SELECTOR, "input[type='submit']")
    GetFinalText = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")

    # self.driver.find_element_by_link_text("India").click()
    # self.driver.find_element_by_css_selector("label[for='checkbox2']").click()
    # self.driver.find_element_by_css_selector("input[type='submit']").click()
    # successtext = self.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
    def CountryText(self):
        return self.driver.find_element(*ConfirmPage.dellocation).send_keys("ind")
    def EndingMethod(self):
        self.driver.find_element(*ConfirmPage.findindia).click()
        self.driver.find_element(*ConfirmPage.Chekbox).click()
        self.driver.find_element(*ConfirmPage.Submit).click()
        successtext = self.driver.find_element(*ConfirmPage.GetFinalText).text
        return successtext












