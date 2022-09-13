import random
import sys
from azure.iot.hub import IoTHubRegistryManager
from TurbityPlus import *


MESSAGE_COUNT = 10
AVG_WIND_SPEED = 10.0
MSG_TXT = "\"service client sent a message\": "
CONNECTION_STRING = "HostName=testingIotMessagesVicente.azure-devices.net;SharedAccessKeyName=device;SharedAccessKey=uuhKWf+kgrcpGLj/iyxob1wrYcAEk3VQOOUTMWO3hhE="
DEVICE_ID = "turbity_plus_test"

def iothub_messaging_sample_run():
    try:
        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
        sensor = TurbityPlus(Type.ADVANCED.name, "-30420348203442", "130981209239128")

        for i in range(0, MESSAGE_COUNT):
            print ( 'Sending message: {0}'.format(i) )
            sensorData = sensor.readSensorData()
            data = MSG_TXT + sensorData.__str__()
            print(data)

            props={}
            # optional: assign system properties
            props.update(messageId = "message_%d" % sensorData.registerId)
            props.update(correlationId = "correlation_%d" % sensorData.registerId)
            props.update(contentType = "application/json")

            # optional: assign application properties
            prop_text = "PropMsg_%d" % i
            props.update(testProperty = prop_text)

            registry_manager.send_c2d_message(DEVICE_ID, data, properties=props)

        try:
            # Try Python 2.xx first
            raw_input("Press Enter to continue...\n")
        except:
            pass
            # Use Python 3.xx in the case of exception
            input("Press Enter to continue...\n")

    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )

if __name__ == '__main__':
    print ( "Starting the Python IoT Hub C2D Messaging service sample..." )

    iothub_messaging_sample_run()