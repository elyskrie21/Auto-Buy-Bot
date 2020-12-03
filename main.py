from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from config import keys
import time 

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def BestBuyOrder(k):
  driver = webdriver.Chrome(r".\chromedriver", options=chrome_options)
  driver.get(k['product_url'])
  
  while True:
    try:
      WebDriverWait(driver, 1).until(lambda d: d.find_element_by_css_selector('button.btn-primary:nth-child(1)')).click()
      break
    except:
      print('no element')
      driver.refresh()
  

  b = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a')))
  b.click()

  while True:
    try:
      driver.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[2]/fieldset/div[2]/div[1]').click()
      break
    except:
      print('not found')


  b = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button'))).click()

  i = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fld-e")))
  i.send_keys(k['email'])

  i = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fld-p1")))
  i.send_keys(k['password'])

  b = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button')))
  b.click()

  while True:
    try:
      driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.firstName"]').send_keys(k['first']) 
      driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.lastName"]').send_keys(k['last'])
      driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.city"]').send_keys(k['city'])
      driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.zipcode"]').send_keys(k['zip'])
      driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.street"]').send_keys(k['address'])
      driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.state"]/option[21]').click()
      driver.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/label[2]/div').click()
      driver.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button').click()
      break
    except:
      print('not ready')

  while True: 
    try:
      driver.find_element_by_xpath('//*[@id="payment.billingAddress.firstName"]').send_keys(k['first'])
      driver.find_element_by_xpath('//*[@id="payment.billingAddress.lastName"]').send_keys(k['last'])
      driver.find_element_by_xpath('//*[@id="payment.billingAddress.city"]').send_keys(k['city'])
      driver.find_element_by_xpath('//*[@id="payment.billingAddress.zipcode"]').send_keys(k['zip'])
      driver.find_element_by_xpath('//*[@id="payment.billingAddress.street"]').send_keys(k['address'])
      driver.find_element_by_xpath('//*[@id="payment.billingAddress.state"]/option[21]').click()

      driver.find_element_by_xpath('//*[@id="optimized-cc-card-number"]').send_keys(k['card'])
      driver.find_element_by_xpath('//*[@id="credit-card-expiration-month"]/div/div/select/option[8]').click()
      driver.find_element_by_xpath('//*[@id="credit-card-expiration-year"]/div/div/select/option[3]').click()
      driver.find_element_by_xpath('//*[@id="payment.billingAddress.lastName"]').send_keys(k['last'])
      driver.find_element_by_xpath('//*[@id="credit-card-cvv"]').send_keys(k['code'])
      driver.find_element_by_xpath('//*[@id="save-card-checkbox"]').click()
      break
    except:
      print('not ready')

  driver.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[4]/button').click()

def NeweggOrder(k):
  driver = webdriver.Chrome(r'./chromedriver', options=chrome_options)
  driver.get('https://www.newegg.com/')
  time.sleep(2)
  driver.get(k['product_url'])

  while True:
    try:
      time.sleep(.5)
      WebDriverWait(driver, 1).until(lambda d: d.find_element_by_css_selector('button.btn-wide')).click()
      break
    except:
      print('no element')
      driver.refresh()

  b = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer > button:nth-child(2)')))
  b.click()

  b = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-undefined')))
  b.click()

  b = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary')))
  b.click()

  i = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#labeled-input-signEmail")))
  i.send_keys(k['email'])

  b = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#signInSubmit')))
  b.click()

  i = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#labeled-input-password")))
  i.send_keys(k['password'])

  b = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#signInSubmit')))
  b.click()

  i = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.retype-security-code:nth-child(3) > input:nth-child(1)")))
  i.send_keys(k['code'])

  b = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnCreditCard')))
  b.click()


def main():
  print('Welcome to the Auto Buy Bot!\nTo get started, enter the product url')
  url = input('Product url: ')
  keys['product_url'] = url
  keys['email'] = input('What is your email: ')
  keys['password'] = input('What is your password: ') 
  
  store = input('Enter N to shop on Newegg. Enter B to shop on Bestbuy: ')

  if store == 'N':
    NeweggOrder(keys)
  if store == 'B':
    BestBuyOrder(keys)

main()
