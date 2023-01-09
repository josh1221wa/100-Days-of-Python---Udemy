import confidential
import requests

class DataManager:
    def __init__(self) -> None:
        self.sheety_header = {"Authorization": confidential.SHEETY_BEARER_TOKEN}
        self.sheety_api_url = "https://api.sheety.co/6cc91aa9cc22f4a9462769e389cc6b7b/flightDeals/prices"
        self.get_rows()
    
    def get_rows(self):
        response = requests.get(url=self.sheety_api_url, headers=self.sheety_header)
        data = response.json()
        return data
    
    def edit_rows(self, data):
        for row in data["prices"]:
            params = {
                        "price": 
                            {
                                "city": row["city"],
                                "iataCode": row["iataCode"], 
                                "lowestPrice": row["lowestPrice"]
                            }
                      }
            request_url = f"{self.sheety_api_url}/{row['id']}"

            response = requests.put(url=request_url, headers=self.sheety_header, json=params)
            response.raise_for_status()