import pygame
from gamecode.tile import Tile
from debug.logger import logger
class Map:
    def __init__(self, mapdata):
        self.Tiles = self.convertMapdataToSpritegroup(mapdata)


    def convertMapdataToSpritegroup(self, mapdata):
        spritegroup = pygame.sprite.Group()
        def readlist(idx1, list):
            for idx2, letter in enumerate(list):
                if letter == 'S':
                    tile = Tile(x=idx1, y=idx2, imagedir="TileImages/BasicBlueSkyTile.png")
                    spritegroup.add(tile.visibleobject)
                    # return Tile(x=, y=, imagedir=, iscollidable = false)
                elif letter == 'B':
                    pass
                else:
                    pass
        for idx1, list in enumerate(mapdata):
            readlist(idx1= idx1, list=list);
            # logger.info(f"\n mapdata {idx1=} \n mapdata {list=}");

        for image in spritegroup:
            logger.debug(f"\n {image.rect.x=}, {image.rect.y=}")
        return spritegroup


    def update(self):
        for visibleobject in self.Tiles:
            visibleobject.update()
