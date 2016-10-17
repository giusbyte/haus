import RPi.GPIO as GPIO
import smbus
import time
import os

bus = smbus.SMBus(1)
address = 0x20 #Bus Address
reg_mode = 0x00
bank = 0x12 #Bank A

isTriggerAlarm = False
alarmBeep = False
ledOn = False

#set up the port expander
bus.write_byte_data(address, reg_mode, 0xff)

def sensor():
        v = bus.read_byte_data(address, bank)
        return v

#set up GPIO 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

while True:
    if sensor() & 1:
        isTriggerAlarm = False
        alarmBeep = False
        GPIO.output(17,False)
        ledOn = False
    else:
        isTriggerAlarm = True
        
    if isTriggerAlarm:
        if not(ledOn):
            GPIO.output(17,True)
            ledOn = True
        if not(alarmBeep):
            os.system("mpg123 -q beep-08b.mp3 &")
            time.sleep(0.2)
            os.system("mpg123 -q beep-08b.mp3 &")
            alarmBeep = True
    time.sleep(0.5)
