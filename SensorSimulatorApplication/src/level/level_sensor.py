from contextlib import nullcontext
import random 

class LevelSensor:
    def __init__(self):
        self.MIN_VALUE = 0.0
        self.MAX_VALUE = 20.0

    def read_sensor_data(self) -> float:
        weights = 80, 19, 1
        choice = random.choices(range(3), weights=weights)[0]
        standardValue = random.uniform(0.0 , 20.0)

        if choice == 0:
            returnedData = round(standardValue, 2)
        elif choice == 1:
            peak = random.uniform(15.0, 20.0)
            returnedData = round(peak, 2)
        else:
            returnedData = "null"

        return returnedData

def mainTest():
    sensor = LevelSensor()
    for i in range(0, 100):
        print(sensor.read_sensor_data())

if __name__ == "__main__":
    mainTest()