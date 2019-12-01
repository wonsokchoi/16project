from camera import *
from matrix import *
from ocr import *
from sql import *

m = Matrix()
t = Translator()
print("Ready to display")
try :
    while True :
        raw = raw_input()
        if len(raw) == 2 :
            data = t.translate_numb(raw)
            print(data)
            m.writeAlph(data[0], data[1])
except KeyboardInterrupt :
    GPIO.cleanup()
    print("Bye")
