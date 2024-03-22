import network
import aioespnow
import asyncio
import random

# A WLAN interface must be active to send()/recv()
network.WLAN(network.STA_IF).active(True)

esp = aioespnow.AIOESPNow()  # Returns AIOESPNow enhanced with async support
esp.active(True)
peer = b'x!\x84\xc68\xb0'
esp.add_peer(peer)


debounce_delay = 50  # Adjust this value to your needs (milliseconds)


async def send_button_state(espnow):
    last_state = 1
    while True:
        state = 1
        if state ==1:
            await asyncio.sleep_ms(debounce_delay)
            state = 1
            if state ==1 :
                if state == 1:
                    message = "ledOn"
                    print(f"Sending command : {message}")
                    await espnow.asend(peer, message)
                else:
                    message = "ledOff"
                    print(f"Sending command : {message}")
                    await espnow.asend(peer, message)
                last_state = state
        await asyncio.sleep_ms(10)  
        


# Async function for reading and sending potentiometer data
async def send_potentiometer_data(espnow):
    while True:
        potentiometer_value = random.randint(200,500)
        message = f"potentiometer:{potentiometer_value}"
        print("j'envoi les donnees ")
        espnow.send(peer, message)
        await asyncio.sleep(1)  # Send every 1 second
        
        
async def main(espnow):
    await asyncio.gather(send_button_state(espnow), send_potentiometer_data(espnow))
        
        
asyncio.run(main(esp))