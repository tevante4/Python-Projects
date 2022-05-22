import tkinter as tk
from tkinter import *
from tkinter import messagebox

import webbrowser


# Function to open html file generated from writeHtmlFile() function
def openInBrowser():
    url = "step310_web_page_generator_assignment.html"
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)


# Function to create the html file (if it doesn't already exists) and overwrite its content with the htmlFileContent string below.
def writeHtmlFile(var_bodytext):
    f = open("step310_web_page_generator_assignment.html", "w")
    htmlFileContent = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Step310 Web Page Generator assignment</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>
                {}
            </h1>
        </body>
    </html>
    """.format(var_bodytext)
    f.write(htmlFileContent)
    f.close()
    #open and read the file after writing:
    f = open("step310_web_page_generator_assignment.html", "r")
    print(f.read())
    openInBrowser()


# Function to get the user's input in the entry from the Tkinter window.
def get_body_text():
    var_bodytext = txt_bodytext.get()
    writeHtmlFile(var_bodytext)


# Creates Tkinter window to ask for user's desired text for the web page's body.
master = tk.Tk()
lbl_bodytext = tk.Label(master, text='Body Text: ')
lbl_bodytext.grid(row=0, column=0, padx=(5,5), pady=(5,5), sticky=N+W)
txt_bodytext = tk.Entry(master, text='')
txt_bodytext.insert(10, 'Please type desired text here..')
txt_bodytext.grid(row=1, column=0, rowspan=2, columnspan=3, padx=(5,5), pady=(5,5), sticky=N+E+W)
btn_generate = tk.Button(master, width=25, height=2, text='Generate Web Page', command=get_body_text)
btn_generate.grid(row=4, column=0, padx=(5,5), pady=(5,5), sticky=W)
tk.mainloop()
