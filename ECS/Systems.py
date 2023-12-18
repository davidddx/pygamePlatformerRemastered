import pygame.display
from Physics import *
from VisibleObject import *

class System:
    class PhysicsSystem:
        def run(self, entities):
            for entity in entities:
                pass  # physics stuff

    class VisibleObjectSystem:
        def run(self, entities):
            for entity in entities:
                visComponent = entity.getComponent("VisibleObject")
                if not visComponent:
                    continue
                posComponent = entity.getComponent("Position")
                if not posComponent:
                    continue
                screen = pygame.display.get_surface()
                screen.blit(visComponent.sprite, (posComponent.x, posComponent.y))