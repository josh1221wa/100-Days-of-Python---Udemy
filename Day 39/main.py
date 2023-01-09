from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
flight_data = FlightData(flight_search, data_manager, notification_manager)

flight_data.search_cheap_flights()