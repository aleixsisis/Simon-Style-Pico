from machine import Pin, PWM
from time import sleep
import random
from piezoNotes import *

class SimonGame:
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

    # Define pitches for each colour
    colour_notes = {
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

    def PlayNote(self, note, duration):
        self.buzzer.freq(notes[note])
        self.buzzer.duty_u16(1000)
        sleep(duration)
        self.Stop()  

    def Stop(self):
        self.buzzer.duty_u16(0)  
        for led in self.LEDS:
            led.off()

    def CHOICE(self):
        return random.choice(self.LEDS)

    def BEGINGAME(self):
        self.Stop()  
        self.sequence = []
        self.user_sequence = []
        self.game_started = True
        self.game_over = False
        self.AddToSequence()

    def AddToSequence(self):
        self.sequence.append(self.CHOICE())
        self.ShowSequence()

    def ShowSequence(self):
        self.Stop()
        for led in self.sequence:
            led.on()
            self.PlayNote(self.colour_notes[led], 0.4)  
            sleep(0.4)
            self.Stop()  
            sleep(0.2)
        self.GetUserInput()

    def GetUserInput(self):
        self.user_sequence = []
        while len(self.user_sequence) < len(self.sequence):
            for i, button in enumerate(self.BUTTONS):
                if button.value() == True:
                    LED = self.LEDS[i]
                    LED.on()
                    self.PlayNote(self.colour_notes[LED], 0.4)
                    self.user_sequence.append(LED)
                    sleep(0.4)
                    self.Stop()
                    sleep(0.2)
                    break
            sleep(0.1)
        self.CheckUserSequence()

    def CheckUserSequence(self):
        if self.user_sequence == self.sequence:
            print(f"Correct!")
            self.AddToSequence()
        else:
            print("Incorrect. Game Over!")
            self.game_over = True
            self.red_led.on()
            self.green_led.on()
            self.blue_led.on()
            self.yellow_led.on()
            self.PlayNote("E3", 0.5) 
            sleep(0.5)
            self.Stop()
            sleep(0.2)
            self.red_led.on()
            self.green_led.on()
            self.blue_led.on()
            self.yellow_led.on()
            self.PlayNote("E3", 0.5) 
            sleep(0.5)
            self.Stop()
            self.game_started = False

    def PLAYGAME(self):
        while True:
            if self.start_button.value() == True:
                if not self.game_started or self.game_over:
                    print('Starting Game')
                    self.BEGINGAME()
                    sleep(1)
            sleep(0.1)  

game = SimonGame()
game.PLAYGAME()

