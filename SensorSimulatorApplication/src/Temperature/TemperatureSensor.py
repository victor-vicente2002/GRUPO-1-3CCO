from config.connection import Connector
from config.configuration import COLUMNS, TABLE
import random

class HardwareIoT:
    def read_temperature():
        temperature = "{:.2f}".format(random.uniform(21, 31))

        if HardwareIoT.break_sensor():
            temperature = 'NULL'

        VALUES = f"{temperature}"
        Connector.insert(COLUMNS, VALUES)
        print(f'INSERT INTO {TABLE} ({COLUMNS}) \nVALUES({VALUES}) \n')
        
    def break_sensor():
        return round(random.uniform(0, 10)) == 9