import tkinter as tk
from tkinter import ttk
import sys
sys.path.append('/tools')
import tools.db as db

mainfrm = tk.Frame()

# Classe de funções adicionais
class Funcs():
    def get_reagent(self, rid):
        db.get_reagent(rid)
        self.refresh_table()

    def return_reagent(self, rid, quantity):
        db.return_reagent(rid, quantity)
        self.refresh_table()
        
    def select_row(self, event):
        curItem = self.tv.focus()
        self.selected = self.tv.item(curItem)["values"]
        
    def refresh_table(self):
        for i in self.tv.get_children():
            self.tv.delete(i)
        
        for i in db.list_reagents():
            self.tv.insert(parent='', index=len(self.tv.get_children()), iid=len(self.tv.get_children()), text='', values=(
                i.id,
                i.name, 
                i.formula, 
                i.density, 
                i.quantity, 
                "Disponível" if i.state == "available" else "Indisponível",
            ))

# Classe que representa a aplicação
class Application(Funcs):
    def __init__(self):
        self.screen()
        self.frames()
        self.treeview()
        self.widgets()
        self.root.mainloop()

    def frames(self):
        self.mainfrm = tk.Frame(self.root, bd=4, bg="#ebf2ff", highlightbackground="#527aff", highlightthickness=3)
        self.mainfrm.place(relx=0.02, rely=0.02, relwidth=0.56, relheight=0.96)
        
        self.tvfrm = tk.Frame(self.root, bd=4, bg="#ebf2ff", highlightbackground="#527aff", highlightthickness=3)
        self.tvfrm.place(relx=0.60, rely=0.02, relwidth=0.38, relheight=0.96)

    def screen(self):
        self.root = tk.Tk()
        root = self.root
        root.geometry("1800x720")
        root.minsize(width=400, height=400)
        root.configure(background="#224c94")

    def widgets(self):
        # Botão para pegar (?) um reagente
        self.getBtn = tk.Button(self.mainfrm, text="Pegar", command=lambda: self.get_reagent(self.selected[0])) # Achar um termo/legenda melhor que "pegar"
        self.getBtn.place(relx=0.05, rely=0.1, relwidth=0.1, relheight=0.1)

        # Botão pra falar a quantidade de reagente devolvido
        self.returnEntry = tk.Entry(self.mainfrm)
        self.returnEntry.place(relx=0.175, rely=0.1, relwidth=0.1, relheight=0.1)

        # Botão para devolver um reagente
        self.returnBtn = tk.Button(self.mainfrm, text="Devolver", command=lambda: self.return_reagent(self.selected[0], float(self.returnEntry.get())))
        self.returnBtn.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)
        
    # Configuração da Treeview
    def treeview(self):
        # Cria as colunas da Treeview
        self.tv = ttk.Treeview(self.tvfrm)
        self.tv['columns'] = ('id', 'name', 'formula', 'density', 'quantity', 'state')
        self.tv["displaycolumns"] = ['name', 'formula', 'density', 'quantity', 'state'] 
        self.tv.column('#0', width=0, stretch=tk.NO)
        self.tv.column('id', width=0, stretch=tk.NO)
        self.tv.column('name', anchor=tk.CENTER, width=150)
        self.tv.column('formula', anchor=tk.CENTER, width=150)
        self.tv.column('density', anchor=tk.CENTER, width=50)
        self.tv.column('quantity', anchor=tk.CENTER, width=50)
        self.tv.column('state', anchor=tk.CENTER, width=100)

        # Adiciona os titulos às colunas
        self.tv.heading('#0', text='', anchor=tk.CENTER)
        self.tv.heading('id', text='', anchor=tk.CENTER)
        self.tv.heading('name', text='Nome', anchor=tk.CENTER)
        self.tv.heading('formula', text='Fórmula', anchor=tk.CENTER)
        self.tv.heading('density', text='Densidade (g/cm³)', anchor=tk.CENTER)
        self.tv.heading('quantity', text='Quantidade (kg)', anchor=tk.CENTER)
        self.tv.heading('state', text='Estado', anchor=tk.CENTER)
        self.tv.bind('<<TreeviewSelect>>', self.select_row)

        # Cria a Scroolbar
        self.scroll = tk.Scrollbar(self.mainfrm, orient='vertical')
        
        # Adiciona os reagentes como linha
        self.refresh_table()

        self.tv.place(relx=0, rely=0, relwidth=1, relheight=1)
        
Application()