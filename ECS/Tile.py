import pygame.sprite

from gamecode.settings import TILE_SIZE
from ECS.VisibleObject import VisibleObject;
from ECS.Physics import Position
from ECS.Entity import Component

class Tile(Component):
    def __init__(self, x : int, y : int, imagedir : str, isCollidable=False):
        self.visibleobject = VisibleObject(spritedir=imagedir);
        self.Position = Position(x=x*TILE_SIZE, y=y*TILE_SIZE)


class Tilemap(Component):
    def __init__(self, tiles : list[list[str]]):
        self.name = "Tilemap"
        self.Tiles = self.loadTiles(tileList= tiles);

    def loadTiles(self, tileList):
        spritegroup = pygame.sprite.Group()
        for yval, alist in enumerate(tileList):
            for xval, letter in enumerate(alist):
                if letter == 'S':
                    logger.debug(f"{xval=} | {yval=}")
                    tile = Tile(x=xval, y=yval, imagedir="TileImages/BasicBlueSkyTile.png")
                    spritegroup.add(tile.visibleobject)
                    logger.debug(f"{tile=} | {xval=} | {yval=}")
                elif letter == 'B':
                    pass
                else:
                    pass
        return spritegroup

