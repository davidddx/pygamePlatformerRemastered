from ECS.Scene import Scene
from ECS.Entity import Entity
from ECS.Physics import Position
from ECS.VisibleObject import VisibleObject
from gamecode.settings import true, false, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from debug.logger import logger
import os

cwd = os.getcwd()
sceneobj = Scene()

image = Entity(name="image")
image.addComponent(Position(x=0, y=0))
image.addComponent(VisibleObject(spritedir=cwd + '/TileImages/BasicBlueSkyTile.png'))
sceneobj.addentity(image)