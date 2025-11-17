from tkinter import *

root = Tk()
root.title(' scetchy login app(we wont hack your robox account>:)')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360)


lbl1 = Label(frame, text = "Full Username", bg='#3895D3', fg='white', width=12)
lbl2 = Label(frame, text = "Full amount off stuff u have", bg='#3895D3', fg='white', width=12)
lbl3 = Label(frame, text = "password", bg='#3895D3', fg='white', width=12)
name_entry = Entry(frame)
is_it_good_eunoph = Entry(frame)
password = Entry(frame, show="*")
def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongades for u getting hacked >:)"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg="#BEBEBE", fg= "black")

btn = Button(text= "Create account", command=display, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=20)
is_it_good_eunoph.place(x=150, y=20)
lbl3.place(x=20, y=20)
password.place(x=150, y=20)
btn.place(x=130, y=210)
textbox.place(y=250)



root.mainloop