from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randint

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

for i in range(20):
	divisor = randint(-2, 2)
	mc.setBlock(x + 10 / divisor, y, z, 41)
