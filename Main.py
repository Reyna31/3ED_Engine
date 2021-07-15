
from gl import Renderer, V2, color
from numpy import sin, cos

width = 960
height = 540

rend = Renderer(width, height)

rend.glClearColor(0,0,0)
rend.glColor(0.2,0.3,0.5)

rend.glPoint(100,100)

rend.glFinish("output.bmp")
