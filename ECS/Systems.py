import pygame.display
from debug.logger import logger
from ECS.Entity import Entity
class Systems:
    @staticmethod
    def PhysicsProcess(self, entity : Entity):
        return None;
        pass #physicsStuff
    @staticmethod
    def DisplayProcess(self, entity : Entity):
        visComponent = entity.getComponent("VisibleObject")
        if not visComponent:
            return None
        posComponent = entity.getComponent("Position")
        if not posComponent:
            logger.error(f"{entity = } Has VisibleObject component but no Position component")
            return None
        screen = pygame.display.get_surface()
        screen.blit(visComponent.sprite, (posComponent.x, posComponent.y))
    @staticmethod
    def Update(self, entities : list):
        for entity in entities:
            Systems.DisplayProcess(entity= entity)
            Systems.PhysicsProcess(entity= entity)
