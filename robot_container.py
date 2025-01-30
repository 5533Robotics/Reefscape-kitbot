import commands2
import commands2.button
import commands2.cmd
import ntcore
import wpilib

from subsystems.command_MecanumDrive import MecanumDrive
from subsystems.command_Mingusqx import Mingusqx
from subsystems.vision import Vision
from utils.math import linear_remap


class RobotContainer:
    def __init__(self) -> None:

        self.front_left = wpilib.Spark(3)
        self.rear_left = wpilib.Spark(2)
        self.front_right = wpilib.Spark(1)
        self.rear_right = wpilib.Spark(0)

        self.front_right.setInverted(True)
        self.rear_right.setInverted(True)

        self.robot_drive = MecanumDrive(
            self.front_left, self.rear_left, self.front_right, self.rear_right
        )

        self.minugusqx = Mingusqx(wpilib.Spark(4))

        self.network_tables = ntcore.NetworkTableInstance.getDefault()
        self.limelight = self.network_tables.getTable("limelight")

        self.joystick = commands2.button.CommandJoystick(0)
        self.controller = commands2.button.CommandXboxController(1)

        self.configureButtonBindings()

    def vision(self):
        vision = Vision(self.robot_drive)
        a = self.controller.a()._condition()
        tx = self.limelight.getNumber("tx", 1)
        
        
        z = (
            self.joystick.getZ() / 2
            if not a
            else tx / 27
        )
        return self.robot_drive.drive(
            self.joystick.getX(),
            self.joystick.getY(),
            z,
        )

    def configureButtonBindings(self) -> None:
        self.robot_drive.setDefaultCommand(
            self.robot_drive.apply_request(lambda: self.vision())
        )

        self.controller.b().whileTrue(self.minugusqx.mingussy(85))

    def getAutonomousCommand(self) -> commands2.Command:
        return commands2.cmd.print_("No autonomous command configured")
