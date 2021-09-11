# Programa principal
from gl import Renderer, V3, _color
from obj import Texture
from shaders import *

import random

width = 1920
height = 1080

rend = Renderer(width, height)

rend.directional_light = V3(0,0,-1)

rend.background = Texture('models/desierto.bmp')

rend.glClearBackground()

rend.active_texture = Texture("models/alien.bmp")
rend.glLoadModel("models/alien.obj",
                 translate = V3(5,-3,-2),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

rend.active_texture = Texture('models/fance.bmp')
rend.glLoadModel('models/fence.obj',
                 translate =V3(-5,-3,-2),
                 scale = V3(3,3,3),
                 rotate = V3(0,0,-90))

rend.glLoadModel('models/militar.obj',
                 translate = V3(0,0,0),
                 scale =V3(2,2,2),
                 rotate = V3(0,0,0))

rend.active_texture = Texture('models/car.bmp')
rend.glLoadModel('models/car.obj',
                 translate = V3(0,0,0),
                 scale = V3(3,3,3),
                 rotate =V3(-45,0,0))



rend.glFinish("output.bmp")


