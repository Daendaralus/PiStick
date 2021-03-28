import RPi.GPIO as GPIO
NULL_CHAR = chr(0)
GPIO.setmode(GPIO.BCM)
inpins = {
     2:['\x00\x00\x01\x00',False] # Button 1
    ,3:['\x00\x00\x02\x00',False] # Button 2
    ,4:['\x00\x00\x04\x00',False] # Button 3
    ,17:['\x00\x00\x08\x00',False] # Button 4
    ,22:['\x00\x00\x10\x00',False] # Button 5
    ,9:['\x00\x00\x20\x00',False] # Button 6
    ,0:['\x00\x00\x40\x00',False] # Button 7
    ,6:['\x00\x00\x80\x00',False] # Button 8
    ,19:['\x00\x00\x00\x01',False] # Button 9
    ,26:['\x00\x00\x00\x02',False] # Button 10
    ,21:['\x00\x00\x00\x04',False] # Button 11
    ,20:['\x00\x00\x00\x08',False] # Button 12
    # ,15:['\x00\x00\x00\x10',False] # Button 13
    # ,14:['\x00\x00\x00\x20',False] # Button 14
    ,15:['\x00\x00\x00\x40',False] # Button 15
    ,14:['\x00\x00\x00\x80',False]}# Button 16

for k,v in inpins.items():
    GPIO.setup(k, GPIO.IN, GPIO.PUD_UP)
    v[0] = int.from_bytes(v[0].encode(), 'big')

import os, sys, time

def submit_action(action):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(action)

while True:
    state = 0
    for k,v in inpins.items():
        if not GPIO.input(k): #Key is down
            if not v[1]:
                state |= v[0]
                #submit_action(v[0])
                v[1] = True
            time.sleep(0.01)
        else:
            v[1] = False
    submit_action(state.to_bytes(4, 'big'))