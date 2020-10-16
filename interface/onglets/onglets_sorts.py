import tkinter

class OngletsSorts():

    def __init__(self, main_onglets):
        self.main_onglets = main_onglets
        self.onglets_sorts = tkinter.ttk.Frame(main_onglets) 
        self.onglets_sorts.pack()
        main_onglets.add(self.onglets_sorts, text='spells')     
        self.create_tableau_spell()

    def set_character(self, character):
        self.character = character

    def create_tableau_spell(self):
        self.tableau = tkinter.ttk.Treeview(self.onglets_sorts, columns=("ID", "NAME", "LVL"))
        #self.tableau.heading("ICONE", text="icone")
        self.tableau.heading("ID", text="ID")
        self.tableau.heading("NAME", text="name")
        self.tableau.heading("LVL", text="lvl")
        self.tableau["show"] = "headings" 
        self.tableau.place(relx=0.05, rely=0.1, relwidth=0.85, relheight=0.75) #self.tableau.pack()
        
    def add_spell(self,id_,name,lvl):
        self.tableau.insert('', 'end', values=(id_,name,lvl))        
        self.character.spells.list_spell[id_] = (name,lvl) 

    def removes_spells(self):
        for row in self.tableau.get_children():
            self.tableau.delete(row)
        self.character.spells.list_spell = {}