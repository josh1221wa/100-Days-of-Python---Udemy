import confidential
import requests
import datetime as dt

date_time = dt.datetime.now()
date = date_time.strftime("%d/%m/%Y")
time = date_time.strftime("%X")

nlp_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {"x-app-id": confidential.NUTRITIONIX_APP_ID,
           "x-app-key": confidential.NUTRITIONIX_API_KEY,
           "Content-Type": "application/json"}

data = input("What exercise did you do today?: ")

params = {"query": data,
          "gender": confidential.GENDER,
          "weight_kg": confidential.WEIGHT_KG,
          "height_cm": confidential.HEIGHT_CM,
          "age": confidential.AGE}

response = requests.post(url=nlp_url, json=params, headers=headers)
data = response.json()["exercises"]

for exercise in data:
    name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    params = {"workout": 
                {
                    "date": date,
                    "time": time,
                    "exercise": name,
                    "duration": duration,
                    "calories": calories
                }
              }

    response = requests.post(url="https://api.sheety.co/6cc91aa9cc22f4a9462769e389cc6b7b/myWorkouts/workouts", json=params, headers=confidential.SHEETY_AUTH)
    response.raise_for_status()