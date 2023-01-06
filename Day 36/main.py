import requests
import confidential
import re
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def get_stock_data() -> tuple:
    params = {"function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": STOCK,
            "apikey": confidential.STOCK_API_KEY}

    response = requests.get(url="https://www.alphavantage.co/query", params=params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    yesterday_close_value : float = float(data[list(data.keys())[0]]["4. close"])
    day_before_close_value : float = float(data[list(data.keys())[1]]["4. close"])

    change = day_before_close_value-yesterday_close_value    
    change_percent= int((abs(change))/day_before_close_value * 100)
    if change < 0:
        return change_percent, -1
    else:
        return change_percent, 1


def get_news() -> tuple:
	params = {"q": "Tesla Inc",
				"apiKey": confidential.NEWS_API_KEY}
	response = requests.get(url="https://newsapi.org/v2/everything", params=params)
	response.raise_for_status()
	data = response.json()["articles"][0]
	title = data["title"]
	brief = data["description"]
	title = re.sub("<.*?>", "", title)      # To remove all HTML elements
	brief = re.sub("<.*?>", "", brief)
	return title, brief

def send_msg(change_percent, change_direction, title, brief):
    arrow = "🔺"
    if change_direction == -1:
        arrow = "🔻"
    msg_text =f"{STOCK}: {arrow}{change_percent}%\nHeadline: {title}\nBrief: {brief}"
    client = Client(confidential.TWILIO_SID, confidential.TWILIO_AUTH)
    message = client.messages.create(body=msg_text, from_=confidential.TWILIO_FROM, to=confidential.TWILIO_TO)
    # print(message.sid)

change_percent, change_direction = get_stock_data()
title, brief = get_news()
send_msg(change_percent, change_direction, title, brief)