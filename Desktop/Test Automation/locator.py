from selenium.webdriver.common.by import By


class HomePageLocators(object):

    SEARCH_TEXTBOX = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    SEARCH_BTN = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    LUCKY_BTN = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]")
    FIRST_SUGGESTION = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/div/ul/li[1]/div/div[2]/div[1]/span")

class ResultPageLocators(object):
    FIRST_RESULT = (By.XPATH, "//*[@id=\"rso\"]/div[1]/div/div/div/div/div/div/div[1]/a/h3")
    CALCULATOR = (By.XPATH, "//*[@id=\"rso\"]/div[1]")
    CALCULATOR_RESULT = (By.ID, "cwos")  
    CONVERTER_RESULT = (By.CLASS_NAME, "DFlfde SwHCTb")