import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass():

    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,Locator,text):
        select = Select(Locator)
        select.select_by_visible_text(text)


    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler1 = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler1.setFormatter(formatter)
        logger.addHandler(filehandler1)  # filehandler object
        logger.setLevel(logging.DEBUG)  # setting the level from where i want to display
        return logger
