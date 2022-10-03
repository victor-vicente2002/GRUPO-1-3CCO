from pickletools import bytes8


# Objeto que seja até 20 bytes

class SensorData:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __str__(self) -> str:
        return f'registerId: {self.id}, value: {self.value}'