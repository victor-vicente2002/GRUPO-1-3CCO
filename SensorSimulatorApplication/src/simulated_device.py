import time
from azure.iot.device import IoTHubDeviceClient

RECEIVED_MESSAGES = 0

CONNECTION_STRING = "HostName=testingIotMessagesVicente.azure-devices.net;DeviceId=device_water_solution_0001;SharedAccessKey=IKIR93YRNVGW8GocWg3Z+3mS6xgVqDMLg2I5PUOx/20="

def message_handler(message):
    global RECEIVED_MESSAGES
    RECEIVED_MESSAGES += 1
    print("")
    print("Message received:")
    print(message)

    # print data from both system and application (custom) properties
    for property in vars(message).items():
        print ("    {}".format(property))

    print("Total calls received: {}".format(RECEIVED_MESSAGES))

def main():
    print ("Starting the Python IoT Hub C2D Messaging device sample...")

    # Instantiate the client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print ("Waiting for C2D messages, press Ctrl-C to exit")
    try:
        # Attach the handler to the client
        client.on_message_received = message_handler

        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()

if __name__ == '__main__':
    main()