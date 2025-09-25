import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("i am goingb to unalive your toys, its alive right?")
window.geometry('350x200')
window.configure(background='light blue')

def openNewWindow():
	newWindow = tk.Toplevel(window)
	newWindow.title("New Window")
	newWindow.geometry("200x100")
	lbl = tk.Label(newWindow, text="This is a new window")
	lbl.grid(column=0, row=0)
	btn = tk.Button(newWindow, text="Close", command=newWindow.destroy)
	btn.grid(column=1, row=0)

open_btn = tk.Button(window, text="Open New Window", command=openNewWindow)
open_btn.pack(pady=20)

window.mainloop()