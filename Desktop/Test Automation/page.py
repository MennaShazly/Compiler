import os
from xml.dom.minidom import Element
from matplotlib.style import available
import arabic_reshaper
from locator import *
from selenium.webdriver.support.ui import Select
from element import BasePageElement
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    def click_search(self):
        element = self.driver.find_element(*HomePageLocators.SEARCH_BTN)
        element.click()

    def click_feeling_lucky(self):
        element = self.driver.find_element(*HomePageLocators.LUCKY_BTN)
        element.click()

    def enter_data(self, data):
        element = self.driver.find_element(*HomePageLocators.SEARCH_TEXTBOX)
        element.send_keys(data)
    
    def press_enter(self):
        element = self.driver.find_element(*HomePageLocators.SEARCH_TEXTBOX)
        element.send_keys(Keys.ENTER)

    def is_title_matches(self, data):
        return data in self.driver.title

    def is_current_url(self, data):
        return self.driver.current_url == data
    
    def get_first_suggestion(self):
        return self.driver.find_element(*ResultPageLocators.FIRST_SUGGESTION).text

    def paste_keys(self, text):
        os.system("echo %s| clip" % text.strip())
        el = self.driver.find_element(*HomePageLocators.SEARCH_TEXTBOX)
        el.send_keys(Keys.CONTROL, 'v')


class ResultsPage(BasePage):

    def is_result_found(self, text_to_be_reshaped):
        reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
        rev_text = reshaped_text[::-1]  
        return rev_text in self.driver.page_source

    def find_in_results(self, data):
        return data in self.driver.page_source

    def click_first_result(self):
        element = self.driver.find_element(*ResultPageLocators.FIRST_RESULT)
        element.click()

    def calculator_result(self):
        return self.driver.find_element(*ResultPageLocators.CALCULATOR_RESULT).text

    def converter_result(self):
        return self.driver.find_element(*ResultPageLocators.CONVERTER_RESULT).text
   


