from batteries.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date) -> None:
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        service_threshold = self.last_service_date.replace(self.last_service_date + 2)

        if service_threshold < self.current_date:
            return True
        else:
            return False