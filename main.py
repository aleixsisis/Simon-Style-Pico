from machine import Pin, PWM
from time import sleep
import random
from piezoNotes import *

# PINS
green_led = Pin(15, Pin.OUT)
red_led = Pin(14, Pin.OUT)
blue_led = Pin(13, Pin.OUT)
yellow_led = Pin(12, Pin.OUT)

# BUTTONS
green_button = Pin(19, Pin.IN)
red_button = Pin(18, Pin.IN)
blue_button = Pin(17, Pin.IN)
yellow_button = Pin(16, Pin.IN)
start_button = Pin(20, Pin.IN)

LEDS = [green_led, red_led, blue_led, yellow_led]
BUTTONS = [green_button, red_button, blue_button, yellow_button]

# Define pitches for each color
color_notes = {
    green_led: "C5",  
    red_led: "D4",    
    blue_led: "E3",   
    yellow_led: "F2"  
}

# Initialize game sequence

sequence = []
user_sequence = []
game_started = False
game_over = False

# PIEZO
buzzer = PWM(Pin(11))

def PlayNote(note, duration):
    buzzer.freq(notes[note])
    buzzer.duty_u16(1000)
    sleep(duration)
    Stop()  

def Stop():
    buzzer.duty_u16(0)  
    for led in LEDS:
        led.off()

def CHOICE():
    return random.choice(LEDS)

def BEGINGAME():
    global sequence, user_sequence, game_started, game_over
    Stop()  
    sequence = []
    user_sequence = []
    game_started = True
    game_over = False
    AddToSequence()

def AddToSequence():
    global sequence
    sequence.append(CHOICE())
    ShowSequence()

def ShowSequence():
    Stop()
    for led in sequence:
        led.on()
        PlayNote(color_notes[led], 0.4)  
        sleep(0.4)
        Stop()  
        sleep(0.2)
    GetUserInput()

def GetUserInput():
    global user_sequence
    user_sequence = []
    while len(user_sequence) < len(sequence):
        for i, button in enumerate(BUTTONS):
            if button.value() == True:
                LED = LEDS[i]
                LED.on()
                PlayNote(color_notes[LED], 0.4)
                user_sequence.append(LED)
                sleep(0.4)
                Stop()
                sleep(0.2)
                break
        sleep(0.1)
    CheckUserSequence()
num = 0
def CheckUserSequence():
    global sequence, user_sequence, game_started, game_over
    if user_sequence == sequence:
<<<<<<< HEAD
        print(f"Correct!")
        AddToSequence()
    else:
        print("Incorrect. Game Over!")
        game_over = True
=======
        
        print(f"Correct! Sequence is now ")
        AddToSequence()
    else:
        print("Incorrect. Game Over!")
>>>>>>> f361ed6906bf51e462d9f6d2eb4e8003cf7f4522
        red_led.on()
        green_led.on()
        blue_led.on()
        yellow_led.on()
<<<<<<< HEAD
        PlayNote("E3", 0.5) 
        sleep(0.5)
        Stop()
        sleep(0.2)
=======
        PlayNote("E3", 0.5)
        sleep(.5)
        Stop()
        sleep(0.2)
        
>>>>>>> f361ed6906bf51e462d9f6d2eb4e8003cf7f4522
        red_led.on()
        green_led.on()
        blue_led.on()
        yellow_led.on()
<<<<<<< HEAD
        PlayNote("E3", 0.5) 
        sleep(0.5)
=======
        PlayNote("E3", 0.5)
        sleep(.5)
        
>>>>>>> f361ed6906bf51e462d9f6d2eb4e8003cf7f4522
        Stop()
        game_started = False

def BUTTONTEST():
    global game_started, game_over
    while True:
        if start_button.value() == True:
            if not game_started or game_over:
                print('Starting Game')
                BEGINGAME()
                sleep(1)
        sleep(0.1)  

BUTTONTEST()
