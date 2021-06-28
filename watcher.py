import board
import neopixel
import time

pixel = neopixel.NeoPixel(board.D18, 1)
last = None

while True:
    try:
        time.sleep(0.05)
        with open('colorfile') as f:
            new = eval(f.read())
            if new != last:
                last = new
                pixel[0] = last
    except KeyboardInterrupt as e:
        raise e
    except:
        pass
