from ECS.Scene import Scene
from ECS.Entity import Entity
from ECS.Physics import Position
from ECS.VisibleObject import VisibleObject
from ECS.Tile import Tilemap
from gamecode.settings import true, false, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from debug.logger import logger
import os
from gamedata.Maps import World1
cwd = os.getcwd()
sceneobj = Scene()
blueskytiledir = cwd + '/TileImages/BasicBlueSkyTile.png'
tmap = Entity(name="tmap")
tmapComponent = Tilemap(tiles= World1.Level1, Tileset= {'S' : blueskytiledir} )
tmap.addComponent(tmapComponent)
sceneobj.addentity(tmap)

# image = Entity(name="image")
# image.addComponent(Position(x=0, y=0))
# image.addComponent(VisibleObject(spritedir=cwd + '/TileImages/BasicBlueSkyTile.png'))
# sceneobj.addentity(image)