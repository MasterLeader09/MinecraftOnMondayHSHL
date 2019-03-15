from mcpi.minecraft import Minecraft
mc = Minecraft.create()

Dein_Name = input("Geben Sie hier Ihren Namen ein: ")

mc.postToChat("Hallo " + Dein_Name)
