from tkinter import *
root=Tk()
root.geometry("400x400")
button=Button(root,text="ClickMe",fg="yellow")
button.pack()
button1=Button(root,text="ClickMe", state=DISABLED,fg="green")
button1.pack()
button2=Button(root,text="ClickMe",padx=50,fg="red",bg="black")
button2.pack()
button3=Button(root,text="ClickMe",padx=50,pady=50,state=DISABLED)
button3.pack()
root.mainloop()