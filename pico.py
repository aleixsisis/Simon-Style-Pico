from machine import Pin, PWM
from time import sleep
from piezoNotes import *
import random

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
LED_NAMES = ["green", "red", "blue", "yellow"]

# PIEZO
def PlayNote(note, duration):
    buzzer.freq(notes[note])
    buzzer.duty_u16(1000)
    sleep(duration)
    
def Stop():
    buzzer.duty_u16(0)
    for led in LEDS:
        led.off()

buzzer = PWM(Pin(11))
buzzer.duty_u16(0)

# Global Variables
sequence = []
player_sequence = []
game_started = False

def show_sequence():
    for led in sequence:
        led.on()
        PlayNote("E1", 0.4)  # You may need to change the note based on LED
        sleep(0.5)
        led.off()
        sleep(0.5)

def get_led_from_button(button):
    if button == green_button:
        return green_led
    elif button == red_button:
        return red_led
    elif button == blue_button:
        return blue_led
    elif button == yellow_button:
        return yellow_led

def check_player_input():
    global player_sequence
    for led in player_sequence:
        if not led in sequence:
            return False
    return True

def handle_button_press():
    if start_button.value() == True:
        start_game()

    for button in BUTTONS:
        if button.value() == True:
            led = get_led_from_button(button)
            led.on()
            PlayNote("E1", 0.4)
            player_sequence.append(led)
            led.off()
            sleep(0.5)  # Debounce delay

def start_game():
    global sequence, player_sequence, game_started
    if not game_started:
        sequence = []
        player_sequence = []
        for _ in range(5):  # Start with a sequence of length 5
            led = random.choice(LEDS)
            sequence.append(led)
        game_started = True
        show_sequence()

def main():
    while True:
        handle_button_press()
        if len(player_sequence) == len(sequence):
            if check_player_input():
                print("Correct sequence!")
                # Add next step or end game logic
            else:
                print("Wrong sequence! Game over.")
                game_started = False
                Stop()
            player_sequence = []
        sleep(0.1)  # Avoid busy-wait loop

if __name__ == "__main__":
    main()
