import pygame.display, pygame.surface
from debug.logger import logger
from gamecode.settings import COMPONENT_VISIBLE_OBJECT, COMPONENT_TILEMAP, COMPONENT_POSITION
from ECS.Entity import Entity
class Systems:
    @staticmethod
    def PhysicsProcess(entity : Entity):
        return None;
        pass #physicsStuff
    @staticmethod
    def DisplayProcess(entity : Entity, screen : pygame.surface):
        visComponent = entity.getComponent(COMPONENT_VISIBLE_OBJECT)
        if not visComponent:
            return None
        posComponent = entity.getComponent(COMPONENT_POSITION)
        if not posComponent:
            logger.error(f"{entity.name = } Has {COMPONENT_VISIBLE_OBJECT} component but no {COMPONENT_POSITION} component")
            return None
        screen.blit(visComponent.sprite, (posComponent.x, posComponent.y))
    @staticmethod
    def DisplayProcessTilemap(entity : Entity, screen : pygame.surface):
        tilemapComponent = entity.getComponent(COMPONENT_TILEMAP)
        if not tilemapComponent:
            return None
        for tile in tilemapComponent.Tiles:
            screen.blit(tile.image, (tile.Position.x, tile.Position.y))

    @staticmethod
    def Update(entities : list):
        screen = pygame.display.get_surface()
        for entity in entities:
            Systems.DisplayProcessTilemap(entity= entity, screen=screen)
            Systems.DisplayProcess(entity= entity, screen=screen)
            Systems.PhysicsProcess(entity= entity)
