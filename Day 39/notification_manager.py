from twilio.rest import Client
import confidential

class NotificationManager:
    def __init__(self) -> None:
        self.client = Client(confidential.TWILIO_SID, confidential.TWILIO_AUTH)
    
    def send_alert(self, fare, dest_city, start_airport, dest_airport, start_date, end_date):
        text = f"Low price alert! Only £{fare} to fly from London-{start_airport} to {dest_city}-{dest_airport} from {start_date} to {end_date}"

        message = self.client.messages.create(body=text, from_=confidential.TWILIO_FROM, to=confidential.TWILIO_TO)