from commands2 import Command, Subsystem
import wpilib

class MecanumDrive(Subsystem):
    def __init__(
        self, front_left: wpilib.Spark, rear_left: wpilib.Spark, front_right: wpilib.Spark, rear_right: wpilib.Spark
    ):
        self.front_left = front_left
        self.rear_left = rear_left
        self.front_right = front_right
        self.rear_right = rear_right


    def apply_request(
        self, request
    ) -> Command:
        return self.run(lambda: request())

    
    def drive(self, x: int, y: int, z: int):
        fl = y - z - x
        fr = y + z + x
        bl = y - z + x
        br = y + z - x
        self.front_left.set(fl)
        self.front_right.set(fr)
        self.rear_left.set(bl)
        self.rear_right.set(br)