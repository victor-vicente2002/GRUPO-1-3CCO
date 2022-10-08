import random
from enum import Enum

class TurbitySensor:
    def __init__(self, type):
        self.MIN_VALUE = 0.9
        self.standardValue = range(10, 150)
        if type == Type.BASIC.name:
            self.range = range(0, 500)
            self.MAX_VALUE = 500
        else: 
            self.range = range(0, 1000)
            self.MAX_VALUE = 1000
    
    def read_sensor_data(self) -> float:
        weights = 80, 15, 5
        choice = random.choices(range(3), weights=weights)[0]
        standard_value = random.uniform(self.standardValue.start, self.standardValue.stop)

        if choice == 0:
            printed_value = round(standard_value, 2)
        elif choice == 1:
            peak = random.uniform(self.range.start, self.range.stop)
            printed_value = round(peak, 2)
        else:
            printed_value = "null"

        return printed_value
 
class Type(Enum):
    BASIC = "BASIC"
    ADVANCED = "ADVANCED"

def mainTest():
    sensor = TurbitySensor(Type.ADVANCED.name)
    for i in range(0, 100):
        print(sensor.read_sensor_data())

if __name__ == "__main__":
    mainTest()