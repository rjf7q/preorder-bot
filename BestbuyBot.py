from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import bbKey , productURL
import time



def xPathConfig(xpath):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    return driver.find_element_by_xpath(xpath).click()

def TypeConfig(xpath,msg):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    return driver.find_element_by_xpath(xpath).send_keys(msg)

def preOrderScript():
    countrySelect       = xPathConfig('/html/body/div[2]/div/div/div/div[1]/div[2]/a[2]')
    addtoCart           = xPathConfig('/html/body/div[3]/main/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/button')
    time.sleep(.5)
    driver.get('https://www.bestbuy.com/cart')
    goToCheckout        =xPathConfig('/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button')
    guestLogin          =xPathConfig('/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button')   

    # ---------------------- input variables--------------------------------------------

    inputFirstName      = TypeConfig('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[1]/label/div/input',bbKey['FN'])
    inputLastName       = TypeConfig('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[2]/label/div/input',bbKey['LN'])
    inputAddress        = TypeConfig('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[3]/label/div[2]/div/div/input',bbKey['STRADD'])
    inputCity           = TypeConfig('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[1]/label/div/input',bbKey['CT'])
    inputZipCode        = TypeConfig('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[6]/div/div[1]/label/div/input',bbKey['ZC'])
    inputEmail          = TypeConfig('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[2]/label/div/input',bbKey['EMAIL'])
    inputPhoneNum       = TypeConfig('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input',bbKey['PN'])
    inputCC             = TypeConfig('/html/body/div[3]/div[2]/div/div/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div/section/div[1]/div/input',bbKey['CC'])



if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')

    driver.get(productURL['bbURL'])
    preOrderScript()
