from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
	positionSpieler = mc.player.getPos()
	x = positionSpieler.x
	y = positionSpieler.y
	z = positionSpieler.z
	mc.setBlock(x, y, z, 8)
