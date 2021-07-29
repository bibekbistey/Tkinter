from tkinter import *
root=Tk()
MODES=[
    ("cheese","very good"),
    ("burger","good"),
    ("Momo","Tastey"),
    ("Chicken","yummy"),
]
pizza=StringVar()
pizza.set("cheese")
for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    maLabel=Label(root,text=value).pack()


myButton=Button(root,text="Click",command=lambda:clicked(pizza.get())).pack()
root.mainloop()