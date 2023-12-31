import os
import importlib
import pygame
from debug.logger import logger
from settings import true,false
import gamecode
import sys
class SceneHandler:
    def __init__(self, scenenumber = 0):
        self.scenenumber = scenenumber;
        cwd = os.getcwd()
        self.scenes = self.load_scenes()
        logger.debug(f"{self.scenes=}")
        self.currentscenefile = self.scenes[scenenumber]
        self.scenedone = false

    def load_scenes(self):
        cwd = os.getcwd()
        scenesdir = os.path.join(cwd, 'Scenes')
        scene_modules = []
        logger.debug(f"{os.listdir(scenesdir)=}")
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

    def changescenetonext(self, step=1):
        if self.scenenumber >= len(self.scenes) - step:
            return None
        logger.debug(f"changing from scene {self.scenes[self.scenenumber]=}"
                     f"to scener: {self.scenes[scenenumber + step]=}")
        self.scenenumber+=step
        return self.scenes[self.scenenumber]

    def checkscenefinish(self):
        if not self.scenedone:
            return False
        return True
    def Update(self):
        running = true
        logger.info("Scenehandler.update is executing")
        pygame.init();
        screen = gamecode.settings.screen = pygame.display.set_mode((gamecode.settings.SCREEN_WIDTH, gamecode.settings.SCREEN_HEIGHT));
        clock = pygame.time.Clock();
        fps = 60
        while running:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.debug("Closing application. pygame.Quit signal received.")
                    running = false
            screen.fill((0, 0, 0));
            self.currentscenefile.sceneobj.update()
            if self.checkscenefinish():
                logger.debug(f"current scene {self.currentscenefile} is finished. Changing to next scene.")
                currentscene = self.currentscenefile = self.changescenetonext()
                if not currentscene:
                    running = false

            pygame.display.flip();


        logger.info("Scenehandler.update has finished executing. Closing the program")
        pygame.quit();
        sys.exit()