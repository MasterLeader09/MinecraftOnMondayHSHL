from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def positionPlayer():
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    return x, y, z