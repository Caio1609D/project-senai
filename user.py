import tkinter as tk
from tkinter import ttk
import sys
sys.path.append('/tools')
import tools.db as db

mainfrm = tk.Frame()

# Classe de funções adicionais
class Funcs():
    def get_reagent(self, rid):
        db.get_reagent(rid, "Sim")
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
        self.get_label = tk.Label(self.mainfrm, text="Pegar Reagente", font=('bold'), bg="#ebf2ff")
        self.getBtn = tk.Button(self.mainfrm, text="Pegar", command=lambda: self.get_reagent(self.selected[0])) # Achar um termo/legenda melhor que "pegar"
        self.get_label.place(relx=0.05, rely=0.15, relwidth=0.16, relheight=0.07)
        self.getBtn.place(relx=0.05, rely=0.2, relwidth=0.1, relheight=0.05)

        # Botão pra falar a quantidade de reagente devolvido
        self.return_label = tk.Label(self.mainfrm, text="Devolver Reagente", font=('bold'), bg="#ebf2ff")
        self.returnEntry = tk.Entry(self.mainfrm)
        self.return_label.place(relx=0.05, rely=0.35, relwidth=0.2, relheight=0.05)
        self.returnEntry.place(relx=0.05, rely=0.4, relwidth=0.1, relheight=0.05)

        # Botão para devolver um reagente
        self.returnBtn = tk.Button(self.mainfrm, text="Devolver", command=lambda: self.return_reagent(self.selected[0], float(self.returnEntry.get())))
        self.returnBtn.place(relx=0.16, rely=0.4, relwidth=0.1, relheight=0.05)
        
        self.title_label = tk.Label(self.mainfrm, text="Usar Reagentes", font=('', 20), bg="#ebf2ff")
        self.text_label = tk.Label(self.mainfrm, text="Nessa parte, você pode pegar registrar o uso de reagentes do estoque.\nUse os botões abaixo para pegar e devolver reagentes e informe a massa do reagente no momento da devolução", bg="#ebf2ff")

        self.title_label.place(relx=0.05, rely=0.025, relheight=0.05, relwidth=0.9)
        self.text_label.place(relx=0.05, rely=0.10, relheight=0.05, relwidth=0.9)

        
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