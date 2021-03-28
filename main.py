import RPi.GPIO as GPIO
NULL_CHAR = chr(0)
GPIO.setmode(GPIO.BCM)
inpins = {17:'\x00\x00\x01\x00'}
for k,v in inpins.items():
    GPIO.setup(k, GPIO.IN, GPIO.PUD_UP)

import os, sys, time

def submit_action(action):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(action.encode())

while True:
    for k,v in inpins.items():
        if not GPIO.input(17):
            submit_action(v.encode())
            time.sleep(0.05)
            submit_action('\x00\x00\x00\x00'.encode())