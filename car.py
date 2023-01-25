#from abc import abstractmethod
# from engines.engine import Engine
# from batteries.battery import Battery
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
