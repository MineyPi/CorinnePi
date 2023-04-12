from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

#post to the chat
#mc.postToChat("Hello Corinne, my darling")

pos = mc.player.getPos()

#place block
x, y, z = mc.player.getPos()
#mc.setBlock(x, y, z, 53)
mc.setBlock(x, y+1, z+1, 17)
mc.setBlock(x, y+1, z+1, 17)
mc.setBlock(x, y+1, z+1, 17)

#teleport
x, y, z = mc.player.getPos()
mc.player.setPos(x, y+2, z+1)
