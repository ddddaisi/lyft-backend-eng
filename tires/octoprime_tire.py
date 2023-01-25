from tires.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_sensor_data) -> None:
        self.tire_sensor_data = tire_sensor_data
    
    def needs_service(self):
        # octoprime tire should be serviced when the sum of all values in the tire wear >= 3
        return sum(self.tire_sensor_data) >= 3.0