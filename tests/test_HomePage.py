import time

import pytest

from PageObject.HomePage import HomePage
from TestData.HomePagedata import HomePagedata
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    @pytest.fixture(params=HomePagedata.getTestData("TestCase2"))
    def getData(self,request):
        return request.param

    def test_fromSubmission(self,getData):

        homepage = HomePage(self.driver)
        log = self.getlogger()
        log.info("First Name" + getData["Name"])
        homepage.getname().send_keys(getData["Name"])
        homepage.getchekbox().click()
        homepage.getemail().send_keys(getData["Email"])
        self.selectOptionByText(homepage.getgender(),getData["Gender"])
        message = homepage.driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[1]/label").text
        print(message)
        assert "Name" in message
        print("This is Updated Line")
        self.driver.refresh()





