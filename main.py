import RPi.GPIO as GPIO
NULL_CHAR = chr(0)
GPIO.setmode(GPIO.BCM)
inpins = {17:"a"}
for k,v in inpins.items():
    GPIO.setup(k, GPIO.IN, GPIO.PUD_UP)

import os, sys
fd = os.open("/dev/hidg0", 'rb+')
bytesWritten = os.write(fd, bytes([252, 8]))
print('bytes written: ' + str(bytesWritten))
while True:
    for k,v in inpins.items():
        if not GPIO.input(17):
            fd.write((NULL_CHAR*2+chr(4)+NULL_CHAR*5).encode())
            fd.write((NULL_CHAR*8).encode())