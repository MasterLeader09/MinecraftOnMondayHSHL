from mcpi.minecraft import Minecraft
mc = Minecraft.create()
golderz = 14
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

hoch = int(input("Bitte eine Hoehe eingeben: "))
wendepunkt = int(input("Nach wie vielen Bloecken soll die Richtung wechseln"))

zaehler = 0
richtung = 1

while zaehler < hoch:
    if richtung == 5:
        richtung -= 4
    
    if richtung == 1:
        mc.setBlock(x, y + zaehler, z, golderz)
        x += 1
    elif richtung == 2:
        mc.setBlock(x, y + zaehler, z, golderz)
        z += 1
    elif richtung == 3:
        mc.setBlock(x, y + zaehler, z, golderz)
        x -= 1
    elif richtung == 4:
        mc.setBlock(x, y + zaehler, z, golderz)
        z -= 1
    
    zaehler += 1
    if zaehler % wendepunkt == 0:
        richtung += 1