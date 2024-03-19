

import network
import espnow
import time

sta = network.WLAN(network.STA_IF)    # Enable station mode for ESP
sta.active(True)
sta.disconnect()        # Disconnect from last connected WiFi SSID

e = espnow.ESPNow()     # Enable ESP-NOW
e.active(True)

peer =  b'\x40\x91\x51\xfb\xe2\x30'#MAC address of peer's wifi interface
e.add_peer(peer)                     # add peer1 (receiver1)

                  # add peer2 (receiver2)

print("Starting...")            # Send to all peers

e.send(peer, "walk", True)     # send commands to pear 1
time.sleep_ms(2000)
e.send(peer, "walk", True)
time.sleep_ms(2000)