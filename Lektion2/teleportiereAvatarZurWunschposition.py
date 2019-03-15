from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x_Koordinate = int(input("Geben Sie eine X-Koordinate an: "))
y_Koordinate = int(input("Geben Sie eine Y-Koordinate an: "))
z_Koordinate = int(input("Geben Sie eine Z-Koordinate an: "))

mc.player.setPos(x_Koordinate, y_Koordinate, z_Koordinate)
