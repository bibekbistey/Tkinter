from tkinter import *
root=Tk()
root.geometry("200x200")
e1=Entry(root,width=50,fg="red")
e1.pack()
def clickThis():
    textoutput="hello" +e1.get()
    mylabel = Label(root, text=textoutput)
    mylabel.pack()
    mybutton1=Button(root,text=textoutput)
    mybutton1.pack()
mybutton=Button(text="ClickMe",command=clickThis)
mybutton.pack()

root.mainloop()
