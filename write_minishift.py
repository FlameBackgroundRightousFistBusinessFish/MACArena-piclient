import sys
import minishift
import time

#Minishift details
width = 16
vid, pid = 0x04d8, 0xf517

ms = minishift.Minishift(minishift.MCP2210Interface(vid, pid), width)

canvas = minishift.Canvas()

if (len(sys.argv) > 1):
    text = sys.argv[1]


canvas.write_text(0,text)
for slice in canvas.scroll():
    ms.update(slice)
    time.sleep(0.05)
