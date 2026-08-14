from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")


event_date = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# print([x.text for x in event_date])

event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# print([x.text for x in event_name])
events = {}
for n in range(len(event_date)):
    events[n] = {"time":event_date[n].text, "name":event_name[n].text}

print(events)
