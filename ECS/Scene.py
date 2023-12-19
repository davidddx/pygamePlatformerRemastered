from ECS.Systems import Systems
class Scene:
    def __init__(self, dir):
        self.dir = dir;
        self.sceneEntities = []

    def addentity(self, entity):
        self.sceneEntities.Append(entity);

    def update(self):
        Systems.PhysicsProcess(self.sceneEntities)
        Systems.DisplayProcess(self.sceneEntities)