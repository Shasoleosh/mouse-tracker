import win32gui, time, os, keyboard, colorsys
from win32api import GetSystemMetrics as scrSize
from PIL import Image, ImageDraw, ImageFont


count = 0

pos = win32gui.GetCursorPos()
lastpos = win32gui.GetCursorPos()

poss = []

image = Image.new("RGBA", (scrSize(0),scrSize(1)), (0,0,0,0))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", 25)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

while True:
    time.sleep(0.005)
    shift = keyboard.is_pressed('shift')
    ctrl = keyboard.is_pressed('ctrl')
    s = keyboard.is_pressed('s')

    lastpos = pos
    pos = win32gui.GetCursorPos()

    if ctrl and shift and s:
        break
    
    if lastpos != pos:
        count = count + 1
        le = abs((lastpos[0] + lastpos[1]) - (pos[0] + pos[1]))/1000

        if le < 0.2:
            color = le
        draw.line((lastpos,pos), fill=hsv2rgb(0.2-color,1,1), width=2)

        print(count)

draw.text((0,0), str(count) + ' points', fill=(0,0,0), font=font)
print('save image')

del draw
time_data = str(time.clock())
image.save("["+time_data+"]_line_story2.png", "PNG")
os.startfile("["+time_data+"]_line_story2.png")