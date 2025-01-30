import math
from commands2 import Command, cmd
from ntcore import NetworkTable
from wpimath.geometry import Rotation2d

from subsystems.command_MecanumDrive import MecanumDrive


class CONSTANTS:
    MOUNT_ANGLE = 0
    HEIGHT = 12
    TARGET_HEIGHT = 8


class Vision:
    def __init__(self, drive_train: MecanumDrive):
        self.drive_train = drive_train

    def distance(self, tx):
        angle_to_target = Rotation2d.fromDegrees(
            CONSTANTS.MOUNT_ANGLE
        ) + Rotation2d.fromDegrees(tx)



        return (CONSTANTS.TARGET_HEIGHT - CONSTANTS.HEIGHT) / angle_to_target.tan()

    def calculate_rotation_error(self, tx):
        camera_horizontal_offset = tx / self.distance(tx)
        error = math.atan(
            (math.atan(camera_horizontal_offset / self.distance(tx))) / self.distance(tx)
        )
        print(error)
        return error
