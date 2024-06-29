import tkinter as tk
from tkinter import font
class SRBox:
        def display(self,master):
            master.geometry('600x100')
            master.title("Search and Replace")
            master.resizable(False,False) #makes the window non resizable
            tk.Label(master, text="Enter the sequence to be found").grid(row=0)
            tk.Label(master, text="Enter the sequence to replace it with").grid(row=1)
            self.e1 = tk.Entry(master) #Entry box1
            self.e2 = tk.Entry(master) #Entry box2
            self.e1.grid(row=0, column=1)
            self.e2.grid(row=1, column=1)    
        def retrieve(self):
            first=self.e1.get()
            second=self.e2.get()
            return first,second #Returns the text from Entry Boxes 
