from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        palindrome_engine = SternmanEngine(current_mileage, last_service_mileage)
        palindrome_battery = SpindlerBattery(last_service_date)
        
        super.__init__(palindrome_engine, palindrome_battery)

    def needs_service(self):
        return super().needs_service()

