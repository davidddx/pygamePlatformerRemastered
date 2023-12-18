import pygame
from ECS.Entity import Component
import gamecode.settings
from debug.logger import logger
#image class takes the following arguments
class VisibleObject(Component):
    def __init__(self, spritedir):
        self.name = "VisibleObject"
        pygame.sprite.Sprite.__init__(self);
        self.sprite = pygame.image.load(spritedir)
        rect = self.sprite.get_rect();
        self.width = rect.width;
        self.height = rect.height;