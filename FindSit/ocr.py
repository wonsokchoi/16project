import pytesseract
import cv2
from matrix import SOURCE, TARGET

#Tesseract
class OCR :
    def __init__(self, path='/home/pi/Desktop/FindSit/img/', name='capture.png'):
        self.filepath = path
        self.filename = name

    def analyze(self, path=None, name=None, blur=4):
        if path == None or name == None :
            img = cv2.imread(self.filepath + self.filename, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (480, 360))

            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            for i in range(blur) : img = cv2.blur(img, (20, 20))
            img = cv2.bitwise_not(img)

            data = pytesseract.image_to_string(img, config='-l eng --oem 3 --psm 13')
            print("OCR Result : " + data)
            return data
    
class Translator :
    def translate_alph(self, word):
        global SOURCE, TARGET
        result = []
        for s in word :
            if s in SOURCE :
                result.append(TARGET[SOURCE.index(s.upper())])
        return result

    def translate_numb(self, word):
        global SOURCE, TARGET
        result = []
        for s in word :
            if s in TARGET :
                result.append(SOURCE[TARGET.index(s)])
        return result

    def join_to_digit(self, strl) :
        try :
            return int("".join(str(strl)))
        except :
            return None
