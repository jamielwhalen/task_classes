from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showerror('Window Title', 'fact')

root.bell()
if tkinter.messagebox.askokcancel("question", 'silly faces?', icon = 'warning'):

    print ("yes")



root.mainloop()