import pygame
from components.Entity import Entity
import gamecode.settings
from debug.logger import logger
#image class takes the following arguments
class VisibleObject(Entity ,pygame.sprite.Sprite):
    def __init__(self, spritedir, x=0, y=0):
        pygame.sprite.Sprite.__init__(self);
        Entity.__init__(self);
        self.sprite = pygame.image.load(spritedir)
        self.rect = self.sprite.get_rect();
        self.rect.center = (x,y);
        self.width = self.rect.width;
        self.height = self.rect.height;

    def update(self):
        gamecode.settings.screen.blit(self.sprite, (self.rect.x, self.rect.y))