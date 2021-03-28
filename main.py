import RPi.GPIO as GPIO
NULL_CHAR = chr(0)
GPIO.setmode(GPIO.BCM)
inpins = {17:['\x00\x00\x01\x00',False]}
for k,v in inpins.items():
    GPIO.setup(k, GPIO.IN, GPIO.PUD_UP)

import os, sys, time

def submit_action(action):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(action.encode())

while True:
    for k,v in inpins.items():
        if not GPIO.input(k): #Key is down
            if not v[1]:
                submit_action(v.encode())
                v[1] = True
            time.sleep(0.01)
            
        else:
            v[1] = False
            submit_action('\x00\x00\x00\x00'.encode())