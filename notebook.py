import ttkbootstrap as tb
import tkinter as tk
class Tabs:
    def display(self, window):
        my_notebook = tb.Notebook(window, bootstyle="info")
        my_notebook.place(x=0,y=730)
        tab1 = tb.Frame(my_notebook)
        tab2 = tb.Frame(my_notebook)
        tab3 = tb.Frame(my_notebook)
        my_text1 = tk.Text(tab1, width=180, height=7)
        my_text1.pack(pady=10, padx=10)
        my_text2 = tk.Text(tab2, width=180, height=7)
        my_text2.pack(pady=10, padx=10)
        my_text3 = tk.Text(tab3, width=180, height=7)
        my_text3.pack(pady=10, padx=10)
        my_notebook.add(tab1, text="Tab One")
        my_notebook.add(tab2, text="Tab Two")
        my_notebook.add(tab3, text="Tab Three")
