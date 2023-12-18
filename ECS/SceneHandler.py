import os
import importlib
# this class needs a list of scenes to work.
# can start at different scene numbers
from debug.logger import logger

class SceneHandler:
    def __init__(self, scenenumber = 0):
        self.scenenumber = scenenumber;
        cwd = os.getcwd()
        self.scenes = self.load_scenes()


    def load_scenes(self):
        cwd = os.getcwd()
        scenesdir = os.path.join(cwd, 'Scenes')
        scene_modules = []

        for filename in os.listdir(scenesdir):
            if filename.endswith(".py") and not filename.startswith("__"):
                scene_module_name = filename[:-3]  # Remove the ".py" extension
                scene_module_path = f'Scenes.{scene_module_name}'
                try:
                    scene_module = importlib.import_module(scene_module_path)
                    scene_modules.append(scene_module)
                    logger.debug(f"Loaded scene module: {scene_module_path}")
                except Exception as e:
                    logger.error(f"Failed to load scene module {scene_module_path}: {e}")

        return scene_modules

    def changescenetonext(self):
        logger.debug(f"changing to scene number: {self.scenenumber + 1}")

    def Update(self):
        self.currentscene.update()
