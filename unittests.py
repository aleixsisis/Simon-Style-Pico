from gamecode import SimonGame
from time import sleep 

game = SimonGame()

#--------------------------------------------------------------------------
#Play Tone Tests
#1. Does the tone play for 0.5 seconds?
#2. Are the tones differentiated? 
 
print ("Testing Blue Tone Playing")
game.PlayNote("E3", 0.5) 
print ("Testing Green Tone Playing: ")
game.PlayNote("C5", 0.5)
print ("Testing Red Tone Playing: ")
game.PlayNote("D4", 0.5)
print ("Testing Yellow Tone Playing: ")
game.PlayNote("F2", 0.5)

#---------------------------------------------------------------------------
#Play LED Tests
#1. Does each colour led turn on? 
#2. Does each colour led turn off?

print ("Testing Blue LED Playing: ")
game.blue_led.on()
sleep(0.2)
game.blue_led.off()
print ("Testing Green LED Playing: ")
game.green_led.on()
sleep(0.2)
game.green_led.off()
print ("Testing Red LED Playing: ")
game.red_led.on()
sleep(0.2)
game.red_led.off()
print ("Testing Yellow LED Playing: ")
game.yellow_led.on()
sleep(0.2)
game.yellow_led.off()

#---------------------------------------------------------------------------
#Play Buttons Tests
#1. Does each button for each colour turn on?
#2. Does each button work in syncrhonisation with the Piezo?

print ("Press a Button to test Button input.")
game.GetUserInput()
print (f"The Button that has been pressed is {game.user_sequence}")

#----------------------------------------------------------------------------
#Stop Functions Test
#1. Does the stop function work to turn off an LED?
game.red_led.on()
print ("The red LED has been turned on and will be for 2 seconds.")
sleep(2)
game.Stop()
print ("The red LED has stopped function.")

#----------------------------------------------------------------------------
#Random Sequences Test
#Can the pico generate random sequences?
print ("The Pico is now generating 4 random choices for the user.")
game.AddToSequence()
sleep(0.2)
game.AddToSequence()
sleep(0.2)
game.AddToSequence()
sleep(0.2)
game.AddToSequence()
sleep(0.2)
game.Stop()
print ("The generated sequence is complete. The above 4 numbers are the sequence.")

#----------------------------------------------------------------------------
#Printing LED Choice Test
print ("Printing the chosen button.")
print(game.CHOICE())
print ("The button you pressed has been displayed in the terminal.")

#----------------------------------------------------------------------------
#Begin Game Test
#1. Test to begin the begin game program.
print ("The BEGINGAME test will now begin.")
game.BEGINGAME()
print ("The BEGINGAME test has ended.")
#----------------------------------------------------------------------------
#Main Game Loop Test (BUTTON TEST)
#1. Test to run the entire game loop.
print ("The main game loop will now begin.")
game.PLAYGAME()