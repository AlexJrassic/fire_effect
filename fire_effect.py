from blinkt import set_brightness, set_pixel, show
import random
import time

colors = [
        [255, 0, 0],    # red
        [255, 255, 0],   # yellow
        [255, 165, 0]   # orange
]

while True:
    brightness = random.random()
    color = random.choice(colors)
    pixel = random.randint(0, 7)
    
    r = color[0]
    g = color[1]
    b = color[2]

    set_brightness(brightness)
    set_pixel(pixel, r, g, b)
    show()
    time.sleep(0.05)
