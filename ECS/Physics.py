from ECS.Entity import Component

class Position(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Physics(Component):
    def __init__(self, xvelocity=0, yvelocity=0, gravity=1):
        self.name = "Physics"
        self.xvelocity = xvelocity;
        self.yvelocity = yvelocity;
        self.gravity = gravity
