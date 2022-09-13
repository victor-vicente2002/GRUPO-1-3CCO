import random
from enum import Enum

class TurbityPlus:
    def __init__(self, type, latitude, longitude):
        self.id = 0
        self.latitude = latitude
        self.longitude = longitude
        self.standardValue = range(10, 150)
        if type == Type.BASIC.name:
            self.range = range(0, 500)
        else: 
            self.range = range(0, 1000)
    
    def readSensorData(self):
        weights = 80, 15, 5
        choice = random.choices(range(3), weights=weights)[0]
        standardValue = random.uniform(self.standardValue.start, self.standardValue.stop)

        if choice == 0:
            printedValue = round(standardValue, 5)
        elif choice == 1:
            peak = random.uniform(self.range.start, self.range.stop)
            printedValue = round(peak, 5)
        else:
            printedValue = "null"

        sendorData = SensorData(
            self.id, 
            printedValue, 
            self.longitude, 
            self.latitude, 
            "Turbity_Plus"
        )
        self.id = self.id + 1
        # print(sendorData.__str__())
        return sendorData

class SensorData:
    def __init__(self, registerId, value, longitude, latitude, deviceName):
        self.registerId = registerId
        self.value = value
        self.longitude = longitude
        self.latitude = latitude
        self.deviceName = deviceName

    def __str__(self):
        return f'registerId: {self.registerId}, value: {self.value}, longitude: {self.longitude}, latitude: {self.latitude}, deviceName: {self.deviceName}'
 
class Type(Enum):
    BASIC = "BASIC"
    ADVANCED = "ADVANCED"

def mainTest():
    sensor = TurbityPlus(Type.ADVANCED.name, "-30420348203442", "130981209239128")
    for i in range(0, 100):
        sensor.readSensorData()

if __name__ == "__main__":
    mainTest()