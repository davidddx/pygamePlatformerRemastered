import pygame
from ECS.Entity import Component
import gamecode.settings
from debug.logger import logger
#image class takes the following arguments
class VisibleObject(Component ,pygame.sprite.Sprite):
    def __init__(self, spritedir, x=0, y=0):
        pygame.sprite.Sprite.__init__(self);
        self.sprite = pygame.image.load(spritedir)
        self.rect = self.sprite.get_rect();
        self.rect.center = (x,y);
        self.width = self.rect.width;
        self.height = self.rect.height;

    def update(self):
        gamecode.settings.screen.blit(self.sprite, (self.rect.x, self.rect.y))