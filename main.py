import RPi.GPIO as GPIO
NULL_CHAR = chr(0)
GPIO.setmode(GPIO.BCM)
inpins = {17:'\x00\x00\x01\x00'}
for k,v in inpins.items():
    GPIO.setup(k, GPIO.IN, GPIO.PUD_UP)

import os, sys, time
fd = open("/dev/hidg0", "rb+")

while True:
    for k,v in inpins.items():
        if not GPIO.input(17):
            fd.write(v.encode())
            time.sleep(0.05)
            fd.write('\x00\x00\x00\x00'.encode())
            fd.flush()