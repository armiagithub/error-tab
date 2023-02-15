import tkinter.messagebox
a=0
Howmani = input('How mani?: ')
Howmani=int(Howmani)
title = input('title?: ')
message = input('message?: ')
while a<Howmani:
    tkinter.messagebox.showerror(title,message)
    a=a+1