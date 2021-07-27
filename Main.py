
from gl import Renderer, V2, color
from numpy import sin, cos

import random

poli1 = [(165, 380),(185, 360),(180, 330),(207, 345),(233, 330),
           (230, 360),(250, 380),(220, 385),(205, 410),(193, 383)]

poli2 = [(321, 335),(288, 286),(339, 251),(374, 302)]

poli3 = [(377, 249),(411, 197),(436, 249)]

poli4 = [(413, 177),(448, 159),(502, 88),(553, 53),(535, 36),(676, 37),(660, 52),
(750, 145),(761, 179),(672, 192),(659, 214),(615, 214),(632, 230),(580, 230),
(597, 215),(552, 214),(517, 144),(466, 180)]

poli5 = [(682, 175),(708, 120),(735, 148),(739, 170)]

width = 960
height = 540

rend = Renderer(width, height)

for i in range (len(poli1)):
    rend.glLine(V2(poli1[i][0],poli1[i][1]),V2(poli1[(i + 1) % len(poli1)][0],poli1[(i + 1) % len(poli1)][1]))

#rend.glLoadModel("",V2(width/2,height/2),V2(100,100))

rend.glFinish("output.bmp")
