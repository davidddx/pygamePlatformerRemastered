from ECS.Entity import Component
from gamecode.settings import COMPONENT_PHYSICS
class Physics(Component):
    def __init__(self, xvelocity=0, yvelocity=0, gravity=1):
        self.name = COMPONENT_PHYSICS
        self.xvelocity = xvelocity;
        self.yvelocity = yvelocity;
        self.gravity = gravity
