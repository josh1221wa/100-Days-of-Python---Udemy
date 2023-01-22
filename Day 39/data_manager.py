import requests
import confidential

class DataManager:
    def __init__(self) -> None:
        self.sheety_header = confidential.SHEETY_HEADER
        self.sheety_api_url = "https://api.sheety.co/6cc91aa9cc22f4a9462769e389cc6b7b/flightDeals/prices"
        
    def get_rows(self):
        response = requests.get(url=self.sheety_api_url, headers=self.sheety_header)
        data = response.json()
        return data["prices"]

    def edit_data(self, sheet_data):
        for row in sheet_data:
            edit_params = {"price":
                                {
                                    "iataCode" : row["iataCode"]
                                }
                            }
            request_url = f"{self.sheety_api_url}/{row['id']}"
            response = requests.put(url=request_url, headers=self.sheety_header, json=edit_params)
            response.raise_for_status()
