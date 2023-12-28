import pygame.display, pygame.surface
from debug.logger import logger
from gamecode.settings import *
from ECS.Entity import Entity
class Systems:
    @staticmethod
    def PhysicsProcess(entity : Entity):
        physicsComponent = entity.getComponent(COMPONENT_PHYSICS)
        if not physicsComponent: return None;
        posComponent = entity.getComponent(COMPONENT_POSITION)
        if not posComponent: logger.error(f"{entity.name = } Has {COMPONENT_PHYSICS} component but no {COMPONENT_POSITION} component")
        posComponent.x += physicsComponent.xvelocity
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

    def HandleCollision(self, entities : list):
        for i in range(len(entities)):
            collision_component1 = entity[i].getComponent(COMPONENT_COLLISION)
            if not collision_component1:
                continue
            logger.debug(f"{entities[i]=} has Collision Component")
            for j in range(i + 1, len(entities)):
                collision_component2 = entity[j].get_component(COMPONENT_COLLISION)
                if not collision_component2:
                    continue;
                logger.debug(f"{entities[j]=} has Collision Component")
                if not (collision_component1.rect.colliderect(collision_component2.rect)
                ):
                    continue;
                logger.debug(f"{entities[i]=} and {entities[j]=} have collided")


    @staticmethod
    def Update(entities : list):
        screen = pygame.display.get_surface()
        for entity in entities:
            Systems.DisplayProcessTilemap(entity= entity, screen=screen)
            Systems.DisplayProcess(entity= entity, screen=screen)
            Systems.PhysicsProcess(entity= entity)
        Systems.HandleCollision(entities)