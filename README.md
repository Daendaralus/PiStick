# PiStick
Raspberry Pi Zero based fighting stick thingy

Inspired by https://github.com/milador/RaspberryPi-Joystick

Use https://github.com/milador/RaspberryPi-Joystick/tree/master/16_Buttons_Joystick "Software Installation" to get the USB gadget up and running.
Afterwards follow "Autostart", replacing WorkingDirectory and ExecStart paths to this main.py (can also throw bluetooth out)
Example: 
```
[Unit]
Description=PiStick start with systemd
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 -u main.py
WorkingDirectory=/home/pi/PiStick
Type=idle
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=pistick
User=pi
Group=pi

[Install]
WantedBy=multi-user.target
```
