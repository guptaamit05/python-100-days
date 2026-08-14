from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")


fName = driver.find_element(By.NAME, value='fName')
fName.send_keys("Satish")
lName = driver.find_element(By.NAME, value='lName')
lName.send_keys("Bhawasar")
email = driver.find_element(By.NAME, value='email')
email.send_keys("satish.bh@ggm.com")

enter_btn  = driver.find_element(By.TAG_NAME, value='button')
enter_btn.click()