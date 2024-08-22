from machine import Pin, PWM, time_pulse_us
from time import sleep

#PINS
green_led = Pin(15, Pin.OUT)
red_led = Pin(14, Pin.OUT)
blue_led = Pin(13, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)

green_button = Pin(19, Pin.IN)
red_button = Pin(18, Pin.IN)
blue_button = Pin(17, Pin.IN)
yellow_button = Pin(16, Pin.IN)
while True:
    if green_button.value() == True:
        print ("Button is Pressed")
        green_led.on()
    if red_button.value() == True:
        print ("Button is Pressed")
        red_led.on()
    if blue_button.value() == True:
        blue_led.on()
        print ("Button is Pressed")
    if yellow_button.value() == True:
        print ("Button is Pressed")
        yellow_led.on()
    

    else:
        print ("Button is not pressed")
        green_led.off()
        red_led.off()
        blue_led.off()
        yellow_led.off()


while True:
    green_led.on()
    red_led.on()
    blue_led.on()
    yellow_led.on()

