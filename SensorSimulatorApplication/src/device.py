import time
from turbity.turbity_sensor import TurbitySensor, Type
from temperature.temperature_sensor import TemperatureSensor
from level.level_sensor import LevelSensor
from ph.ph_sensor import PhSensor
from dissolved_oxigen.kit_oem import KitOEM
from condutivity.condutivity_sensor import CondutivitySensor
from iot_hub_sender import iothub_messaging_sample_run

# "HostName=testingIotMessagesVicente.azure-devices.net;SharedAccessKeyName=device;SharedAccessKey=uuhKWf+kgrcpGLj/iyxob1wrYcAEk3VQOOUTMWO3hhE="

class Device:
    def __init__(self, device_id, connection_string):
        self.temperature_sensor = TemperatureSensor()
        self.turbity_sensor = TurbitySensor(Type.ADVANCED.name)
        self.ph_sensor = PhSensor()
        self.level_sensor = LevelSensor()
        self.oxigem_sensor = KitOEM()
        self.condutivity_sensor = CondutivitySensor()
        self.battery_percentage = 100.0
        self.device_id = device_id
        self.connection_string = connection_string
    
    def generate_variation(self, temp_value, min_value):
        if temp_value == None:
            return 0
        return (temp_value - min_value) / 10.0

    def get_variation_from_registry(self, max_value, variation):
        return (max_value * 0.1) * variation
    
    def read_data(self):
        while(True):
            temperature_registry = self.temperature_sensor.read_temperature()
            turbity_registry = self.turbity_sensor.read_sensor_data()
            ph_registry = self.ph_sensor.get_ph_value()
            oxigem_registry = self.oxigem_sensor.read()
            condutivity_registry = self.condutivity_sensor.read_sensor_data()

            variation = self.generate_variation(temperature_registry, self.temperature_sensor.MIN_VALUE)

            turbity_registry = None if turbity_registry == None \
                else round(turbity_registry + self.get_variation_from_registry(
                    self.turbity_sensor.MAX_VALUE, 
                    variation
                ), )

            ph_registry = None if ph_registry == None \
                else round(ph_registry - self.get_variation_from_registry(
                    self.ph_sensor.MAX_VALUE,
                    variation
                ), 2)

            oxigem_registry = None if oxigem_registry == None \
                else round(oxigem_registry - self.get_variation_from_registry(
                    self.oxigem_sensor.max_range,
                    variation
                ), 2)
                
            condutivity_registry = None if condutivity_registry == None \
                else round(condutivity_registry  + self.get_variation_from_registry(
                    self.condutivity_sensor.MAX_VALUE,
                    variation
                ), 2)

            if self.battery_percentage <= (0.005 * 4):
                print("Mensagem de last will")
                iothub_messaging_sample_run("last will", self.device_id, self.connection_string)
            else:
                message_one = f'1{temperature_registry};{ph_registry};{round(self.battery_percentage, 3)}'
                iothub_messaging_sample_run(message_one, self.device_id, self.connection_string)
                self.battery_percentage = self.battery_percentage - 0.005
                message_two = f'2{turbity_registry};{oxigem_registry};{round(self.battery_percentage, 3)}'
                iothub_messaging_sample_run(message_two, self.device_id, self.connection_string)
                self.battery_percentage = self.battery_percentage - 0.005
                message_three = f'3{condutivity_registry};{round(self.battery_percentage, 3)}'
                iothub_messaging_sample_run(message_three, self.device_id, self.connection_string)
                self.battery_percentage = self.battery_percentage - 0.005
                print(f'Battery: {self.battery_percentage}')

if __name__ == "__main__":
    device = Device("device_water_solution_0001", "HostName=testingIotMessagesVicente.azure-devices.net;SharedAccessKeyName=device;SharedAccessKey=uuhKWf+kgrcpGLj/iyxob1wrYcAEk3VQOOUTMWO3hhE=")
    while(True):
        time.sleep(10)
        device.read_data()