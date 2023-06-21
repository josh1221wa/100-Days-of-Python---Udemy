from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--log-level=3")   # Disable extra console prompts

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_no = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# article_no.click()  # Clicks the link

# We can find a link with specific text using the given method
encyclopedia = driver.find_element(by=By.LINK_TEXT, value="encyclopedia")
# encyclopedia.click()

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")  # This enters the text in the input bar
search.send_keys(Keys.ENTER)    # Hits the enter key

driver.quit()