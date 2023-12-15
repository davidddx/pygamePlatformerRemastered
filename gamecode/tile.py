import pygame.sprite

from gamecode.settings import *
from components.VisibleObject import VisibleObject;

class Tile():
    def __init__(self, x, y, imagedir, isCollidable=false):
        self.visibleobject = VisibleObject(spritedir=imagedir, x=x * 16, y=y * 16);