# Import libraries, tkinter for gui, gtts to convert text into audio, and playsound to play audio files
from fileinput import filename
import os
from tkinter import *
from turtle import bgcolor
from gtts import gTTS
from playsound import playsound

# Initialize window
window = Tk()
# Set window dimensions
window.geometry("300x300")
#set window background color
window.configure(bg='blue')
#set window title
window.title("Text To Audio Mini App")

text_string = StringVar()
Label(window, text = "Please enter your text.", font = 'arial 15 bold', bg = 'blue').pack()

entry_field = Entry(window, textvariable = text_string, width='43')
entry_field.place(x=20,y=100)

# function to convert text to audio 
def Text_to_Audio():
    message = entry_field.get()
    audio = gTTS(text = message, lang="en")
    filename = "Text_to_Audio.mp3"
    audio.save(filename)
    playsound(filename)
    os.remove(filename)

# function to exit from app, quit the program by stopping the mainloo()
def Exit():
    window.destroy()

# function to reset the entry field
def Reset():
    text_string.set("")

# define buttons
Button(window, text = "Play", font = "arial 15 bold", command = Text_to_Audio, width = '4').place(x=25, y=140)

Button(window, font = 'arial 15 bold', text = 'Exit', width ='4', command = Exit).place(x=100, y=140)

Button(window, font = 'arial 15 bold', text = 'Reset', width='4', command = Reset).place(x=175, y=140)


window.mainloop()
