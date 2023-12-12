#!/usr/bin/python
"""This program is made to simplify the process of requesting Google Bard 
responses for Etsy products. It take a standard AI derscriptor and returns
potential product titles, descriptions, and etsy tags."""

import tkinter as tk
from tkinter import *

root=tk.Tk()
root.title('sunshine-etsy-title-description-tags-generator')
root.resizable(1,1)
root.columnconfigure(0, weight = 3)
root.columnconfigure(1, weight = 6)

bard_cookie_label = Label(root, text="Bard Cookie")
bard_cookie_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

bard_cookie_textbox = Text(root)
bard_cookie_textbox.grid(column=2, row=0, sticky=W, padx=5, pady=5)

exitButton = Button(root, text = "Exit", command = root.destroy) 
exitButton.grid(column = 2, row = 1, sticky = E, padx=5, pady=5)

root.mainloop()