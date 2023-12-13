#!/usr/bin/python
"""This program is made to simplify the process of requesting Google Bard 
responses for Etsy products. It take a standard AI derscriptor and returns
potential product titles, descriptions, and etsy tags."""

import tkinter as tk
from tkinter import *
from bardapi import Bard

def get_everything():
    get_title
    #
    print(descriptor_textbox.get("1.0",'end-1c'))
    print("get everything")
    pass

def get_title():
    #bard = Bard(token = bard_cookie_textbox.get("1.0", 'end-1c'))
    #bard.get_answer(descriptor_textbox.get("1.0",'end-1c'), "")['content']
    #
    pass

def get_description():
    #
    pass

def get_tags():
    #
    pass

def save_tsv():
    #
    pass

root=tk.Tk()
root.title('sunshine-etsy-title-description-tags-generator')
root.resizable(1,1)
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=3)
root.rowconfigure(0, weight=1)

bard_cookie_label = Label(root, text="Bard Cookie __Secure-1PSID")
bard_cookie_label.grid(column=0, row=0, sticky=E, padx=5, pady=5)

bard_cookie_textbox = Text(root, height = 1, width = 80)
bard_cookie_textbox.grid(column=1, row=0, columnspan=2, sticky=W, padx=5, pady=5)

descriptor_label = Label(root, text="Input AI Descriptor")
descriptor_label.grid(column=0, row=1, sticky=E, padx=5, pady=5)

descriptor_textbox = Text(root, height = 1, width = 80)
descriptor_textbox.grid(column=1, row=1, columnspan=2, sticky=W, padx=5, pady=5)

ai_title_label = Label(root, text="AI Suggested Title")
ai_title_label.grid(column=0, row=2, sticky=W, padx=5, pady=5)

ai_title_textbox = Text(root, height = 20, width = 40)
ai_title_textbox.grid(column=0, row=3, columnspan=1, sticky=W, padx=5, pady=5)

ai_description_label = Label(root, text="AI Suggested Description")
ai_description_label.grid(column=1, row=2, sticky=W, padx=5, pady=5)

ai_description_textbox = Text(root, height = 20, width = 40)
ai_description_textbox.grid(column=1, row=3, columnspan=1, sticky=W, padx=5, pady=5)

ai_tags_label = Label(root, text="AI Suggested Tags")
ai_tags_label.grid(column=2, row=2, sticky=W, padx=5, pady=5)

ai_tags_textbox = Text(root, height = 20, width = 40)
ai_tags_textbox.grid(column=2, row=3, columnspan=1, sticky=W, padx=5, pady=5)

request_populate_button = Button(root, text="Request", command=get_everything)
request_populate_button.grid(column=0, row=4, sticky=W, padx=5, pady=5)

exit_button = Button(root, text="Exit", command = root.destroy) 
exit_button.grid(column=2, row=4, sticky=E, padx=5, pady=5)

root.mainloop()