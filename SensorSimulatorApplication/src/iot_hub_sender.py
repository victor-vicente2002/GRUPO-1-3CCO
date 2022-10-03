from turbity.turbity_sensor import *
from temperature.temperature_sensor import *
from temperature.enums import *
from level.level_sensor import *
from ph.ph_sensor import *
from dissolved_oxigen.kit_oem import *
from condutivity.condutivity_sensor import *
from sensor_data import SensorData  

turbity_value = TurbitySensor(Type.ADVANCED)
temperature_value = TemperatureSensor()
level_value = LevelSensor()
ph_value = PhSensor()
oxigem_value = KitOEM()
condutivity_value = CondutivitySensor()

for i in range(0, 100):
    print(f'Turbidez: {turbity_value.read_sensor_data()}\n' + 
        f'Temperatura: {temperature_value.read_temperature()}\n' +
        f'Nível da água: {level_value.read_sensor_data()}\n' + 
        f'Oxigenio da água: {oxigem_value.read()}\n' +
        f'Ph: {level_value.read_sensor_data()}\n' +
        f'Condutividade: {condutivity_value.read_sensor_data()}')