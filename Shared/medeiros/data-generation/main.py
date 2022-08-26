import json
import datetime
from random import Random, random
from time import sleep
values = []

def getPHValue():
    return Random().randrange(6, 9)

def run():
    while True:
        data = {
            "ph": getPHValue(),
            "dateTime": str(datetime.datetime.now())
        }
        json_data = json.dumps(data)
        print(json_data)
        values.append(json_data)
        sleep(1)

run()