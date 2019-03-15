from random import randint
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x_Koordinate = randint(-126, 126)
y_Koordinate = randint(-62, 62)
z_Koordinate = randint(-126, 126)

mc.player.setPos(x_Koordinate, y_Koordinate, z_Koordinate)
