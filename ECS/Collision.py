import pygame
from ECS.Entity import Component
from gameocde.settings import COMPONENT_COLLISION
#Entities with Collision component collide with entities with collision Component
class Collision(Component):
    def __init__(self, spriteSurf : pygame.Surface, type="rect"):
        self.name = COMPONENT_COLLISION
        collsurf = None
        if type == "rect":
            collsurf = spriteSurf.get_rect()
        elif type == "mask":
            collsurf = pygame.mask.from_surface(spriteSurf)
        else:
            collsurf = spriteSurf.get_rect()
        
        self.CollisionSurface = collsurf