button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
pin = machine.Pin(12, machine.Pin.OUT)
while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
	    pin.value(1)
        print('Button pressed!')
    elif not first and second:
	    pin.value(0)
        print('Button released!')	
