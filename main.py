import pyautogui
import time
import queue
from PIL import Image, ImageDraw

img = Image.open("img.png")
time.sleep(5)
pos = pyautogui.position()
RED = (255,0,0)

def flood_fil(img, x,y,new_color):
    w = img.width
    h = img.height
    old_color = img.getpixel((x,y))
    q = queue.Queue()
    q.put((x,y))
    
    while not q.empty():
        x,y = q.get()
        if x<0 or x>=w or y<0 or y>=h or img.getpixel((x,y)) != old_color:
            continue
        else:
            img.putpixel((x,y), new_color)
            q.put((x+1, y))
            q.put((x-1, y))
            q.put((x, y+1))
            q.put((x, y-1))

    img.save("floodfill.png")        

flood_fil(img, pos.x, pos.y, RED)