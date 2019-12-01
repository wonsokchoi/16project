import picamera
import cv2
import time

class Camera :
    def __init__(self, path='/home/pi/Desktop/FindSit/img/', name='capture.png'):
        self.filepath = path
        self.filename = name
        self.camera = picamera.PiCamera()

    def take(self) :
        self.camera.start_preview()
        self.camera.capture(self.filepath+self.filename)
        self.camera.stop_preview()

    def test(self):
        self.camera.start_preview()
        time.sleep(1000)
        self.camera.stop_preview()        

    def show(self) :
        img = cv2.imread(self.filepath+self.filename, cv2.IMREAD_COLOR)
        cv2.imshow('CAPTURED IMAGE', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
