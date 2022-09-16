import json
import datetime
from azure.iot.hub import IoTHubRegistryManager
from random import randrange, random
from time import sleep
values = []
CONNECTION_STRING = "HostName=ph-sensor.azure-devices.net;SharedAccessKeyName=device;SharedAccessKey=FnE7PLEKz0729CqYKwGZNll2DDROQ26x7HPBZTyHtjg="
DEVICE_ID = 'ph-sensor01'

interval_in_seconds = 15 * 60

def getPHValue(last_ph_value):
    ph_variation = round(random(), 3)
    normal_variation_probability = random()
    ph_value = None
    if normal_variation_probability > 0.1: # representa 80% de chance
        sum_or_sub = randrange(0, 2)
        ph_value = last_ph_value + ph_variation if sum_or_sub == 1 else last_ph_value - ph_variation
    else:
        ph_value = randrange(4, 12) + ph_variation
    last_ph_value = ph_value
    nullable_probability = random()
    return None if nullable_probability < 0.1 else ph_value

def send_data_to_iot_hub(data):
    try:
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
        registry_manager.send_c2d_message(DEVICE_ID, data)
        print("Dado enviado para o IoT Hub")
    except Exception as e:
        print("Erro ao enviar dado para o IoT Hun")

def run():
    last_ph_value = randrange(6, 10)
    while True:
        data = {
            "ph": getPHValue(last_ph_value),
            "dateTime": str(datetime.datetime.now())
        }
        json_data = json.dumps(data)
        print(json_data)
        send_data_to_iot_hub(json_data)
        
        values.append(json_data)
        sleep(interval_in_seconds)

run()