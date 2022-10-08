from random import randrange, random

NULL_PROBABILITY = 0.1 # 80% de chance pelo range de 0.0 a 0.9

class PhSensor:
    def __init__(self):
        self.last_ph_value = randrange(6, 10)
        self.MIN_VALUE = 4
        self.MAX_VALUE = 12

    def get_ph_value(self):
        ph_variation = round(random(), 3) # pega as casas decimais depois da virgula
        normal_variation = random()
        ph_value = None
        if normal_variation > NULL_PROBABILITY:
            sum_or_sub = randrange(0, 2)
            ph_value = self.last_ph_value + ph_variation if sum_or_sub == 1 else self.last_ph_value - ph_variation
        else:
            ph_value = randrange(4, 12) + ph_variation
        self.last_ph_value = ph_value
        nullable_probability = random()
        return None if nullable_probability < 0.1 else round(ph_value, 2)