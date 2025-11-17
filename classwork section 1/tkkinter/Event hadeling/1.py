from tkinter import *

window = Tk()
window.title("event handler")
window.geometry("750x850")

def handle_keypress(event):
    """print the charicter accosiated to the key pressed"""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked")

button = Button(text="Click me!", width=50, height=10)
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()