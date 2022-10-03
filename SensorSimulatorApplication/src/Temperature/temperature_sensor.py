import random

class TemperatureSensor:
    def read_temperature(self):
        temperature = round(random.uniform(21, 31), 2)
        null = round(random.uniform(0, 10)) == 9
        return None if null else temperature