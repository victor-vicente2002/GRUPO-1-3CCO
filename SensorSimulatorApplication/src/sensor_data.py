
# Objeto que seja até 20 bytes

class SensorData:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __str__(self) -> str:
        return f'id: {self.id}, value: {self.value}'