from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

#get position function
pos = mc.player.getPos()

#place block near you
x, y, z = mc.player.getPos()

#Make a GIANT BLOCK
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 1)