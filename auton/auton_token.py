from enum import Enum

class AutonTokenTypes(Enum):
    ACTION = 0
    SUBSYSTEM = 1

    PREPOSITION = 2

    POSITION = 3
    SPEED = 4
    DURATION = 5

    EOF = 6

class AutonToken:
    def __init__(self, _type: AutonTokenTypes, value: str):
        self.type = _type
        self.value = value
    
    def get_value(self):
        if(self.get_type == AutonTokenTypes.DURATION):
            return self.value[:-1]
        return self.value
    
    def get_type(self):
        return self.type

    def parse_position(self):
        position = [0, 0, 0]
        token_position = self.get_value()[-1]
        match token_position:
            case "x":
                position[0] = int(self.get_value()[:-1])
            case "y":
                position[1] = int(self.get_value()[:-1])
            case "z":
                position[2] = int(self.get_value()[:-1])
        return position
