from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import  neKey , productURL
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
    addtoCart       =xPathConfig('/html/body/div[6]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div[2]/button')
    prodInsure      =xPathConfig('/html/body/div[6]/div[2]/div[2]/div/div/div/div[3]/button[1]')
    viewCart        =xPathConfig('/html/body/div[6]/div[2]/div[2]/div/div/div[2]/div[2]/button[2]')
    covidMask       =xPathConfig('/html/body/div[14]/div/div[2]/div/div/div[2]/button')
    secureCheck     =xPathConfig('/html/body/div[4]/div/div[11]/div[2]/div[2]/div/a[2]')
    guestCheckout   =xPathConfig('/html/body/div[3]/div/div[2]/div/div/div[1]/form[2]/div[2]/div/button')

    # ---------------------- input variables--------------------------------------------

    inputFirstname  =TypeConfig('/html/body/div[3]/div/div[2]/div[1]/div/div/div[7]/ul/li/div/form/ul/li[1]/input', neKey['FN'])
    inputLastname   =TypeConfig('/html/body/div[3]/div/div[2]/div[1]/div/div/div[7]/ul/li/div/form/ul/li[2]/input',neKey['LN'])
    inputAddress    =TypeConfig('/html/body/div[3]/div/div[2]/div[1]/div/div/div[7]/ul/li/div/form/ul/li[5]/input',neKey['ADDR'])
    inputCity       =TypeConfig('/html/body/div[3]/div/div[2]/div[1]/div/div/div[7]/ul/li/div/form/ul/li[7]/ul/li[1]/div/input',neKey['CTY'])
    inputZipCode    =TypeConfig('/html/body/div[3]/div/div[2]/div[1]/div/div/div[7]/ul/li/div/form/ul/li[7]/ul/li[2]/div[2]/input',neKey['ZC'])
    inputPhoneNum   =TypeConfig('/html/body/div[3]/div/div[2]/div[1]/div/div/div[7]/ul/li/div/form/ul/li[7]/ul/li[3]/input',neKey['PN'])
    inputEmail      =TypeConfig('/html/body/div[3]/div/div[2]/div[1]/div/div/div[7]/ul/li/div/form/ul/li[7]/ul/li[4]/input',neKey['EMAIL'])

    # --------------------- contine to payment-------------------------------------------

    paymentContinue =xPathConfig('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[4]/div/div/a')
if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')

    driver.get(productURL['neURL'])
    preOrderScript()
    