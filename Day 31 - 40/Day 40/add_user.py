# This file can be run if we want to add a user to our mailing list.

import confidential
import requests

sheety_header = confidential.SHEETY_HEADER
endpoint_url = "https://api.sheety.co/6cc91aa9cc22f4a9462769e389cc6b7b/flightDeals/users"

print("Welcome to Joshua's Flight Club!\nWe find the best deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
while True:
    email = input("What is your email?\n")
    email_check = input("Type your email again.\n")

    if email != email_check:
        print("The emails do not match. Please enter again.")
    else:
        break

data = {
            "user": 
                {
                    "firstName" : first_name,
                    "lastName" : last_name,
                    "email" : email
                }
        }

response = requests.post(url=endpoint_url, json=data, headers=sheety_header)
response.raise_for_status()
print("You're in the club!")