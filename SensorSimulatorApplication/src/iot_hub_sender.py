from turbity.turbity_sensor import *
from temperature.temperature_sensor import *
from temperature.enums import *
from level.level_sensor import *
from ph.ph_sensor import *
from dissolved_oxigen.kit_oem import *
from condutivity.condutivity_sensor import *
from azure.iot.hub import IoTHubRegistryManager

def iothub_messaging_sample_run(data, device_id, connection_string):
    try:
        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(connection_string)

        print ( f'Sending message to IoTHub: {data}' )

        props={}
        props.update(contentType = "application/json")

        registry_manager.send_c2d_message(device_id, data, properties=props)

    except Exception as ex:
        print (f'Unexpected error {ex}')
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )