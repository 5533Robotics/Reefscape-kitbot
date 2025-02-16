import commands2
from ntcore import NetworkTable

from subsystems.command_MecanumDrive import MecanumDrive


class AlignToAprilTag(commands2.Command):
    def __init__(self, drive: MecanumDrive, limelight: NetworkTable):
        super().__init__()
        self.drive = drive
        self.limelight = limelight
        self.kP = 0.35

        self.addRequirements(drive)
    
    def initialize(self):
        pass
    
    def execute(self):
        target_valid = self.limelight.getNumber("tv", 0)
        if target_valid:
            tx = self.limelight.getNumber("tx", 0.0)  
            x_correction = -self.kP * tx  
            self.drive.drive(-x_correction, 0, 0)  
        else:
            self.drive.drive(0, 0, 0)
    
    def isFinished(self):
        target_valid = self.limelight.getNumber("tv", 0)
        return target_valid and abs(self.limelight.getNumber("tx", 0.0)) < 0.1
    
    def end(self, interrupted):
        self.drive.drive(0, 0, 0)  
