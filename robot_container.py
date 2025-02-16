from commands2 import cmd
import commands2
import commands2.util
import ntcore
import wpilib
from auton.AlignToAprilTag import AlignToAprilTag
from auton.auton_parse import AutonParser
from auton.auton_tokenize import AutonTokenizer
from auton.auton_translation import AutonCommand
from subsystems.command_MecanumDrive import MecanumDrive
from subsystems.command_Mingusqx import Mingusqx

class RobotContainer:
    def __init__(self) -> None:
        self.speed = 85
        self.taker = wpilib.DigitalInput(0)
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

        print(f"{self.taker.get()}")
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
                lambda: self.mingusqx.run(self.speed),
                lambda: self.mingusqx.run(0),
                self.mingusqx,
            )
        )

        self.joystick.button(3).whileTrue(
            cmd.runEnd(
                lambda: self.speed,
                lambda: setattr(self, "speed", self.speed - 5),
                self.mingusqx,
            )
        )

        self.joystick.button(4).whileTrue(
            AlignToAprilTag(self.robot_drive, self.limelight)
        )

        self.joystick.button(5).whileTrue(
            cmd.runEnd(
                lambda: self.speed,
                lambda: setattr(self, "speed", self.speed + 5),
                self.mingusqx,
            )
        )

        

    def getAutonomousCommand(self) -> commands2.Command:

        file = open(wpilib.getOperatingDirectory() + "/autons/two_piece.txt", "r")
        content = file.read()
        tokenizer = AutonTokenizer(content)
        parser = AutonParser(tokenizer._tokenize())
        auton = parser.parse()
        commands = (AutonCommand(self.robot_drive, self.mingusqx, auton)).parse()
        file.close()
        return commands2.SequentialCommandGroup(*commands)
