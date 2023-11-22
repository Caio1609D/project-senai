import tkinter as tk

frm = tk.Frame()
def widgets(self):
        # Botão para pegar (?) um reagente
        self.getBtn = tk.Button(self.frm, text="Pegar", command=lambda: self.get_reagent(self.selected[0])) # Achar um termo/legenda melhor que "pegar"
        self.getBtn.place(relx=0.05, rely=0.1, relwidth=0.1, relheight=0.1)

        # Botão pra falar a quantidade de reagente devolvido
        self.returnEntry = tk.Entry(self.frm)
        self.returnEntry.place(relx=0.175, rely=0.1, relwidth=0.1, relheight=0.1)

        # Botão para devolver um reagente
        self.returnBtn = tk.Button(self.frm, text="Devolver", command=lambda: self.return_reagent(self.selected[0], float(self.returnEntry.get())))
        self.returnBtn.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)