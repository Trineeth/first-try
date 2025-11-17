from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("practice thingy")

def topwin():
    top = Toplevel()
    top.geometry("180x180")
    top.title("toplevel")
    l2 = Label(top, text = "Virus detectud, shutting down window")
    l2.pack()

    top.mainloop()

l = Label(root, text = "this is root window")
btn = Button(root, text = "click here to open a window", command = topwin)

l.pack()
btn.pack()

root.mainloop()