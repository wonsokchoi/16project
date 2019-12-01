from ctypes import *
import RPi.GPIO as GPIO

DISPLAY = [
    [0x42,0x42,0x42,0x42,0x42,0x42,0x24,0x18],#U
    [0x3C,0x22,0x22,0x3C,0x22,0x22,0x22,0x3C],#B
    [0x3C,0x42,0x40,0x40,0x40,0x40,0x42,0x3C],#C
    [0x3C,0x42,0x42,0x42,0x42,0x42,0x42,0x3C],#O
    [0x7C,0x40,0x40,0x7C,0x40,0x40,0x40,0x7C],#E
    [0x7C,0x40,0x40,0x7C,0x40,0x40,0x40,0x40],#F
    [0x44,0x44,0x44,0x7C,0x44,0x44,0x44,0x44],#H
    [0x7C,0x10,0x10,0x10,0x10,0x10,0x10,0x10],#T
    [0x24,0x28,0x30,0x20,0x30,0x28,0x24,0x24],#K
    [0x3C,0x22,0x22,0x22,0x3C,0x24,0x22,0x21],#R
]

SOURCE = [s for s in 'UBCOEFHTKR']
TARGET = [n for n in '0123456789']

# Matrix
class Matrix :
    def __init__(self, cs_pin=8):
        self.cs_pin = cs_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.cs_pin, GPIO.OUT)

        self.hspi = CDLL('./dev_hardware_SPI.so')
        self.init_spi()
        self.init_matrix()

    def init_spi(self):
        self.hspi.DEV_HARDWARE_SPI_begin("/dev/spidev0.0")
        self.hspi.DEV_HARDWARE_SPI_ChipSelect(3)

    def init_matrix(self):
        self.write(0x09,0x00,0x09,0x00)
        self.write(0x0a,0x03,0x0a,0x03)
        self.write(0x0b,0x07,0x0b,0x07)
        self.write(0x0c,0x01,0x0c,0x01)
        self.write(0x0f,0x00,0x0f,0x00)

    def writeByte(self, reg):
        GPIO.output(self.cs_pin, 0)
        self.hspi.DEV_SPI_WriteByte(reg)

    def write(self, address1, dat1, address2, dat2):
        GPIO.output(self.cs_pin, 0)
        self.writeByte(address1)
        self.writeByte(dat1)
        self.writeByte(address2)
        self.writeByte(dat2)
        GPIO.output(self.cs_pin, 1)

    def writeAlph(self, first="U", second="U"):
        global DISPLAY
        for j in range(1, 9):
            self.write(j, DISPLAY[SOURCE.index(second)][j-1],
                       j, DISPLAY[SOURCE.index(first)][j-1])

    def writeNumb(self, first=0, second=0) :
        global DISPLAY
        for j in range(1, 9):
            self.write(j, DISPLAY[second][j-1],
                       j, DISPLAY[first][j-1])



