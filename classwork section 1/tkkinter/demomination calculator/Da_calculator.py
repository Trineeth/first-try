from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('demonation calculator')
root.configure(bg= 'light blue')
root.geometry('650x400')


upload = Image.open("app_img.jpg")

upload = upload.resize(300, 300)
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')

label1 = Label(root,
               text="Hey user! welcome to money cal",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    msgBox = messagebox.showinfo(
        "Alert! do u want to show money count?")
    if msgBox == 'ok':
        topwin()

button1 = Button(root,
                 text="Lets get started",
                 command=msg,
                 bg='brown',
                 fg='white')
button1.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top.title("money cal")
    top.configure(bg='light grey')
    top.geometry("600x350+500+50")

    label = Label(top, text="enter total amount here", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="here are the number of noted of each money thing", bg= 'light grey')

    l1 = Label(top, text="100", bg='light grey')
    l2 = Label(top, text="10", bg='light grey')
    l3 = Label(top, text="1", bg='light grey')
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note100 = amount // 100
            amount %= 100
            note10 = amount // 10
            amount %= 10
            note1 = amount // 1
            amount %= 1

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note100))
            t2.insert(END, str(note10))
            t3.insert(END, str(note1))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    btn = Button(top, text='calculate', command=calculator, bg='brown', fg='white')

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=170)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200   )
    t2.place(x=270, y=230   )
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()


