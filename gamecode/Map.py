import pygame
from ECS.Tile import Tile
from debug.logger import logger
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
class Map:
    def __init__(self, mapdata, daytime="D"):
        self.Tiles = self.convertMapdataToSpritegroup(mapdata)
        self.BackgroundTiles = self.getBackgroundSpriteGroup(daytime = daytime)
        self.daytime = daytime

    def getBackgroundSpriteGroup(self, daytime):
        def generatetiles(imagedir):
            spritegroup = pygame.sprite.Group()
            for i in range(int(SCREEN_WIDTH/TILE_SIZE) + 1):
                for j in range(int(SCREEN_HEIGHT/TILE_SIZE) + 1):
                    spritegroup.add(Tile(x=i, y=j, imagedir=imagedir).visibleobject)
            return spritegroup
        if daytime == "D":
            return generatetiles(imagedir="TileImages/BasicBlueSkyTile.png")


        elif daytime == "N":
            return generatetiles(imagedir="TileImages/BasicBlueSkyTile.png")
        else:
            return generatetiles(imagedir="TileImages/BasicBlueSkyTile.png")




    # converts mapdata in gamedata/maps to spritegroup of tile class
    def convertMapdataToSpritegroup(self, mapdata):
        spritegroup = pygame.sprite.Group()
        def readlist(yval, list):
            for xval, letter in enumerate(list):
                if letter == 'S':
                    logger.debug(f"{xval=} | {yval=}")
                    tile = Tile(x=xval, y=yval, imagedir="TileImages/BasicBlueSkyTile.png")
                    spritegroup.add(tile.visibleobject)
                    # return Tile(x=, y=, imagedir=, iscollidable = false)
                elif letter == 'B':
                    pass
                else:
                    pass
        for idx1, list in enumerate(mapdata):
            readlist(yval= idx1, list=list);
            # logger.info(f"\n mapdata {idx1=} \n mapdata {list=}");

        for image in spritegroup:
            logger.debug(f"\n {image.rect.x=}, {image.rect.y=}")
        return spritegroup


    def update(self):
        for visibleobject in self.BackgroundTiles:
            visibleobject.update()
