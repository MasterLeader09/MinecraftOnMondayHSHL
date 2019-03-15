from mcpi.minecraft import Minecraft
mc = Minecraft.create()

positionDesSpielers = mc.player.getPos()
x = positionDesSpielers.x
y = positionDesSpielers.y
z = positionDesSpielers.z

hoehe = int(input("Wie hoch soll die Treppe sein: "))

zaehler = 0
while zaehler < hoehe:
    mc.setBlock(x + zaehler, y + zaehler, z)