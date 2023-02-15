#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
import confidential
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_rows()

for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_city_code(row['city'])

data_manager.edit_data(sheet_data)

for row in sheet_data:
    cheapest_fare, source_city_code, dest_city_code, start_date, end_date = flight_search.get_flight(row['iataCode'])
    flight = FlightData(cheapest_fare, source_city_code, dest_city_code, start_date, end_date)
    if flight.fare < row['lowestPrice']:
        notification_manager.send_alert(flight, "London", row['city'])
