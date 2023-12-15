class Scene:
    def __init__(self, dir):
        self.dir = dir;
        self.scenechildren = []

    def addentity(self, entity):
        self.scenechildren.Append(entity);

    def update(self):
        for entity in self.scenechildren:
            entity.update()