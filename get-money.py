from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import secrets

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-startup-window')
driver = webdriver.Chrome(
    executable_path="/Users/pbsoft/bot_bitmagnet/chromedriver", chrome_options=chrome_options)
ran = secrets.SystemRandom().randrange(0, 20, 5)
ran2 = secrets.SystemRandom().randrange(0, 50, 5)
url = "http://www.bitcoinearningshq.com/bitfaucet/login"
time.sleep(ran2)
driver.get(url)
search_form = driver.find_element_by_id("username")
search_form.send_keys("bitcoin_address")
search_form.click()
search_form.send_keys(Keys.ENTER)
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(ran)
search_form2 = driver.find_element_by_class_name("btn-success")
search_form2.click()
time.sleep(ran)
driver.execute_script("window.scrollTo(0, 900);")
time.sleep(ran)
search_form3 = driver.find_element_by_id("go_btn")
search_form3.click()
time.sleep(ran)
search_form4 = driver.find_element_by_class_name("btn-success")
search_form4.click()
time.sleep(ran)
driver.close()
