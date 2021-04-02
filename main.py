import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# inpins = {
#      2:['\x00\x00\x01\x00',False] # Button 1
#     ,3:['\x00\x00\x02\x00',False] # Button 2
#     ,4:['\x00\x00\x04\x00',False] # Button 3
#     ,17:['\x00\x00\x08\x00',False] # Button 4
#     ,22:['\x00\x00\x10\x00',False] # Button 5
#     ,9:['\x00\x00\x20\x00',False] # Button 6
#     ,0:['\x00\x00\x40\x00',False] # Button 7
#     ,6:['\x00\x00\x80\x00',False] # Button 8 -> moves y axis to half
#     ,19:['\x00\x00\x00\x01',False] # Button 9
#     ,26:['\x00\x00\x00\x02',False] # Button 10
#     ,21:['\x00\x00\x00\x04',False] # Button 11
#     ,20:['\x00\x00\x00\x08',False] # Button 12
#     # ,15:['\x00\x00\x00\x10',False] # Button 13
#     # ,14:['\x00\x00\x00\x20',False] # Button 14
#     ,15:['\x00\x00\x00\x40',False] # Button 15
#     ,14:['\x00\x00\x00\x80',False]}# Button 16 -> triggers 2,7,8,16
inpins = {
     2:[ 1,False] # Button 1
    ,3:[ 2,False] # Button 2
    ,4:[ 3,False] # Button 3
    ,17:[4,False] # Button 4
    ,22:[5,False] # Button 5
    ,9:[ 6,False] # Button 6
    ,0:[ 7,False] # Button 7
    ,6:[ 8,False] # Button 8 -> moves y axis to half
    ,19:[9,False] # Button 9
    ,26:[10,False] # Button 10
    ,21:[11,False] # Button 11
    ,20:[12,False] # Button 12
    # ,1500',False] # Button 13
    # ,1400',False] # Button 14
    ,15:[15,False] # Button 15
    ,14:[16,False]}# Button 16 -> triggers 2,7,8,16

for k,v in inpins.items():
    inpins[k][0] = 1<<v[0]#int.from_bytes(v[0].encode(), 'big')
    GPIO.setup(k, GPIO.IN, GPIO.PUD_UP)


print(inpins)

import os, sys, time

def submit_action(action):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(action)
state = 0
while True:    
    sendclean = True
    old_state = state
    for k,v in inpins.items():
        if not GPIO.input(k): #Key is down
            if not v[1]:
                state |= v[0]
                #submit_action(v[0])
                print(state, " | ", hex(state))
                v[1] = True
                
            sendclean = False
            time.sleep(0.01)
        else:
            v[1] = False
            state &= v[0]^(2**16)
    if old_state!=state:
        submit_action(state.to_bytes(4, 'big'))
    # elif state!=0:
    #     submit_action(state.to_bytes(4, 'big'))