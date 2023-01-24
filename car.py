#from abc import abstractmethod
from engine import Engine
from battery import Battery

class Car(Engine, Battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()

    def engine_should_be_serviced(self):
        return self.engine.engine_should_be_serviced()

    def battery_should_be_serviced(self):
        return self.battery.battery_should_be_serviced_serviced()
    
    
