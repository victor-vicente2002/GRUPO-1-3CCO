import random

random.seed(111)

class KitOEM:

  #range 0.01 - 100 mg/L or 0.1 - 400% saturation
  max_range = 100
  min_range = 0.01

  #round 0.05 above or below the real value mg/L
  accuracy  = 0.05

  #max_rate(read per second)
  max_rate = 1

  #the sensor has 95% chance of reading a number value and 5% chance of reading None
  read_null_chances = 95, 5

  def __init__(self):
    pass

  def read(self) -> float:

    choice = random.choices(range(2), weights=self.read_null_chances)[0]
    is_null_value = bool(choice)

    if is_null_value: return None

    actual_value = random.uniform(self.min_range, self.max_range)

    accuracy = random.uniform(-self.accuracy, self.accuracy)

    accured_value = actual_value + accuracy

    return round(accured_value, 2)
