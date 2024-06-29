import tkinter as tk
def file_inp(file,text):
        workfile=open(file)
        data=workfile.read()
        text.insert(tk.END,data)
