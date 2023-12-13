#!/usr/bin/python
"""This program is made to simplify the process of requesting Google Bard 
responses for Etsy products. It take a standard AI derscriptor and returns
potential product titles, descriptions, and etsy tags."""

import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfile
from bardapi import Bard
import requests
from bardapi.constants import SESSION_HEADERS

default_descriptor = "A tshirt with a body building shark with big arms"
default_ai_title_request = "Please give me an Esty product title of 100 and 140 characters for "
default_ai_description_request = "Please give me an Esty product description for "
default_ai_tags = "Please give me 20 Esty tags no more than 20 characters long in csv format for "

def get_everything():
    #Setup session and cookies
    _1PSID = bard_cookie_1PSID_textbox.get("1.0", 'end-1c')
    _1PSIDTS = bard_cookie_1PSIDTS_textbox.get("1.0", 'end-1c')
    _1PSIDCC = bard_cookie_1PSIDCC_textbox.get("1.0", 'end-1c')
    
    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", _1PSID)
    session.cookies.set("__Secure-1PSIDTS", _1PSIDTS)
    session.cookies.set("__Secure-1PSIDCC", _1PSIDCC)
    
    print("Initializing requests...")
    bard = Bard(token = bard_cookie_1PSID_textbox.get("1.0", 'end-1c'), session = session)
    
    print("Requesting a title...")
    ai_title_textbox.insert('1.0', bard.get_answer(ai_title_request_textbox.get("1.0",'end-1c') + descriptor_textbox.get("1.0",'end-1c'))['content'])
    
    print("Requesting a description...")
    ai_description_textbox.insert('1.0', bard.get_answer(ai_description_request_textbox.get("1.0",'end-1c') + descriptor_textbox.get("1.0",'end-1c'))['content'])
    
    print("Requesting tags...")
    ai_tags_textbox.insert('1.0', bard.get_answer(ai_tags_request_textbox.get("1.0",'end-1c') + descriptor_textbox.get("1.0",'end-1c'))['content'])
    
def save_file():
    print("Save file...")
    file = asksaveasfile(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
    file.write("Title:\n" + ai_title_textbox.get("1.0",'end-1c') + "\nDescription:\n" + ai_description_textbox.get("1.0",'end-1c') + "\nTags:\n" + ai_tags_textbox.get("1.0",'end-1c'))
    file.close

root=tk.Tk()
root.title('sunshine-etsy-title-description-tags-generator')
root.resizable(1,1)
# The following code makes the response text boxes automatically resize
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Cookie label and text boxes
bard_cookie_1PSID_label = Label(root, text="Bard Cookie __Secure-1PSID")
bard_cookie_1PSID_label.grid(column=0, row=0, sticky=E, padx=5, pady=5)

bard_cookie_1PSID_textbox = Text(root, height = 1, width = 80)
bard_cookie_1PSID_textbox.grid(column=1, row=0, columnspan=2, sticky="ew", padx=5, pady=5)

bard_cookie_1PSIDTS_label = Label(root, text="Bard Cookie __Secure-1PSIDTS")
bard_cookie_1PSIDTS_label.grid(column=0, row=1, sticky=E, padx=5, pady=5)

bard_cookie_1PSIDTS_textbox = Text(root, height = 1, width = 80)
bard_cookie_1PSIDTS_textbox.grid(column=1, row=1, columnspan=2, sticky="ew", padx=5, pady=5)

bard_cookie_1PSIDCC_label = Label(root, text="Bard Cookie __Secure-1PSIDCC")
bard_cookie_1PSIDCC_label.grid(column=0, row=2, sticky=E, padx=5, pady=5)

bard_cookie_1PSIDCC_textbox = Text(root, height = 1, width = 80)
bard_cookie_1PSIDCC_textbox.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5, pady=5)

# The AI inout descriptor label and text box
descriptor_label = Label(root, text="Input AI Descriptor")
descriptor_label.grid(column=0, row=3, sticky=E, padx=5, pady=5)

descriptor_textbox = Text(root, height = 1, width = 80)
descriptor_textbox.grid(column=1, row=3, columnspan=2, sticky=W, padx=5, pady=5)

# The response labels, default request, and response and text boxes
ai_title_label = Label(root, text="AI Suggested Title")
ai_title_label.grid(column=0, row=4, sticky=W, padx=5, pady=5)

ai_title_request_textbox = Text(root, height = 2, width = 60)
ai_title_request_textbox.grid(column=0, row=5, columnspan=1, sticky="ew", padx=5, pady=5)

ai_title_textbox = Text(root, height = 20, width = 60)
ai_title_textbox.grid(column=0, row=6, columnspan=1, sticky="nsew", padx=5, pady=5)

ai_description_label = Label(root, text="AI Suggested Description")
ai_description_label.grid(column=1, row=4, sticky=W, padx=5, pady=5)

ai_description_request_textbox = Text(root, height = 2, width = 60)
ai_description_request_textbox.grid(column=1, row=5, columnspan=1, sticky="ew", padx=5, pady=5)

ai_description_textbox = Text(root, height = 20, width = 60)
ai_description_textbox.grid(column=1, row=6, columnspan=1, sticky="nsew", padx=5, pady=5)

ai_tags_label = Label(root, text="AI Suggested Tags")
ai_tags_label.grid(column=2, row=4, sticky=W, padx=5, pady=5)

ai_tags_request_textbox = Text(root, height = 2, width = 60)
ai_tags_request_textbox.grid(column=2, row=5, columnspan=1, sticky="ew", padx=5, pady=5)

ai_tags_textbox = Text(root, height = 20, width = 60)
ai_tags_textbox.grid(column=2, row=6, columnspan=1, sticky="nsew", padx=5, pady=5)

# The request, save, and exit buttons
request_populate_button = Button(root, text="Request", command=get_everything)
request_populate_button.grid(column=0, row=7, sticky=W, padx=5, pady=5)

save_file_button = Button(root, text="Save File", command=save_file)
save_file_button.grid(column=1, row=7, sticky=W, padx=5, pady=5)

exit_button = Button(root, text="Exit", command = root.destroy) 
exit_button.grid(column=2, row=7, sticky=E, padx=5, pady=5)

# Extraniously helpful code
descriptor_textbox.insert('1.0', default_descriptor)
ai_title_request_textbox.insert('1.0', default_ai_title_request)
ai_description_request_textbox.insert('1.0', default_ai_description_request)
ai_tags_request_textbox.insert('1.0', default_ai_tags)

root.mainloop()