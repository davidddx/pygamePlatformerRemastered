from ECS.Scene import Scene
# this class needs a list of scenes to work.
# can start at different scene numbers
from debug.logger import logger

class SceneHandler:
    def __init__(self, scenes, scenenumber = 0):
        self.scenenumber = scenenumber;
        self.scenesdir = scenes;
        self.currentscene = Scene(scenes[scenenumber]);


    def changescenetonext(self):
        logger.debug(f"changing to scene number: {self.scenenumber + 1}")

    def Update(self):
        self.currentscene.run()
