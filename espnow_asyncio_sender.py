import network
import aioespnow
import asyncio
from machine import Pin ,ADC
import random
network.WLAN(network.STA_IF).active(True)


esp=aioespnow.AIOESPNow()
esp.active(True)
peer=b'\x48\x3f\xda\x53\xf5\x74'
esp.add_peer(peer)

#Creer un evenement pour controler l'execution du coroutine
execute_event=asyncio.Event()

# Definir la fonction pour enabler le system
def enable_system():
    execute_event.set()
    
    
    
# Definir la fonction pour disabler notre systeme
def disable_system():
        execute_event.clear()
async def send_button_state(espnow): 
    last_state=True
    while True:
        if execute_event.is_set(): # si l'evenement est enabled
            state=1
            if state !=0:
                message="allumer les donnees"
                print("les donnees sont envoyer")
                await espnow.asend(peer,message)
            else:
                message="ledOff"
                print(f"Sending command :{message}")
                await espnow.asend(peer,message)
            last_state=state
        await asyncio.sleep_ms(10) # a ajuster
# Async courotine pour lire et envoyer les donnees  potentiometer 
async def send_potentiometer(espnow):
    while True:
        if execute_event.is_set():
            potentiometer_value= random.randint(100,300)
            message=f"potentiometer :{potentiometer_value}"
            espnow.send(peer,message)
        await asyncio.sleep_ms(200)
# definir un courotine  sur l'evenement de click sur le button
async def enable_disable_listner():
        enable_disabled_pin=1
        while True:
            if  enable_disabled_pin:
                print("Button clicked,toggling courotine execution")
                if execute_event.is_set():
                    disable_system()
                else :
                    enable_system()
                await asyncio.sleep_ms(500)
            await asyncio.sleep_ms(100)
            
async def main(espnow):
    await asyncio.gather(enable_disable_listner(),send_button_state(espnow),send_potentiometer(espnow))
    
asyncio.run(main(esp))
        

                
        
