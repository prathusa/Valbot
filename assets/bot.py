import pyautogui as pag
from PIL import Image
import time


# scale = 2
# with Image.open('play.png') as im:
#     # im.thumbnail(size)
#     # im.resize((int(im.width*scale), int(im.height*scale)))
#     # print(im.size)
#     # im.save("play1.png", "PNG")
#     half = 1.3
#     out = im.resize( [int(half * s) for s in im.size], Image.ANTIALIAS)
#     print(out.size)
#     out.save("play1.png", "PNG")

time.sleep(3)
playButton = Image.open('assets/deathmatchN.png')

point = pag.locateOnScreen(playButton)
print(point)