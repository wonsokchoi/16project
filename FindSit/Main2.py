from camera import *
from matrix import *
from ocr import *
from sql import *

c = Camera()
o = OCR()
t = Translator()
s = SQL()

tablename = 'data_table'
seatnumber = '0'
building = "'Soongsil Univ'"

try :
    while True :
        c.take()
        raw_data = o.analyze()
        data = t.translate_alph(raw_data)
        value = t.join_to_digit(data)
        if value :
            s.update(tablename, value, seatnumber, building)
        else :
            s.update(tablename, '98', seatnumber, building)
            
except KeyboardInterrupt :
    GPIO.cleanup()
    print("Bye")

#s.select(tablename)
#s.delete(tablename, seatnumber, building)
#s.insert(tablename, seatnumber, building, value)
