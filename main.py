#!/usr/bin/python
"""This program is made to simplify the process of requesting Google Bard 
responses for Etsy products. It take a standard AI derscriptor and returns
potential product titles, descriptions, and etsy tags."""

import tkinter as tk
from tkinter import *
from bardapi import Bard
import requests
from bardapi.constants import SESSION_HEADERS


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
    ai_title_textbox.insert('1.0', bard.get_answer("Please give me an Esty product title for " + descriptor_textbox.get("1.0",'end-1c'))['content'])
    
    print("Requesting a description...")
    ai_description_textbox.insert('1.0', bard.get_answer("Please give me an Esty product description for " + descriptor_textbox.get("1.0",'end-1c'))['content'])
    
    print("Requesting tags...")
    ai_tags_textbox.insert('1.0', bard.get_answer("Please give me 20 esty tags no more than 20 characters long in csv format for " + descriptor_textbox.get("1.0",'end-1c'))['content'])
    #ive me 20 esty tags no more than 20 characters long in csv format for
    #ai_tags_textbox.insert('1.0', bard.get_answer("Please provide me with 20 Etsy product tags appropriate for" + descriptor_textbox.get("1.0",'end-1c') + "product limiting them to 20 characters or less in csv format")['content'])

def save_tsv():
    #
    pass

root=tk.Tk()
root.title('sunshine-etsy-title-description-tags-generator')
root.resizable(1,1)
#root.columnconfigure(0, weight=3)
#root.columnconfigure(1, weight=3)
#root.columnconfigure(2, weight=3)
#root.rowconfigure(0, weight=1)

bard_cookie_1PSID_label = Label(root, text="Bard Cookie __Secure-1PSID")
bard_cookie_1PSID_label.grid(column=0, row=0, sticky=E, padx=5, pady=5)

bard_cookie_1PSID_textbox = Text(root, height = 1, width = 80)
bard_cookie_1PSID_textbox.grid(column=1, row=0, columnspan=2, sticky=W, padx=5, pady=5)

bard_cookie_1PSIDTS_label = Label(root, text="Bard Cookie __Secure-1PSIDTS")
bard_cookie_1PSIDTS_label.grid(column=0, row=1, sticky=E, padx=5, pady=5)

bard_cookie_1PSIDTS_textbox = Text(root, height = 1, width = 80)
bard_cookie_1PSIDTS_textbox.grid(column=1, row=1, columnspan=2, sticky=W, padx=5, pady=5)

bard_cookie_1PSIDCC_label = Label(root, text="Bard Cookie __Secure-1PSIDCC")
bard_cookie_1PSIDCC_label.grid(column=0, row=2, sticky=E, padx=5, pady=5)

bard_cookie_1PSIDCC_textbox = Text(root, height = 1, width = 80)
bard_cookie_1PSIDCC_textbox.grid(column=1, row=2, columnspan=2, sticky=W, padx=5, pady=5)


descriptor_label = Label(root, text="Input AI Descriptor")
descriptor_label.grid(column=0, row=3, sticky=E, padx=5, pady=5)

descriptor_textbox = Text(root, height = 1, width = 80)
descriptor_textbox.grid(column=1, row=3, columnspan=2, sticky=W, padx=5, pady=5)

ai_title_label = Label(root, text="AI Suggested Title")
ai_title_label.grid(column=0, row=4, sticky=W, padx=5, pady=5)

ai_title_textbox = Text(root, height = 20, width = 60)
ai_title_textbox.grid(column=0, row=5, columnspan=1, sticky=W, padx=5, pady=5)

ai_description_label = Label(root, text="AI Suggested Description")
ai_description_label.grid(column=1, row=4, sticky=W, padx=5, pady=5)

ai_description_textbox = Text(root, height = 20, width = 60)
ai_description_textbox.grid(column=1, row=5, columnspan=1, sticky=W, padx=5, pady=5)

ai_tags_label = Label(root, text="AI Suggested Tags")
ai_tags_label.grid(column=2, row=4, sticky=W, padx=5, pady=5)

ai_tags_textbox = Text(root, height = 20, width = 60)
ai_tags_textbox.grid(column=2, row=5, columnspan=1, sticky=W, padx=5, pady=5)

request_populate_button = Button(root, text="Request", command=get_everything)
request_populate_button.grid(column=0, row=6, sticky=W, padx=5, pady=5)

exit_button = Button(root, text="Exit", command = root.destroy) 
exit_button.grid(column=2, row=6, sticky=E, padx=5, pady=5)

# Extraniously helpful code
descriptor_textbox.insert('1.0', "A tshirt with a body building shark with big arms")


root.mainloop()