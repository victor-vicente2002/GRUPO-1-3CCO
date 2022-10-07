from turbity.turbity_sensor import *
from temperature.temperature_sensor import *
from temperature.enums import *
from level.level_sensor import *
from ph.ph_sensor import *
from dissolved_oxigen.kit_oem import *
from condutivity.condutivity_sensor import *
from azure.iot.hub import IoTHubRegistryManager

MESSAGE_COUNT = 10
AVG_WIND_SPEED = 10.0
MSG_TXT = "\"service client sent a message\": "
CONNECTION_STRING = "HostName=testingIotMessagesVicente.azure-devices.net;SharedAccessKeyName=device;SharedAccessKey=uuhKWf+kgrcpGLj/iyxob1wrYcAEk3VQOOUTMWO3hhE="
DEVICE_ID = "turbity_plus_test"

def iothub_messaging_sample_run(data):
    try:
        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

        print ( 'Sending message to IoTHub: {0}'.format(data) )

        props={}
        # optional: assign system properties
        props.update(contentType = "application/json")

        # optional: assign application properties

        registry_manager.send_c2d_message(DEVICE_ID, data, properties=props)

    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )

# if __name__ == '__main__':
#     print ( "Starting the Python IoT Hub C2D Messaging service sample..." )

#     iothub_messaging_sample_run()