import random

from tkinter import *

window = Tk()

window.title("Friendship Calculator")

window.geometry("385x385")

# Functions


def friendship_generator():
    friendship = ["They're not very compatible ", "They ight", "They're close friends", "Best friends"]
    justin = random.choices(friendship)
    label.set(justin)


# This creates the text field


# Label
title = Label(text="Whose friendship would you like to calculate?:")
title.grid(column=0, row=0)

title2 = Label(text="Enter the first person's name here:")
title2.grid(column=0, row=1)

title3 = Label(text="Enter the second person's name here:")
title3.grid(column=0, row=2)


# Entry field
entry_field1 = Entry()
entry_field1.grid(column=1, row=1)

entry_field2 = Entry()
entry_field2.grid(column=1, row=2)


# Button
button1 = Button(text="Calculate", command=friendship_generator)
button1.grid(column=0, row=4)

# Result
label = StringVar()
label.set('')
label_box = Label(window, textvariable=label)
label_box.grid(row=3, column=1)

window.mainloop()

