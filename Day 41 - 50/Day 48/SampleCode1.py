from selenium import webdriver
from selenium.webdriver.common.by import By # Used to search elements
from selenium.webdriver.chrome.options import Options   # Used to make options for the opening window

options = Options()
options.add_argument('--headless')  # Option to run without window
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)  # Wont open the window
# driver = webdriver.Chrome() # Will open the window

driver.get("https://www.python.org/")
# print(driver.title) # Prints the title of the given page
driver.implicitly_wait(5)   # Is a waiting time in seconds for page to load, not always useful but can be used in certain cases

introduction = driver.find_element(by=By.CLASS_NAME, value="introduction")
# print(introduction.get_attribute('textContent'))   # Gets the text content

search_box = driver.find_element(by=By.ID, value="id-search-field")
# print(search_box)

logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
# print(logo.size)  # Prints the size of the logo

docs = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a") # Selects the element using a CSS selector
# print(docs.text)

"""If we have no way to locate an element in a site using class, names or even css selector we use XPath. The XPath can be copied using the inspect menu by right clicking element -> Copy -> Copy XPath"""

xpath_element = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(xpath_element.text)

driver.quit()