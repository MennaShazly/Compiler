import string
from turtle import home
import unittest

from numpy import result_type
from sqlalchemy import false, true
import page
from selenium import webdriver

class Tests(unittest.TestCase):

    def setUp(self):
        # lang_de = webdriver.ChromeOptions()
        # lang_de.add_argument("--lang=en")
        # self.driver = webdriver.Chrome(chrome_options=lang_de)
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(50)
        

    def test_search(self): 
        home_page = page.HomePage(self.driver)
        home_page.enter_data("instabug")
        home_page.click_search()
        self.assertFalse(home_page.is_current_url("https://www.google.com/"), "TC_1 Failed")

    def test_empty_search(self):
        home_page = page.HomePage(self.driver)
        home_page.click_search()
        self.assertTrue(home_page.is_current_url("https://www.google.com/"), "TC_2 Failed")

   
    def test_lucky_btn(self):
        home_page = page.HomePage(self.driver)
        home_page.click_feeling_lucky()
        self.assertTrue(home_page.is_current_url("https://www.google.com/doodles"), "TC_3 Failed")

    def test_first_result_search(self):
        home_page = page.HomePage(self.driver)
        result_page = page.ResultsPage(self.driver)
        home_page.enter_data("instabug")
        home_page.press_enter()
        url = result_page.click_first_result()
        self.assertTrue(home_page.is_current_url("https://www.instabug.com/"), "TC_8 Failed")
        
    # Not working properly :(
    def test_calculator(self):
        home_page = page.HomePage(self.driver) 
        home_page.enter_data("50/5")
        home_page.press_enter()
        self.assertEqual(page.ResultsPage.calculator_result, 10)

    def test_converster(self):
        home_page = page.HomePage(self.driver) 
        result_page = page.ResultsPage(self.driver)
        home_page.enter_data("1 egp in eur")
        home_page.press_enter()
        flag = false
        if (result_page.converter_result == 0.052):
            flag = true 
        self.assertTrue(flag, "TC_11 Failed")

    def test_auto_complete(self):
        home_page = page.HomePage(self.driver)
        result_page = page.ResultsPage(self.driver)
        home_page.enter_data("fac")
        home_page.click_search()
        flag = false
        if (home_page.get_first_suggestion == "facebook"):
            flag = true
        self.assertTrue(flag and result_page.find_in_results("facebook") , "TC_12 Failed")

    def test_incorrect_keyword(self):
        home_page = page.HomePage(self.driver)
        result_page = page.ResultsPage(self.driver)
        home_page.enter_data("uhhkjjkleh")
        home_page.click_search()
        self.assertTrue(result_page.is_result_found("لم ينجح بحثك عن"), "TC_13 Failed")

    def test_correction(self):
        home_page = page.HomePage(self.driver)
        result_page = page.ResultsPage(self.driver)
        home_page.enter_data("congratlasion")
        home_page.click_search()
        self.assertTrue(result_page.find_in_results("congratulations"), "TC_15 Failed")

    def test_search_langs(self): 
        home_page = page.HomePage(self.driver)
        result_page = page.ResultsPage(self.driver)
        home_page.enter_data("如何测试一个网站")
        home_page.click_search()
        self.assertTrue(result_page.find_in_results("测试"), "TC_17 Failed")

    # Not working properly :(
    def test_search_special_chars(self): 
        home_page = page.HomePage(self.driver)
        result_page = page.ResultsPage(self.driver)
        home_page.enter_data("?.*&^%$#])")
        home_page.click_search()
        self.assertTrue(result_page.is_result_found("لم ينجح بحثك عن"), "TC_19 Failed")

    def test_paste(self):
        home_page = page.HomePage(self.driver)
        result_page = page.ResultsPage(self.driver)
        home_page.paste_keys("instabug careers")
        home_page.click_search()
        self.assertTrue(result_page.find_in_results("instabug careers"), "TC_20 Failed")

    #Not working properly :(
    def test_large_paragraph(self): 
        home_page = page.HomePage(self.driver)
        result_page = page.ResultsPage(self.driver)
        home_page.enter_data("""
        The trees, therefore, must be such old and primitive techniques that they thought nothing of them, deeming them so inconsequential that even savages like us would know of them and not be suspicious. At that, they probably didn't have too much time after they detected us orbiting and intending to land. And if that were true, there could be only one place where their civilization was hidden.
        Eating raw fish didn't sound like a good idea. "It's a delicacy in Japan," didn't seem to make it any more appetizing. Raw fish is raw fish, delicacy or not.
        """)
        home_page.click_search()
        self.assertTrue(result_page.is_result_found("نحصر البحث في"), "TC_21 Failed")

    def test_search_title(self):
        home_page = page.HomePage(self.driver)
        test_data = "instabug"
        home_page.enter_data(test_data)
        home_page.click_search()
        self.assertTrue(home_page.is_title_matches(test_data), "TC_23 Failed")


    # driver.forward()
# driver.back()
#        self.driver.implicitly_wait(2000)


       

    def tearDown(self):
        self.driver.close()

    
if __name__ == "__main__":
    unittest.main()
