from tkinter import *
from tkinter import ttk
import sys
sys.path.append('/tools')
import tools.db as db

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def main():
    ttk.Label(frm, text="Opa, bom dia").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=0)
    root.mainloop()

main()