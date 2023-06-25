# Price tracker on Amazon

GOAL_PRICE = 100

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import confidential

my_email = confidential.MAIL_ID
password = confidential.PASSWORD

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43", "Accept-Language": "en-US,en;q=0.9"}

response = requests.get(url=url, headers=headers)
content = response.text

soup = BeautifulSoup(content, "lxml")

price = int(soup.find(name="span", class_="a-price-whole").getText().rstrip(".")) + int(soup.find(name="span", class_="a-price-fraction").getText())/100
item_name = soup.find(name="span", id="productTitle").getText().strip()

if price < GOAL_PRICE:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    msg = f"{item_name} is now {price}\n{url}"
    connection.sendmail(from_addr=my_email, to_addrs=confidential.TO_MAIL, msg=f"Subject: Amazon Price Alert\n\n{str(msg)}")