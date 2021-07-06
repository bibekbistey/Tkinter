from tkinter import *
top=Tk()
top.geometry("400x250")
def display():
    label3 = Button(top, text="Clickme", fg="blue", bg="black", )
    label3.pack(side=LEFT)
label = Label(top, text="My name is Bibek Bista",command=display)
label.pack()

top.mainloop()