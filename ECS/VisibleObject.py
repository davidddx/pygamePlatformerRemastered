import pygame
from ECS.Entity import Component
import gamecode.settings
from debug.logger import logger
from gamecode.settings import COMPONENT_VISIBLE_OBJECT
#image class takes the following arguments
class VisibleObject(Component):
    def __init__(self, spritedir):
        self.name = COMPONENT_VISIBLE_OBJECT
        self.sprite = pygame.image.load(spritedir)
        self.rect = self.sprite.get_rect();

class InvisibleObject(Component):
    def __init__(self, posx = 0, posy = 0):
        self.name = COMPONENT_INVISIBLE_OBJECT
        self.rect = pygame.Rect(posx, posy, 0, 0)