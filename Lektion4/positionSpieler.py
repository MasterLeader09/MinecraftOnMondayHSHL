from mcpi.minecraft import Minecraft
mc = Minecraft.create()

positionSpieler = mc.player.getPos()
x = positionSpieler.x
y = positionSpieler.y
z = positionSpieler.z

mc.postToChat("X: " + str(x) + " Y: " + str(y) + " Z: " + str(z))
