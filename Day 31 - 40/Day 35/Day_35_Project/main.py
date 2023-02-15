import requests
import confidential
from twilio.rest import Client

openweather_api_key = confidential.OPENWEATHER_KEY
twilio_sid = confidential.TWILIO_SID
twilio_auth_token = confidential.TWILIO_AUTH
client = Client(twilio_sid, twilio_auth_token)

parameters = {"lat" : 10.057906,
              "lon" : 76.346359,
              "appid" : openweather_api_key}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()

if data["weather"][0]["id"] > 700:
    message = client.messages \
                    .create(
                        body="It's going to rain. Bring an ☔",
                        from_=confidential.TWILIO_FROM,
                        to=confidential.TWILIO_TO
                    )