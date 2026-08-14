
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)

#Create and configure webdriver
# driver = webdriver.Chrome(chrome_options)
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# get Count using CSS_Selector
count_views = driver.find_element(By.CSS_SELECTOR, value="#articlecount a ")
print(count_views.text)