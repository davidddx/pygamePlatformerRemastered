import pygame, os, gamecode.settings
from gamecode.settings import true, false
from gamecode.tile import Tile;
from debug.logger import logger
from gamecode.Map import Map
from gamedata.Maps.World1 import Level1

class Game:
    def __init__(self):
        self.running = true;


    #gameloop
    def run(self):
        logger.info("Game.run is executing")
        cwd = os.getcwd();
        pygame.init();
        gamecode.settings.screen = pygame.display.set_mode((gamecode.settings.SCREEN_WIDTH, gamecode.settings.SCREEN_HEIGHT));
        clock = pygame.time.Clock();
        running = self.running

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = false


            # SceneHandler.update()
            gamecode.settings.screen.fill((0, 0, 0));
            amap.update()
            pygame.display.flip();

        pygame.quit();

