from ECS.Scene import Scene
from ECS.Entity import Entity
from ECS.Physics import Physics
from ECS.VisibleObject import VisibleObject, InvisibleObject
from ECS.Tile import Tilemap
from gamecode.settings import true, false, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from debug.logger import logger
import os
from gamedata.Maps import World1
cwd = os.getcwd()
sceneobj = Scene()
blueskytiledir = cwd + '/TileImages/BasicBlueSkyTile.png'

phystest = Entity(name="phystest")
phystest.addComponent(VisibleObject(spritedir=blueskytiledir))
phystest.addComponent(Physics(xvelocity = 0.5, yvelocity=0.001, gravity = 0.01))
sceneobj.addentity(phystest)

# tmap = Entity(name="tmap")
# tmapComponent = Tilemap(tiles= World1.Level1, Tileset= {'S' : blueskytiledir} )
# tmap.addComponent(tmapComponent)
# physComponent = Physics(xvelocity= 0.001, yvelocity= 0.001, gravity=1)
# tmap.addCbygomponent(physComponent)
# sceneobj.addentity(tmap)

# image = Entity(name="image")
# image.addComponent(Position(x=0, y=0))
# image.addComponent(VisibleObject(spritedir=cwd + '/TileImages/BasicBlueSkyTile.png'))
# sceneobj.addentity(image)