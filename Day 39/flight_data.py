from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

class FlightData:
    def __init__(self, flight_search:FlightSearch, data_manager:DataManager, notification_manager:NotificationManager):
        self.flight_search = flight_search
        self.data_manager = data_manager
        self.notification_manager = notification_manager
        self.data = self.data_manager.get_rows()
        self.find_city_codes()

    def find_city_codes(self):
        for row in self.data["prices"]:
            if row["iataCode"] == '':
                city_code = self.flight_search.get_city_code(row["city"])
                row["iataCode"] = city_code
        # print(self.data)
        self.data_manager.edit_rows(self.data)

    def search_cheap_flights(self):
        for row in self.data["prices"]:
            cheap_flight = self.flight_search.get_cheapest_flight(row["iataCode"])
            if cheap_flight[0] < row["lowestPrice"]:
                self.notification_manager.send_alert(cheap_flight[0], row["city"], cheap_flight[1], cheap_flight[2], cheap_flight[3], cheap_flight[4])