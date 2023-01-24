from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, current_mileage, last_service_mileage, warning_light_is_on=False):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_indicator_on = warning_light_is_on
    
    @abstractmethod
    def engine_should_be_serviced(self):
        pass

