from tires.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_sensor_data) -> None:
        self.tire_sensor_data = tire_sensor_data
    
    def needs_service(self):
        # carrigantires should be serviced when one or more of the values in the tire wear >= 0.9
        return any(map(lambda current_tire: current_tire >=0.9, self.tire_sensor_data))