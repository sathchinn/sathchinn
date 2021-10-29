from tkinter import *
import pyttsx3
root = Tk()
def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)

    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(9, END)



my_entry = Entry(root, font=("Times New Roman", 32))
my_entry.pack(pady=20)

my_button = Button(root, text="Speak", command = talk)
my_button.pack(pady=20)

root.mainloop()