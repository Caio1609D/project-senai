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

    def select_row(self, event):
        curItem = self.tv.focus()
        self.selected = self.tv.item(curItem)["values"]

    def get_reagent(self, rid):
        db.get_reagent(rid)
        self.refresh_table()

    def return_reagent(self, rid, quantity):
        db.return_reagent(rid, quantity)
        self.refresh_table()

    def login(self, user, password):
        self.logwin.destroy()
        self.root.deiconify()

    def add_reagent(self, name, formula, density, quantity):
        db.add_reagent(name, formula, density, quantity)
        self.refresh_table()


# Classe que repersenta a nossa aplicação
class Application(Funcs):
    
    def __init__(self):
        self.root = root
        self.style = style
        self.selected = None
        self.screen()
        self.frames()
        self.treeview()
        self.widgets()
        self.login_window()
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

    # Função de Login
    def login_window(self):
        # Cria a janela de login
        self.logwin = tk.Toplevel(root)
        
        # Desabilita temporáriamente a root
        self.root.withdraw()

        # Configura a janela de login
        self.logwin.geometry("600x240")
        self.logwin.title("Login")
        self.logwin.configure(background="#224c94")
        
        # Criação dos Widgets de Login
        self.user_label = tk.Label(self.logwin, text="Usuário:")
        self.pass_label = tk.Label(self.logwin, text="Senha:")
        
        self.user_entry = tk.Entry(self.logwin)
        self.pass_entry = tk.Entry(self.logwin, show="*")

        self.logBtn = tk.Button(self.logwin, text="Enviar", command=lambda: self.login(self.user_entry.get(), self.pass_entry.get()))
        
        # Dando um Place em tudo
        self.user_label.place(x=10, y=10, height=36)
        self.user_entry.place(x=10, y=51, width=200, height=36)

        self.pass_label.place(x=10, y=92, height=36)
        self.pass_entry.place(x=10, y=133, width=200, height=36)

        self.logBtn.place(x=10, y=174, width=100, height=36)
        
        self.logwin.mainloop()

    # Configuração dos Frames internos
    def frames(self):
        self.frm1 = tk.Frame(self.root, bd=4, bg="#ebf2ff", highlightbackground="#527aff", highlightthickness=3)
        self.frm1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48)

        self.frm2 = tk.Frame(self.root, bd=4, bg="#ebf2ff", highlightbackground="#527aff", highlightthickness=3)
        self.frm2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.48)

    def widgets(self):
        frm2 = self.frm2

        # Widgets para adicionar reagentes
        self.name_label = tk.Label(frm2, text="Nome")
        self.name_entry = tk.Entry(frm2)

        self.formula_label = tk.Label(frm2, text="Formula")
        self.formula_entry = tk.Entry(frm2)

        self.density_label = tk.Label(frm2, text="Densidade (g/cm³)")
        self.density_entry = tk.Entry(frm2)

        self.quantity_label = tk.Label(frm2, text="Quantidade (kg)") # Paleativo (só enquanto não temos a balança)
        self.quantity_entry = tk.Entry(frm2)

        self.addBtn = tk.Button(frm2, text="Adicionar Reagente", command=lambda: 
            self.add_reagent(
                self.name_entry.get(), 
                self.formula_entry.get(), 
                self.density_entry.get(), 
                self.quantity_entry.get()
            )
        )

        # Dando um place nisso tudo
        self.name_label.place(relx=0.05, rely=0.05, relheight=0.09, relwidth=0.19)
        self.formula_label.place(relx=0.25, rely=0.05, relheight=0.09, relwidth=0.19)
        self.density_label.place(relx=0.45, rely=0.05, relheight=0.09, relwidth=0.19)
        self.quantity_label.place(relx=0.65, rely=0.05, relheight=0.09, relwidth=0.19)

        self.name_entry.place(relx=0.05, rely=0.15, relheight=0.09, relwidth=0.19)
        self.formula_entry.place(relx=0.25, rely=0.15, relheight=0.09, relwidth=0.19)
        self.density_entry.place(relx=0.45, rely=0.15, relheight=0.09, relwidth=0.19)
        self.quantity_entry.place(relx=0.65, rely=0.15, relheight=0.09, relwidth=0.19)

        self.addBtn.place(relx=0.35, rely=0.25, relheight=0.14, relwidth=0.19)

    # Configuração da Treeview
    def treeview(self):
        # Cria as colunas da Treeview
        self.tv = ttk.Treeview(self.frm1)
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
        self.scroll = tk.Scrollbar(self.frm1, orient='vertical')
        
        # Adiciona os reagentes como linha
        self.refresh_table()

        self.tv.place(relx=0, rely=0, relwidth=1, relheight=1)

Application()