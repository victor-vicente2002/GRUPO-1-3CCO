from turbity.turbity_sensor import *
from temperature.temperature_sensor import *
from temperature.enums import *
from level.level_sensor import *
from ph.ph_sensor import *
from dissolved_oxigen.kit_oem import *
from condutivity.condutivity_sensor import *
from azure.iot.device import IoTHubDeviceClient
from azure.iot.device import Message
import uuid
from datetime import timedelta, datetime

def iothub_messaging_sample_run(data, device_id, connection_string):
    device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)
    try:
        
        device_client.connect()

        msg= {"Time:": str(datetime), "SensorData": str(data)} 
        msg = Message(json.dumps(msg))
        msg.message_id = uuid.uuid4()
        msg.device_id = device_id
        msg.content_encoding = "utf-8"
        msg.content_type = "application/json"
        print("sending message #" + str(msg.message_id) + ": body: " + str(msg))
        
        device_client.send_message(msg)
    except KeyboardInterrupt:
        print("User initiated exit")
    except Exception:
        print("Unexpected exception!")
        raise
    finally:
        device_client.shutdown()