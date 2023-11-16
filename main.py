import tkinter as tk
from tkinter import ttk
import sys
sys.path.append('/tools')
import tools.db as db

root = tk.Tk()
style = ttk.Style()

class Application():
    
    def __init__(self):
        self.root = root
        self.style = style
        self.screen()
        self.frames()
        root.mainloop()
    
    def screen(self):
        root = self.root
        root.geometry("1800x720")
        root.minsize(width=400, height=400)
        root.configure(background="#224c94")
    
    def visuals(self):
        style = self.style
        style.configure("BW.TLabel", foreground="white", background="#224c94")

    def frames(self):
        self.frm = tk.Frame(root, bd=4, bg="#ebf2ff", highlightbackground="#527aff", highlightthickness=3)
        self.frm.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)

    def buttons(self):
        self.clean = tk.Button(self.frm)

Application()