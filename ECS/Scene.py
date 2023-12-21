from ECS.Systems import Systems
class Scene:
    def __init__(self):
        self.Entities = []

    def addentity(self, entity):
        self.Entities.append(entity);

    def update(self):
        Systems.Update(entities=self.Entities);