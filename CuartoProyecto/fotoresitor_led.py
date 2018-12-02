from machine import Pin,PWM,ADC
led=Pin(12)
led.on()
adc=ADC(0)
pwm=PWM(led)
pwm.freq(60)
while True:
   pwm.duty(adc.read())
