import board
import neopixel

pixel = neopixel.NeoPixel(board.D18, 1)
pixel[0] = [0,0,0]
