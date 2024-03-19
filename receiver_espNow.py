import network
import espnow

def espnow_rx():

    # A WLAN interface must be active to send()/recv()
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.disconnect()                # Disconnect from last connected WiFi SSID

    e = espnow.ESPNow()                  # Enable ESP-NOW
    e.active(True)

    peer = b'\x40\x91\x51\xfb\xe2\x30'   # MAC address of peer's wifi interface
    e.add_peer(peer)                     # Sender's MAC registration

    while True:
        host, msg = e.recv()
        if msg:                          # wait for message
            if msg == b'walk':           # decode message and translate
                print("walk")       # to the NyBoard's command
            elif msg == b'back':
               print("back")
            elif msg == b'stop':
                print("stop")

if __name__ == "__main__":
    espnow_rx()
    