from auton.auton_token import AutonToken, AutonTokenTypes


class AutonTokenizer:
    def __init__(self, source: str):
        self.subsystems = {"mingusqx", "drive"}
        self.prepositions = {"for", "at"}
        self.source = source
        self.tokens = []
        self.position = 0

    def _is_number(self, value: str):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _tokenize(self):
        for line in self.source.split('\n'):
            parts = line.strip().split()
            for part in parts:
                if part == "run":
                    self.tokens.append(AutonToken(AutonTokenTypes.ACTION, part))
                elif part in self.subsystems:
                    self.tokens.append(AutonToken(AutonTokenTypes.SUBSYSTEM, part))
                elif part in self.prepositions:
                    self.tokens.append(AutonToken(AutonTokenTypes.PREPOSITION, part))
                elif part.endswith('s') and self._is_number(part[:-1]):
                    self.tokens.append(AutonToken(AutonTokenTypes.DURATION, part))
                elif part.endswith(("x", "y", "z")):
                    if not part[-2].isdigit():
                        raise ValueError(f"Invalid distance: {part}")
                    self.tokens.append(AutonToken(AutonTokenTypes.POSITION, part))
                elif self._is_number(part):
                    self.tokens.append(AutonToken(AutonTokenTypes.SPEED, part))
                else:
                    raise ValueError(f"Unexpected token: {part}")
        self.tokens.append(AutonToken(AutonTokenTypes.EOF, ""))
        return self.tokens
