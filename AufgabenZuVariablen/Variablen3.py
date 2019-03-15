from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
	positionSpieler = mc.player.getPos()
	x = positionSpieler.x
	y = positionSpieler.y
	z = positionSpieler.z
	Blocktyp = mc.getBlock(x, y, z)
	if Blocktyp == 8:
		mc.postToChat("Der Spieler ist im Wasser")
	elif Blocktyp == 10:
		mc.postToChat("Der Spieler ist in der Lava")
	else:
		mc.postToChat("Der Spieler ist sicher")
