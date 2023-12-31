import pygame.display, pygame.surface
from debug.logger import logger
from gamecode.settings import *
from ECS.Entity import Entity
class Systems:
    @staticmethod
    def PhysicsProcess(entity : Entity):
        physicsComponent = entity.getComponent(COMPONENT_PHYSICS)
        if not physicsComponent: return None;
        visibleObject = entity.getComponent(COMPONENT_VISIBLE_OBJECT)
        invisibleObject = entity.getComponent(COMPONENT_INVISIBLE_OBJECT)
        if visibleObject:
            visibleObject.rect.x += physicsComponent.xvelocity
            physicsComponent.yvelocity += physicsComponent.gravity
            visibleObject.rect.y += physicsComponent.yvelocity
            logger.debug(f"{entity.name=} | {physicsComponent.gravity=} |\n"
                         f" {physicsComponent.yvelocity=}, {physicsComponent.xvelocity=} \n"
                         f"{visibleObject.rect.x=} | {visibleObject.rect.y=}")
        elif invisibleObject:
            invisibleObject.rect.x += physicsComponent.xvelocity
            physicsComponent.yvelocity += physicsComponent.gravity
            invisibleObject.rect.y += physicsComponent.yvelocity
            logger.debug(f"{entity.name=} | {physicsComponent.gravity=} |\n"
                         f" {physicsComponent.yvelocity=}, {physicsComponent.xvelocity=} \n"
                         f"{invisibleObject.rect.x=} | {invisibleObject.rect.y=}")
        else:
            logger.error(f"{entity.name = } Has {COMPONENT_PHYSICS} component but no {COMPONENT_VISIBLE_OBJECT} or {COMPONENT_INVISIBLE_OBJECT} component")
    @staticmethod
    def DisplayProcess(entity : Entity, screen : pygame.surface):
        visComponent = entity.getComponent(COMPONENT_VISIBLE_OBJECT)
        if not visComponent: return None
        screen.blit(visComponent.sprite, (visComponent.rect.x, visComponent.rect.y))
    @staticmethod
    def DisplayProcessTilemap(entity : Entity, screen : pygame.surface):
        tilemapComponent = entity.getComponent(COMPONENT_TILEMAP)
        if not tilemapComponent:
            return None
        for tile in tilemapComponent.Tiles:
            screen.blit(tile.image, (tile.rect.x, tile.rect.y))

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
        # Systems.HandleCollision(entities)