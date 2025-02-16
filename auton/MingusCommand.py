import commands2
import wpilib
from subsystems.command_Mingusqx import Mingusqx

class MingusForTime(commands2.Command):
    def __init__(self, mingusqx: Mingusqx, speed: int, time_seconds: float):
        super().__init__()
        self.mingusqx = mingusqx
        self.speed = speed
        self.time = time_seconds
        self.timer = wpilib.Timer()
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
        self.mingusqx.run(0)
