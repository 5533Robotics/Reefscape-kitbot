from auton.DriveCommand import DriveForTime
from auton.MingusCommand import MingusForTime
from subsystems.command_MecanumDrive import MecanumDrive
from subsystems.command_Mingusqx import Mingusqx


class AutonCommand:
    def __init__(self, drive: MecanumDrive, mingusqx: Mingusqx, program):
        self.drive = drive
        self.mingusqx = mingusqx
        self.program = program
        self.conversions = {
            "drive": self.create_drive_command,
            "mingusqx": self.create_mingus_command
        }
    
    def create_drive_command(self, cmd):
        x_speed, y_speed, z_rotation = cmd["position"]
        return DriveForTime(self.drive, x_speed, y_speed, z_rotation, cmd["time"])

    def create_mingus_command(self, cmd):
        return MingusForTime(self.mingusqx, cmd["speed"], cmd["time"])

    def parse(self):
        return [self.conversions[cmd["subsystem"]](cmd) 
                for cmd in self.program if cmd["subsystem"] in self.conversions]
