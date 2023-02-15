class FlightData:
    
    def __init__(self, cheapest_fare, source_city_code, dest_city_code, start_date, end_date, stop_overs=0, via_city=""):
        self.fare = cheapest_fare
        self.start_city_code = source_city_code
        self.dest_city_code = dest_city_code
        self.start_date = start_date
        self.end_date = end_date        
        self.stop_overs = stop_overs
        self.via_city = via_city