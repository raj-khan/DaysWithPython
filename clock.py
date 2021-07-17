from tkinter import *
from tkinter.ttk import *

from time import strftime

# root.title("Raj Clock") #this will be have a title
root = Tk()

# this will work like desktop widget
root.overrideredirect(1)

def time():
  string = strftime('%H:%M:%S %p')
  label.config(text=string)
  label.after(1000, time) # call time after 1 second


label = Label(root, font=("ds-digital", 80), background="black", foreground="yellow")
label.pack(anchor='center')
time()

mainloop()
