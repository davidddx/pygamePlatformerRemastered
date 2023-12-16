from ECS.Entity import Component
class Physics(Component):
    def __init__(self, xvelocity=0, yvelocity=0, gravitationalforce=1):
        self.xvelocity = xvelocity;
        self.yvelocity = yvelocity;
        self.gravitationalforce = gravitationalforce
