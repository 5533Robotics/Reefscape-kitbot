import typing
import commands2
from robot_container import RobotContainer
class Shplorgel(commands2.TimedCommandRobot):
    # 10ft 10.75in
    autonomousCommand: typing.Optional[commands2.Command] = None
    
    def robotInit(self) -> None:
        self.container = RobotContainer()

    def robotPeriodic(self) -> None:
        commands2.CommandScheduler.getInstance().run()

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass

    def autonomousInit(self) -> None:
        self.autonomousCommand = self.container.getAutonomousCommand()

        if self.autonomousCommand:
            self.autonomousCommand.schedule()

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        if self.autonomousCommand:
            self.autonomousCommand.cancel()
            

    def teleopPeriodic(self) -> None:
        pass

    def testInit(self) -> None:
        commands2.CommandScheduler.getInstance().cancelAll()