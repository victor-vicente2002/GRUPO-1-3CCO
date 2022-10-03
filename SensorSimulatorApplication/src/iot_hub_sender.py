from turbity.turbity_sensor import *
from temperature.temperature_sensor import *
from temperature.enums import *
from level.level_sensor import *
from ph.ph_sensor import *
from sensor_data import SensorData  

turbity_value = TurbitySensor.read_sensor_data()
