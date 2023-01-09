import os
import confidential
import requests
import json
import datetime

class FlightSearch:
    def __init__(self) -> None:
        self.city_codes_url = "https://api.tequila.kiwi.com/locations/query"
        self.flight_search_headers = {"apikey": confidential.FLIGHT_SEARCH_API}
        self.flight_search_url = "https://api.tequila.kiwi.com/v2/search"
        self.start_code = "LON"


    def get_city_code(self, city_name: str):
        params={"term": city_name,
                "limit": 1,
                "location-types": "city"}

        response = requests.get(url=self.city_codes_url, params=params, headers=self.flight_search_headers)
        response.raise_for_status()
        city_code = response.json()["locations"][0]["code"]
        return city_code
    

    def get_cheapest_flight(self, dest_code):
        start_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        end_date = (datetime.date.today() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")

        params = {"fly_from": self.start_code,
                  "fly_to": dest_code,
                  "date_from": start_date,
                  "date_to": end_date,
                  "nights_in_dst_from": 7,
                  "nights_in_dst_to": 28,
                  "flight_type": "round",
                  "curr": "GBP",
                  "asc": 1,
                  "limit": 200
                }

        response = requests.get(url=self.flight_search_url, params=params, headers=self.flight_search_headers)
        response.raise_for_status()
        cheapest_fare = response.json()["data"][0]["price"]
        flight_from = response.json()["data"][0]["flyFrom"]
        flight_to = response.json()["data"][0]["flyTo"]
        date_from = response.json()["data"][0]["route"][0]["local_departure"][0:11]
        date_to = response.json()["data"][0]["route"][1]["local_arrival"][0:11]
        return cheapest_fare, flight_from, flight_to, date_from, date_to