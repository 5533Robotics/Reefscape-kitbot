import commands2
import ntcore
import wpilib
from auton.DriveCommand import DriveForTime
from auton.MingusCommand import RunMingusqxForTime
from subsystems.command_MecanumDrive import MecanumDrive
from subsystems.command_Mingusqx import Mingusqx
from subsystems.vision import Vision


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

        self.configureButtonBindings()

    def vision(self):
        vision = Vision(self.robot_drive)
        a = self.joystick.button(3).getAsBoolean()
        tx = self.limelight.getNumber("tx", 1)
        kP = 0.5
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

        self.joystick.button(0).whileTrue(self.minugusqx.mingussy(85))

    def getAutonomousCommand(self) -> commands2.Command:
        return commands2.SequentialCommandGroup(
            DriveForTime(self.robot_drive, 40, 0, 0, 5),
            RunMingusqxForTime(self.minugusqx, 80, 3)
        )