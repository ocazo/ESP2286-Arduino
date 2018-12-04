from machine import Pin
import time
ledR=Pin(15,Pin.OUT)  # Rojo
ledG=Pin(12,Pin.OUT)  # Verde
ledB=Pin(13,Pin.OUT)  # Azul
while True:
    ledR.on()
    time.sleep(0.1)
    ledR.off()
    time.sleep(0.1)
	ledG.on()
    time.sleep(0.1)
    ledG.off()
    time.sleep(0.1)
	ledB.on()
    time.sleep(0.1)
    ledB.off()
    time.sleep(0.1)
