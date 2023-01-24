from battery import Battery
from datetime import datetime

class NubbinBattery(Battery):
    def __init__(self, last_service_date) -> None:
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
    
    def battery_should_be_serviced(self):
        service_threshold = self.last_service_date.replace(self.last_service_date + 4)

        if service_threshold < datetime.today().date():
            return True
        else:
            return False