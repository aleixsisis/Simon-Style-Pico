from machine import Pin, ADC

ldr = ADC(Pin(26))
led1 = (Pin(20))

while True:

    #read the ldr and print
    lightValue = ldr.read_u16()
    print (lightValue)
    if ldr lightValue 