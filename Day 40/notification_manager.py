from twilio.rest import Client
import confidential
from flight_data import FlightData

class NotificationManager:
    def __init__(self) -> None:
        self.client = Client(confidential.TWILIO_SID, confidential.TWILIO_AUTH)
    
    def send_alert(self, flight:FlightData, start_city, dest_city):
        text = f"Low price alert! Only £{flight.fare} to fly from {start_city}-{flight.start_city_code} to {dest_city}-{flight.dest_city_code} from {flight.start_date} to {flight.end_date}"
        if flight.stop_overs == 1:
            text += f"\n\nFlight has 1 stopover, via {flight.via_city}"

        message = self.client.messages.create(body=text, from_=confidential.TWILIO_FROM, to=confidential.TWILIO_TO)