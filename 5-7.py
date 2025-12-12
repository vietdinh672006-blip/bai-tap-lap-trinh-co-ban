# import the modules
import tkinter
import random
# list of possible colour.
colours = ['Red','Blue','Green','Pink','Black',
'Yellow','Orange','White','Purple','Brown']
score = 0
# the game time left, initially 30 seconds.
timeleft = 30

# *** NEW GLOBAL VARIABLE TO HOLD THE CORRECT ANSWER'S COLOUR ***
correct_colour = ''

# function that will start the game.
def startGame(event):
    if timeleft == 30:
        # start the countdown timer.
        countdown()
    # run the function to choose the next colour.
    nextColour()

# Function to choose and
# display the next colour.
def nextColour():
    global score
    global timeleft
    global correct_colour # Use the new global variable

    # if a game is currently in play
    if timeleft > 0:
        # make the text entry box active.
        e.focus_set()
        
        # *** CORRECTED LOGIC: Check input against the PREVIOUS correct_colour ***
        # The first time nextColour() runs (from startGame), correct_colour is empty, so we skip the check.
        if correct_colour != '':
            if e.get().lower() == correct_colour.lower():
                score += 1
        
        # clear the text entry box.
        e.delete(0, tkinter.END)
        
        # 1. Shuffle the list
        random.shuffle(colours)
        
        # 2. Select the color for the text (colours[1]) and the word for the text (colours[0])
        # And importantly, store the correct answer (the color) before changing the label
        correct_colour = colours[1]

        # 3. Change the label configuration
        label.config(fg = str(colours[1]), text = str(colours[0]))
        
        # update the score.
        scoreLabel.config(text = "Score: " + str(score))

# Countdown timer function
def countdown():
    global timeleft
    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1
        # update the time left label
        timeLabel.config(text = "Time left: " + str(timeleft))
        # run the function again after 1 second.
        timeLabel.after(1000, countdown)
    else:
        # Game over when time runs out
        label.config(text="Time's Up!", fg="red")

# Driver Code
# create a GUI window
root = tkinter.Tk()
# set the title
root.title("COLORGAME")
# set the size
root.geometry("375x200")
# add an instructions label
instructions = tkinter.Label(root, text = "Type in the **colour**"
" of the words, and not the word text!",
font = ('Helvetica', 12))
instructions.pack()
# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",
font = ('Helvetica', 12))
scoreLabel.pack()
# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " +
str(timeleft), font = ('Helvetica', 12))
timeLabel.pack()
# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()
# add a text entry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
# set focus on the entry box
e.focus_set()
# start the GUI
root.mainloop()
