from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/doc/")

# get text by class name, 
title = driver.find_element(By.CLASS_NAME, value="call-to-action")
# print(f"Price: {title.text} and Product name: {download_buttons.text}")


# get button text
download_buttons = driver.find_element(By.CLASS_NAME, value="download-buttons")
# print(download_buttons.text)


# find all the h2 on webpage..
find_all_element_h2 = driver.find_elements(By.TAG_NAME, value="h2")
# for h2_tags in find_all_element_h2:
    # print(h2_tags.text)


a_href = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# get the link href text
print(a_href.get_attribute("href"))


# driver.close()
