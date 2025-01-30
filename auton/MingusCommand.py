import commands2
import wpilib


class RunMingusqxForTime(commands2.Command):
    def __init__(self, mingusqx, speed, time):
        super().__init__()
        self.mingusqx = mingusqx
        self.speed = speed / 100
        self.timer = wpilib.Timer()
        self.time = time
        self.addRequirements([mingusqx])
    
    def initialize(self):
        self.timer.reset()
        self.timer.start()
    
    def execute(self):
        self.mingusqx.mingussy(self.speed)
    
    def isFinished(self):
        return self.timer.get() >= self.time
    
    def end(self, interrupted):
        self.mingusqx.mingussy(0)
