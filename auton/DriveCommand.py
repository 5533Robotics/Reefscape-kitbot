import commands2
import wpilib

from subsystems.command_MecanumDrive import MecanumDrive

class DriveForTime(commands2.Command):
    def __init__(self, drive: MecanumDrive, x_speed: int, y_speed: int, z_rotation: int, time_seconds: int):
        super().__init__()
        self.drive = drive
        self.x_speed = x_speed / 100
        self.y_speed = y_speed / 100
        self.z_rotation = z_rotation / 100
        self.timer = wpilib.Timer()
        self.time = time_seconds 
        self.addRequirements(drive)
    
    def initialize(self):
        self.timer.reset()
        self.timer.start()
    
    def execute(self):
        self.drive.drive(self.x_speed, self.y_speed, self.z_rotation)
    
    def isFinished(self):
        return self.timer.get() >= self.time
    
    def end(self, interrupted):
        self.drive.drive(0, 0, 0)