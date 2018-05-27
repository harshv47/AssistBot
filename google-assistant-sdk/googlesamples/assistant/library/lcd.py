import time
import RPi.GPIO as GPIO
from RPLCD import CharLCD
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=22, pin_e=18, pins_data=[16,11,12,15])

while True:
    lcd.write_string(u"Hello world!")
    time.sleep(1)
    lcd.clear()
    time.sleep(1)