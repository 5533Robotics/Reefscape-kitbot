from typing import List
from auton.auton_token import AutonToken, AutonTokenTypes


class AutonParser:
    def __init__(self, tokens: List[AutonToken]):
        self.tokens = tokens
        self.program = []
        self.position = 0

    def parse(self):
        body = {}
        while self.at().get_type() != AutonTokenTypes.EOF:
            if self.at().get_type() != AutonTokenTypes.ACTION:
                raise ValueError("Auton should start with type of ACTION")
            self.consume()

            body["subsystem"] = self.at().get_value()

            self.consume()

            if self.at().get_type() != AutonTokenTypes.PREPOSITION:
                if self.at().get_value() != "for":
                    raise ValueError("Preposition of 'for' should follow type of SUBSYSTEM")
                raise ValueError("Preposition should follow type of SUBSYSTEM")
            self.consume()

            body["time"] = float(self.at().get_value()[:-1])

            self.consume()

            if self.at().get_type() != AutonTokenTypes.PREPOSITION:
                if self.at().get_value() != "at":
                    raise ValueError("Preposition of 'at' should follow type of TIME")
                raise ValueError("Preposition should follow type of SUBSYSTEM")
            self.consume()

            if body["subsystem"] == "drive":
                body["position"] = self.at().parse_position()
            else:
                body["speed"] = int(self.at().get_value())
            self.consume()
            
            self.program.append(body)
            body = {}
        return self.program
            


    def consume(self):
        self.position += 1

    def at(self):
        return self.tokens[self.position]



