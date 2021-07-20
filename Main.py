
from gl import Renderer, V2, color
from numpy import sin, cos

import random

width = 960
height = 540

rend = Renderer(width, height)

rend.glClearColor(1,1,1)
rend.glColor(1,1,1)

#Cuadrado
rend.glLine(V2(50,50),V2(100,50))
rend.glLine(V2(50,50),V2(50,100))
rend.glLine(V2(100,50),V2(100,100))
rend.glLine(V2(50,100),V2(100,100))

#Pentagono
rend.glLine(V2(50,200),V2(50,250))
rend.glLine(V2(50,200),V2(100,175))
rend.glLine(V2(50,250),V2(100,275))
rend.glLine(V2(100,175),V2(125,225))
rend.glLine(V2(100,275),V2(125,225))

#Triangulo
rend.glLine(V2(150,50),V2(200,50))
rend.glLine(V2(150,50),V2(150,100))
rend.glLine(V2(150,100),V2(200,50))

#Hexagono
rend.glLine(V2(200,400),V2(250,400))
rend.glLine(V2(250,400),V2(275,450))
rend.glLine(V2(275,450),V2(250,500))
rend.glLine(V2(250,500),V2(200,500))
rend.glLine(V2(200,500),V2(175,450))
rend.glLine(V2(175,450),V2(200,400))



rend.glFinish("output.bmp")
