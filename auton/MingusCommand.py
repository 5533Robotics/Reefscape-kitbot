from commands2 import Command
import wpilib
from subsystems.command_Mingusqx import Mingusqx

class RunMingusqxForTime(Command):
    def __init__(self, mingusqx: Mingusqx, speed: int, time: float):
        super().__init__()
        self.mingusqx = mingusqx
        self.speed = speed / 100  
        self.timer = wpilib.Timer()
        self.time = time
        self.addRequirements(mingusqx)

    def initialize(self):
        self.timer.reset()
        self.timer.start()
        self.mingusqx.run(self.speed)  

    def execute(self):
        pass  

    def isFinished(self):
        return self.timer.get() >= self.time

    def end(self, interrupted):
        self.mingusqx.stop()  
