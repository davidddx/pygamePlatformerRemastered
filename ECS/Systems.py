import pygame.display
from Physics import *
from VisibleObject import *
from debug.logger import logger

class Systems:
    @staticmethod
    def PhysicsProcess(self, entities):
        return None;
        for entity in entities:
            pass  # physics stuff
    @staticmethod
    def DisplayProcess(self, entities):
        for entity in entities:
            visComponent = entity.getComponent("VisibleObject")
            if not visComponent:
                continue
            posComponent = entity.getComponent("Position")
            if not posComponent:
                logger.error(f"{entity = } Has VisibleObject component but no Position component")
                continue
            screen = pygame.display.get_surface()
            screen.blit(visComponent.sprite, (posComponent.x, posComponent.y))