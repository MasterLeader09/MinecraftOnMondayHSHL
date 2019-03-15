import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

unterbrechung = 0.1
diamant = 57
gold = 41

def positionGeaendert():
	xAlt, yAlt, zAlt = positionSpieler()
	time.sleep(unterbrechung)
	xNeu, yNeu, zNeu = positionSpieler()
	if xAlt != xNeu or yAlt != yNeu or zAlt != zNeu:
		return True
	else:
		return False

def positionSpieler():
	posSpieler = mc.player.getTilePos()
	x = posSpieler.x
	y = posSpieler.y
	z = posSpieler.z
	return x, y, z

Baustein = 41

while True:
	x, y, z = positionSpieler()
	if positionGeaendert():
		if Baustein == 41:
			Baustein = 57
		else:
			Baustein = 41
	mc.setBlock(x, y - 1, z, Baustein)
	#time.sleep(unterbrechung)
