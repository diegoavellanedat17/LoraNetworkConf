import pycom           # we need this module to control the LED
from network import WLAN

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'FOXO':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'jugodenaranja07'), timeout=5000)
        print('WLAN connection succeeded!')
        break