import pygame.display
from debug.logger import logger
from ECS.Entity import Entity
class Systems:
    @staticmethod
    def PhysicsProcess(entity : Entity):
        return None;
        pass #physicsStuff
    @staticmethod
    def DisplayProcess(entity : Entity, screen):
        visComponent = entity.getComponent("VisibleObject")
        if not visComponent:
            return None
        posComponent = entity.getComponent("Position")
        if not posComponent:
            logger.error(f"{entity = } Has VisibleObject component but no Position component")
            return None
        screen.blit(visComponent.sprite, (posComponent.x, posComponent.y))
    @staticmethod
    def DisplayProcessTilemap(entity : Entity, screen):
        tilemapComponent = entity.getComponent("Tilemap")
        if not tilemapComponent:
            return None
        for tile in tilemapComponent:
            screen.blit(tile.visibleobject.sprite, (tile.Position.x, tile.Position.y))

    @staticmethod
    def Update(entities : list):
        screen = pygame.display.get_surface()
        for entity in entities:
            Systems.DisplayProcessTilemap(entity= entity, screen=screen)
            Systems.DisplayProcess(entity= entity, screen=screen)
            Systems.PhysicsProcess(entity= entity)
