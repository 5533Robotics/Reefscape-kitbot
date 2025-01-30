
from commands2 import Command, Subsystem, cmd
import wpilib


class Mingusqx(Subsystem):
    def __init__(
        self, mingus_motor: wpilib.Spark
    ):
        self.mingus_motor = mingus_motor

    def run(self, voltage: int):
        voltage /= 100
        self.mingus_motor.set(voltage)
    
    def mingussy(self, voltage: int) -> Command:
        return cmd.runEnd(lambda: self.run(voltage), lambda: self.run(0))