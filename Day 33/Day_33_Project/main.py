import requests
from datetime import datetime
import smtplib
import confidential
from time import sleep

MY_LAT = 10.943585 # Your latitude
MY_LONG = 436.754175 # Your longitude

while True:
    sleep(60)   # Repeats every 60 seconds
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=confidential.MAIL_ID, password=confidential.PASSWORD)

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 5

    time_now = datetime.now()

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

    if (int(iss_latitude) in range(int(MY_LAT)-5, int(MY_LAT)+6)) and (int(iss_longitude) in range(int(MY_LONG)-5, int(MY_LONG)+5)) and (time_now.hour not in range(sunrise, sunset+1)):
        connection.sendmail(from_addr=confidential.MAIL_ID, to_addrs=confidential.MAIL_ID, msg="Subject:Look Up\n\nLook Up")

    connection.close()
    print("Next")