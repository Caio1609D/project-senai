import tkinter as tk
from tkinter import ttk
import sys
sys.path.append('/tools')
import tools.db as db

root = tk.Tk()
style = ttk.Style()

# Classe pra guardar as funções da aplicação
class Funcs():

    # Responsável por puxar os reagentes do db e transformar em tabela
    def refresh_table(self):
        for i in db.list_reagents():
            self.tv.insert(parent='', index=0, iid=0, text='', values=(
                i.name, 
                i.formula, 
                i.density, 
                i.quantity, 
                "Disponível" if i.state == "available" else "Indisponível"
            ))

    def select_row(self, event):
        curItem = self.tv.focus()
        self.selected = self.tv.item(curItem)["values"]
        print(self.selected)


# Classe que repersenta a nossa aplicação
class Application(Funcs):
    
    def __init__(self):
        self.root = root
        self.style = style
        self.selected = None
        self.screen()
        self.frames()
        self.treeview()
        root.mainloop()
    
    # Configuração da tela
    def screen(self):
        root = self.root
        root.geometry("1800x720")
        root.minsize(width=400, height=400)
        root.configure(background="#224c94")
    
    def visuals(self):
        style = self.style
        style.configure("BW.TLabel", foreground="white", background="#224c94")

    # Configuração dos Frames internos
    def frames(self):
        self.frm = tk.Frame(root, bd=4, bg="#ebf2ff", highlightbackground="#527aff", highlightthickness=3)
        self.frm.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)

    def widgets(self):
        self.cleanBtn = tk.Button(self.frm)

    # Configuração da Treeview
    def treeview(self):
        # Cria as colunas da Treeview
        self.tv = ttk.Treeview(self.frm)
        self.tv['columns'] = ('Name', 'Formula', 'Density', 'Quantity', 'State')
        self.tv.column('#0', width=0, stretch=tk.NO)
        self.tv.column('Name', anchor=tk.CENTER, width=150)
        self.tv.column('Formula', anchor=tk.CENTER, width=150)
        self.tv.column('Density', anchor=tk.CENTER, width=50)
        self.tv.column('Quantity', anchor=tk.CENTER, width=50)
        self.tv.column('State', anchor=tk.CENTER, width=100)

        # Adiciona os titulos às colunas
        self.tv.heading('#0', text='', anchor=tk.CENTER)
        self.tv.heading('Name', text='Nome', anchor=tk.CENTER)
        self.tv.heading('Formula', text='Fórmula', anchor=tk.CENTER)
        self.tv.heading('Density', text='Densidade', anchor=tk.CENTER)
        self.tv.heading('Quantity', text='Quantidade', anchor=tk.CENTER)
        self.tv.heading('State', text='Estado', anchor=tk.CENTER)
        self.tv.bind('<<TreeviewSelect>>', self.select_row)

        # Cria a Scroolbar
        self.scroll = tk.Scrollbar(self.frm, orient='vertical')
        
        # Adiciona os reagentes como linha
        self.refresh_table()

        self.tv.place(relx=0, rely=0, relwidth=1, relheight=1)

Application()