import machine
import time
vuelta = 1
while vuelta < 6:  
  print("Vuelta " +str(vuelta))
  vuelta = vuelta + 1
  ledR.on()
  time.sleep(0.5)
  ledR.off()
  time.sleep(0.5)
  ledG.on()
  time.sleep(0.5)
  ledG.off()
  time.sleep(0.5)
  ledB.on()
  time.sleep(0.5)
  ledB.off()
  time.sleep(0.5)
