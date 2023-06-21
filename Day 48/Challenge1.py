# Scrape data from Python.org to make a dictionary of events

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")

count = 0

events = {}

while True:
    try:
        time_element = str(driver.find_element(by=By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{count + 1}]/time').get_attribute("datetime"))
        time = time_element.split("T")[0]

        event_name = driver.find_element(by=By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{count + 1}]/a').text
        
        event_dict = {"time": time, "name": event_name}
        events[count] = event_dict

        count += 1
    
    except NoSuchElementException:
        break

print(events)

