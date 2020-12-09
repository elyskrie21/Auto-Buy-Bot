from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from config import keys
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def check_exists_by_css_selector(css_selector, driver):
    try:
        driver.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True

def checkout(k, driver):
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary'))).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#labeled-input-signEmail'))).send_keys(k['email'])
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#signInSubmit'))).click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#labeled-input-password"))).send_keys(k['password'])
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#signInSubmit'))).click()

    i = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.retype-security-code:nth-child(3) > input:nth-child(1)")))
    i.send_keys(keys['code'])
    i.send_keys(Keys.CONTROL, 'a')
    i.send_keys(Keys.BACKSPACE)
    i.send_keys(keys['code'])
   
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnCreditCard'))).click()

def NeweggOrder(k):
  driver = webdriver.Chrome(r'./chromedriver', options=chrome_options)
  driver.get('https://www.newegg.com/')
  time.sleep(5)
  driver.get(k['product_url'])
  time.sleep(2)
  
  if check_exists_by_css_selector('button.btn-wide', driver):
    while True:
      try:
        while True:
          try:
            WebDriverWait(driver, 1).until(lambda d: d.find_element_by_css_selector('button.btn-wide')).click()
            break
          except:
            print('no element')
            driver.get(k['product_url'])

        WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer > button:nth-child(2)'))).click()
        WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-undefined'))).click()
        break
      except:
        driver.get(k['produc_url'])
    checkout(k, driver)

  elif check_exists_by_css_selector('.atnPrimary', driver):
    while True:
      try:
        b = WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.atnPrimary')))
        if 'ADD TO CART' in b.text:
            b.click()
        checkout(k, driver)
        break
      except:
        driver.get(k['product_url'])
    

        
