from mcpi.minecraft import Minecraft
mc = Minecraft.create()

positionDesAvatars = mc.player.getPos()

x_Koordinate = positionDesAvatars.x
y_Koordinate = positionDesAvatars.y
z_Koordinate = positionDesAvatars.z