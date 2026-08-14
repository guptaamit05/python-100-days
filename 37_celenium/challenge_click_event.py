from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# click on a link and open the page...
# click_link = driver.find_element(By.LINK_TEXT, "anyone can edit")
# click_link.click()


# click the icon of search box..
search_icon_click_first = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
search_icon_click_first.click()

# Type something on a input box
search_box = driver.find_element(By.NAME, value="search")

# Typed the text in search box and press the enter button.
search_box.send_keys("Python", Keys.ENTER)


