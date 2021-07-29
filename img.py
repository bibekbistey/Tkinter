from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title('image')

root.iconbitmap('calc.ico')

my_image=ImageTk.PhotoImage(Image.open('bibek.jpg'))
my_label=Label(image=my_image)
my_label.pack()

root.mainloop()
