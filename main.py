from machine import Pin, PWM, time_pulse_us
from time import sleep
import random
from piezoNotes import *

#PINS
green_led = Pin(15, Pin.OUT)
red_led = Pin(14, Pin.OUT)
blue_led = Pin(13, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)


#BUTTONS
green_button = Pin(19, Pin.IN)
red_button = Pin(18, Pin.IN)
blue_button = Pin(17, Pin.IN)
yellow_button = Pin(16, Pin.IN)
start_button = Pin(20, Pin.IN)

LEDS = (green_led, red_led, blue_led, yellow_led)

LIST = []
#PIEZO 
def PlayNote(note, duration):
    buzzer.freq(notes[note])
    buzzer.duty_u16(1000)
    sleep(duration)
    
def Stop():
    buzzer.duty_u16(0)
    green_led.off()
    red_led.off()
    blue_led.off()
    yellow_led.off()

buzzer = PWM (Pin(11))

bluenoise = PlayNote("E6", 0.4)

    
buzzer.duty_u16(0)
def BUTTONTEST():
    while True:
        if green_button.value() == True:
            print ("Button is Pressed")
            green_led.on()
            PlayNote("E1", 0.4)
            
        if red_button.value() == True:
            print ("Button is Pressed")
            red_led.on()
            PlayNote("F2", 0.4)

        if blue_button.value() == True:
            blue_led.on()
            print ("Button is Pressed")
            PlayNote("E2", 0.4)

        if yellow_button.value() == True:
            print ("Button is Pressed")
            yellow_led.on()
            PlayNote("CS2", 0.4)
        if start_button.value() == True:
            print ('ye')
        

        else:
            print ("Button is not pressed")
            green_led.off()
            red_led.off()
            blue_led.off()
            yellow_led.off()
            Stop()


def EVERYTHINGTEST():
    while True:
        green_led.on()
        PlayNote("E1", 0.4)
        red_led.on()
        PlayNote("F2", 0.4)
        blue_led.on()
        PlayNote("E2", 0.4)
        yellow_led.on()
        PlayNote("CS2", 0.4)
        sleep(5)
        Stop()

def CHOICE():

    return random.choice(LEDS)
def BEGINGAME():
    led = CHOICE()
    led.on()
    LIST.append(f"{led}")
# yellow_button.value() == True and LEDS == yellow_led:
#    print("yes")
if start_button.value() == True:
    BEGINGAME()
while True:
    print (f"{LIST}")

