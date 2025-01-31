from commands2 import cmd
import commands2
import ntcore
import wpilib
from auton.AlignToAprilTag import AlignToAprilTag
from auton.DriveCommand import DriveForTime
from subsystems.command_MecanumDrive import MecanumDrive
from subsystems.command_Mingusqx import Mingusqx


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

        self.mingusqx = Mingusqx(wpilib.Spark(4))

        self.network_tables = ntcore.NetworkTableInstance.getDefault()
        self.limelight = self.network_tables.getTable("limelight")

        self.joystick = commands2.button.CommandJoystick(0)

        self.configureButtonBindings()

    def configureButtonBindings(self) -> None:
        self.robot_drive.setDefaultCommand(
            self.robot_drive.apply_request(
                lambda: self.robot_drive.drive(
                    self.joystick.getX(),
                    self.joystick.getY(),
                    self.joystick.getZ() / 2,
                )
            )
        )

        self.joystick.button(1).whileTrue(
            cmd.runEnd(
                lambda: self.mingusqx.run(85),
                lambda: self.mingusqx.run(0),
                self.mingusqx,
            )
        )

        self.joystick.button(4).whileTrue(
            AlignToAprilTag(self.robot_drive, self.limelight)
        )

    def getAutonomousCommand(self) -> commands2.Command:
        return commands2.SequentialCommandGroup(
        DriveForTime(self.robot_drive, 0, -40, 0, 1.90),
        cmd.runOnce(lambda: self.mingusqx.run(60), self.mingusqx),
        commands2.WaitCommand(1),
        cmd.runOnce(lambda: self.mingusqx.run(0), self.mingusqx),
    )

