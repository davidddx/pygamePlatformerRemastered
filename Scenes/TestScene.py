from ECS.Scene import Scene
from ECS.Entity import Entity
from ECS.Physics import Position
from ECS.VisibleObject import VisibleObject
from gamecode.settings import true, false, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from debug.logger import logger
import os

cwd = os.getcwd()
sceneobj = Scene()
background = Entity(name= 'background')
for i in range(int(SCREEN_WIDTH / TILE_SIZE) + 1):
    for j in range(int(SCREEN_HEIGHT / TILE_SIZE) + 1):
        background.addComponent(component=VisibleObject(cwd + '/TileImages/BasicBlueSkyTile.png'))
        background.addComponent(component=Position(x=i, y=j))

sceneobj.addentity(background)