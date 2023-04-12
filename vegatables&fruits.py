from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

#get position function
pos = mc.player.getPos()

#place block near you
x, y, z = mc.player.getPos()

#create vegatbles and fruits near us
#mc.setBlock(x, y, z+1, 103)
#mc.setBlock(x, y, z+2,  83)

#Make a Flower Garden
mc.setBlocks(x+1, y+1, z+1, x+11, y, z+11, 37)

# make Melon garden
#mc.setBlocks(x+1, y+1, z+1, x+11, y, z+11, 103)