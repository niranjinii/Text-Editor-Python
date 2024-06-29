import tkinter as tk
import ttkbootstrap as tb

class WordCounter(tk.Frame):
    def __init__(self, master,text_area):
        super().__init__(master) #super returns an object that represents parent class. It's a method displaying inheritance.
        self.text_area = text_area
        self.meter = tb.Meter(self, metertype="semi", amountused=0, interactive=False, bootstyle='info', subtext='Word Count')
        self.meter.pack()
        text_area.bind("<KeyRelease>", self.update_meter)
    def update_meter(self, event):
        text = self.text_area.get("1.0", "end-1c")
        self.meter.configure(amountused= len(text.split()))
