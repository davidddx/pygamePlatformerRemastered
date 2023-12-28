import pygame
from gamecode.settings import TILE_SIZE, COMPONENT_TILEMAP
from ECS.VisibleObject import VisibleObject;
from ECS.Physics import Position
from ECS.Entity import Component
from debug.logger import logger

class Tile(Component, pygame.sprite.Sprite):
    def __init__(self, x : int, y : int, image : pygame.sprite.Sprite, isCollidable=False):
        pygame.sprite.Sprite.__init__(self);
        self.image = image;
        self.rect = self.image.get_rect();


class Tilemap(Component):
    def __init__(self, tiles : list[list[str]], Tileset = {}):
        self.name = COMPONENT_TILEMAP
        self.Tileset = self.loadImages(Tileset=Tileset) #Dictionary must follow format {'Char' : 'ImageDirectory'}
        self.Tiles = self.loadTiles(tileList= tiles);

    def loadImages(self, Tileset : dict):
        newdict = dict()
        keys = list(Tileset.keys())
        sprite = pygame.sprite.Sprite()
        for key in keys:
            sprite.image = pygame.image.load(Tileset[key])
            newdict[key] = sprite.image
        return newdict
    def loadTiles(self, tileList):
        spritegroup = pygame.sprite.Group()
        for yval, alist in enumerate(tileList):
            for xval, letter in enumerate(alist):
                if not letter in self.Tileset:
                    logger.error(f"Tile at ({xval=},{yval=}) of tilemap {self} is not defined in self.Tileset.")
                    continue;
                tile = Tile(x=xval, y=yval, image=self.Tileset[letter])
                logger.debug(f"{tile=} | {xval=} | {yval=}")
                logger.debug(f"{tile.image=}")
                spritegroup.add(tile)

                # if letter == 'S':
                #     logger.debug(f"{xval=} | {yval=}")
                #     tile = Tile(x=xval, y=yval, imagedir="TileImages/BasicBlueSkyTile.png")
                #     spritegroup.add(tile.visibleobject)
                #     logger.debug(f"{tile=} | {xval=} | {yval=}")
                # elif letter == 'B':
                #     pass
                # else:
                #     pass
        return spritegroup

