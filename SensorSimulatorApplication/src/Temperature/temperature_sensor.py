import random

class TemperatureSensor:
    def __init__(self):
        self.MIN_VALUE = 21
        self.MAX_VALUE = 31

    def read_temperature(self) -> float:
        temperature = round(random.uniform(self.MIN_VALUE, self.MAX_VALUE), 2)
        null = round(random.uniform(0, 10)) == 9
        return None if null else temperature

