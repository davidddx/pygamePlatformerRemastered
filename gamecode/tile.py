import pygame.sprite

from gamecode.settings import TILE_SIZE
from ECS.VisibleObject import VisibleObject;

class Tile():
    def __init__(self, x, y, imagedir, isCollidable=false):
        self.visibleobject = VisibleObject(spritedir=imagedir, x=x * TILE_SIZE, y=y * TILE_SIZE);