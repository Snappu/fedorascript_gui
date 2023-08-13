import os
from tkinter import *
from tkinter import messagebox

root = Tk ()
root.title("Fedorascript_GUI")
root.geometry('800x600')
root.resizable(width=False, height=False)

def click_button():
	os.system('chmod +x Fedoscript.sh')
	os.system('./Fedoscript.sh')
	os.system('chmod +x script_two.sh')
	os.system('./script_two.sh')
	root.destroy()
	messagebox.showinfo('good', 'Script started')
	termstop = input("Click enter to close...")

lb = Label(root, text="Start", font=("Aria Bolt", 20))
lb.pack(expand=True)

btn = Button(root, text="Start", command=click_button)
btn.pack(expand=True, ipadx=40, ipady=20)

root.mainloop()
