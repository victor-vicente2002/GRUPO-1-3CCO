from turbity.turbity_sensor import TurbitySensor, Type
from temperature.temperature_sensor import TemperatureSensor
from level.level_sensor import LevelSensor
from ph.ph_sensor import PhSensor
from dissolved_oxigen.kit_oem import KitOEM
from condutivity.condutivity_sensor import CondutivitySensor
from iot_hub_sender import iothub_messaging_sample_run

def main():
    temperature_sensor = TemperatureSensor()
    turbity_sensor = TurbitySensor(Type.ADVANCED.name)
    ph_sensor = PhSensor()
    level_sensor = LevelSensor()
    oxigem_sensor = KitOEM()
    condutivity_sensor = CondutivitySensor()

    while(True):
        temperature_registry = temperature_sensor.read_temperature()
        turbity_registry = turbity_sensor.read_sensor_data()
        ph_registry = ph_sensor.get_ph_value()
        oxigem_registry = oxigem_sensor.read()
        condutivity_registry = condutivity_sensor.read_sensor_data()

        variation = generate_variation(temperature_registry, temperature_sensor)

        turbity_registry = None if turbity_registry == None else turbity_registry + get_variation_from_registry(turbity_sensor.MAX_VALUE, variation)
        ph_registry = None if ph_registry == None else ph_registry - get_variation_from_registry(ph_sensor.MAX_VALUE, variation)
        oxigem_registry = None if oxigem_registry == None else oxigem_registry - get_variation_from_registry(oxigem_sensor.max_range, variation)
        condutivity_registry = None if condutivity_registry == None else condutivity_registry + get_variation_from_registry(condutivity_sensor.MAX_VALUE, variation)
        # level_registry = level_registry

        data = {
            'temperature': temperature_registry,
            'turbidy': turbity_registry,
            'ph': ph_registry,
            'dissolvedOxygen': oxigem_registry,
            'conductivity': condutivity_registry
        }

        iothub_messaging_sample_run(str(data))

        
    
def generate_variation(temp_value, temp_sensor):
    if temp_value == None:
        return 0
    return (temp_value - temp_sensor.MIN_VALUE) / 10.0

def get_variation_from_registry(max_value, variation):
    return (max_value * 0.1) * variation

if __name__ == "__main__":
    main()