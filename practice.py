import turtle as trtl
import random as ran
import tkinter as tk
from tkinter import messagebox

# Create a root window (it can stay hidden)
root = tk.Tk()
root.withdraw()

  # Hide the root window

# Display a message box
def write_letter(x,y,color,letter):
    t.penup()
    t.goto(x,y)
    t.pencolor(color)
    t.write(' '.join(letter), font = ('Arial', 80, 'normal'))


# Set up the screen
sc = trtl.Screen()
sc_height = 800
sc_width = 600
sc.setup(width=sc_width, height=sc_height)
# Set up list and guess count
puzzle = [["_", "_", "_", "_", "_"],["_", "_", "_", "_", "_"],["_", "_", "_", "_", "_"],["_", "_", "_", "_", "_"],["_", "_", "_", "_", "_"],["_", "_", "_", "_", "_"]]
currentGuessCount = 0
canvas = trtl.getcanvas()


# Set up words list
words = []
used_letters = []
word_bank = open("five_letters.txt")
for line in word_bank:
    words.append(line[:-1])
word_bank.close()
wordle_word = ran.choice(words)
word_letters = list(wordle_word)
print(wordle_word)
# Starting position for the first letter
x = -200
y = 300
spacing = 90

# Set up the turtle
t = trtl.Turtle()
t.penup()
# t.hideturtle()
t.speed(0)

# The word to guess

for i in range(6):
    t.penup()
    t.goto(x,y)
    t.write(' '.join(puzzle[i]), font = ('Arial', 80, 'normal'))
    y -= 125
x = -172
y = -340
for i in range(6):
    for i in range(5):
        canvas.create_rectangle(x - 42 ,y - 70 ,x + 42, y + 40, width = 2.5)
        x += spacing
    y+= 125
    x = -172



# Get the user's guess
y = 300
x = -200
while currentGuessCount <= 5:
    try:
        guess = sc.textinput("Word?", "Word")
        letters = list(guess)
        if len(guess) != 5:
            raise ValueError
        elif guess not in words:
            raise ValueError
        # if guess == wordle_word:
        #         write_letter(x,y,"green",letters)
        #         break
            
        else:
            for i in range(len(letters)):
                if letters[i] in ['m','w']:
                    x -= 15
                if letters[i] == word_letters[i]:
                    write_letter(x,y,'green',letters[i])  # Correct letter in correct position
                elif letters[i] in word_letters and puzzle[currentGuessCount].count(letters[i]) < word_letters.count(letters[i]):                    
                    write_letter(x,y,'yellow',letters[i])  # Correct letter but wrong position
                else:
                    write_letter(x,y,'black',letters[i])
                puzzle[currentGuessCount][i] = guess[i]
                if letters[i] in ['m','w']:
                    x += 15
                x += spacing   # Incorrect letter
                print(puzzle[currentGuessCount].count(letters[i]))
                print(puzzle)
            if puzzle[currentGuessCount] == word_letters:
                break
        currentGuessCount += 1
        x = -200
        y -= 125

            
    except ValueError as e:
        messagebox.showinfo("Information", 'Must be a word from the dictionary that is 5 letters long!')

# Set up the spacing between letters
# Loop through each letter in the guess and print it with the correct color


    # Move to the next position and write the letter
  # Move x to the right for the next letter


# Keeps the window open until you click on it
sc.mainloop()

