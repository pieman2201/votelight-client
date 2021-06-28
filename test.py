import board
import neopixel

pixel = neopixel.NeoPixel(board.D18, 1)

MAX_BRIGHTNESS = 255

while 1:
    for i in range(3):
        for v in range(MAX_BRIGHTNESS * 2 + 1):
            l = [0] * 3
            l[i] = MAX_BRIGHTNESS - abs(MAX_BRIGHTNESS - v)
            pixel[0] = l
