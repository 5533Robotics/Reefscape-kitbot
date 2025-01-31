from commands2 import Subsystem, Command, cmd
import wpilib

class Mingusqx(Subsystem):
    def __init__(self, mingus_motor: wpilib.Spark):
        super().__init__()
        self.mingus_motor = mingus_motor

    def run(self, speed: float):
        self.mingus_motor.set(speed / 100)

    def stop(self):
        self.mingus_motor.set(0)

    def apply_request(self, speed: float) -> Command:
        return cmd.runEnd(lambda: self.run(speed), self.stop, self)
