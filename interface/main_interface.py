import threading
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import os
from interface.map_interface import MapInterface



class Interface(threading.Thread):

    def __init__(self):
        threading.Thread(None,self.launch).start()

    def create_charater(self,gfx,speudo ,id_,lvl = ""):
        dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),f"resource\\gfx\\{gfx}.png")
        image = Image.open(dir_path) 
        photo = ImageTk.PhotoImage(image)
        self.canvas_gfx_character.create_image(photo.width()/4.5,photo.height()/2,image=photo)
        self.canvas_gfx_character.image = photo
        self.canvas_gfx_character.place(relx=0.05, rely=0.9, relwidth=0.5, relheight=0.5)
        self.canvas_gfx_character.place(relx=0.03, rely=0.1, relwidth=1, relheight=1)

        speudo_and_id ="SPEUDO: "+ speudo +"        ID: "+ id_ + "        LEVEL: "+ lvl
        name = Label(self.onglets_personnage, text = speudo_and_id, relief = RAISED )
        name.place(relx=0.01, rely=0.017,relwidth=0.4, relheight=0.09)
        
    def create_text(self):
        self.richTextBox1=Text(self.onglets_packets,font = '{MS Sans Serif} 10')
        self.richTextBox1.place(relx=0.05, rely=0.07, relwidth=0.85, relheight=0.75)
        self.scrollbar = Scrollbar(self.richTextBox1)
        self.scrollbar.pack( side = RIGHT, fill=Y)
        
    def print_richTextBox1(self,text):
        self.richTextBox1.insert(END,text+"\n")
        self.richTextBox1.see("end")
          

    def create_canvas_character(self):
        self.canvas_gfx_character = Canvas(self.onglets_personnage)
        self.create_charater("0","None","nul","nul")
        self.canvas_gfx_character.place(relx=0.03, rely=0.1, relwidth=1, relheight=1)
        
        self.canvas_vita = Canvas(self.onglets_personnage)
        self.print_image("stats\\vitaliter.png",self.canvas_vita)
        self.canvas_vita.place(relx=0.75, rely=0.05, relwidth=0.1, relheight=0.12)

        self.canvas_sagesse = Canvas(self.onglets_personnage)
        self.print_image("stats\\sagesse.png",self.canvas_sagesse)
        self.canvas_sagesse.place(relx=0.75, rely=0.20, relwidth=0.1, relheight=0.12)

        self.canvas_force = Canvas(self.onglets_personnage)
        self.print_image("stats\\force.png",self.canvas_force)
        self.canvas_force.place(relx=0.75, rely=0.35, relwidth=0.1, relheight=0.12)

        self.canvas_intel = Canvas(self.onglets_personnage)
        self.print_image("stats\\intelligence.png",self.canvas_intel)
        self.canvas_intel.place(relx=0.75, rely=0.50, relwidth=0.1, relheight=0.12)

        self.canvas_chance = Canvas(self.onglets_personnage)
        self.print_image("stats\\chance.png",self.canvas_chance)
        self.canvas_chance.place(relx=0.75, rely=0.65, relwidth=0.1, relheight=0.12)

        self.canvas_agi = Canvas(self.onglets_personnage)
        self.print_image("stats\\agilite.png",self.canvas_agi)
        self.canvas_agi.place(relx=0.75, rely=0.80, relwidth=0.1, relheight=0.12)

    def create_label_caracteristique(self,character):
        self.label_vita = Label(self.onglets_personnage, text = character.vie_max)
        self.label_vita.place(relx=0.80, rely=0.05, relwidth=0.1, relheight=0.12)

        self.label_sagesse = Label(self.onglets_personnage, text = character.sagesse)
        self.label_sagesse.place(relx=0.80, rely=0.20, relwidth=0.1, relheight=0.12)

        self.label_force = Label(self.onglets_personnage, text = character.force)
        self.label_force.place(relx=0.80, rely=0.35, relwidth=0.1, relheight=0.12)

        self.label_intel = Label(self.onglets_personnage, text = character.intel)
        self.label_intel.place(relx=0.80, rely=0.50, relwidth=0.1, relheight=0.12)

        self.label_chance = Label(self.onglets_personnage, text = character.chance)
        self.label_chance.place(relx=0.80, rely=0.65, relwidth=0.1, relheight=0.12)

        self.label_agi = Label(self.onglets_personnage, text = character.agi)
        self.label_agi.place(relx=0.80, rely=0.80, relwidth=0.1, relheight=0.12)

    def base_start(self,character):
        self.vita = Label(self.bot, bg="red", text = character.vie_actuelle +" / " + character.vie_max)
        self.vita.pack()
        self.vita.place(relx=0.20, rely=0.90, relwidth=0.08, relheight=0.08)

        self.energie = Label(self.bot, bg="yellow", text = character.ennergie_actuelle +" / " + character.ennergie_max)
        self.energie.pack()
        self.energie.place(relx=0.40, rely=0.90, relwidth=0.08, relheight=0.08)

        self.xp = Label(self.bot,bg="deep sky blue", text = character.xp_actuelle +" / " + character.xp_fin)
        self.xp.pack()
        self.xp.place(relx=0.60, rely=0.90, relwidth=0.1, relheight=0.08)

        self.kamas = Label(self.bot, bg="orange", text = character.kamas)
        self.kamas.pack()
        self.kamas.place(relx=0.80, rely=0.90, relwidth=0.08, relheight=0.08)

    def print_image(self,path,canvas_):
        dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"resource\\" +path )
        image = Image.open(dir_path) 
        photo = ImageTk.PhotoImage(image)
        canvas_.create_image(photo.width(),photo.height(),image=photo)
        canvas_.image = photo
    
    def create_notebook(self):
        self.onglets = ttk.Notebook(self.bot)
        self.onglets.pack()
        self.onglets.place(relx=0.15, rely=0.05, relwidth=0.83, relheight=0.83)


        #onglet pour les packets
        self.onglets_packets = ttk.Frame(self.onglets)       
        self.onglets_packets.pack()
        self.onglets.add(self.onglets_packets, text='Packet')
        
        #onglet pour le personnage
        self.onglets_personnage = ttk.Frame(self.onglets)      
        self.onglets_personnage.pack()
        self.onglets.add(self.onglets_personnage, text='character')

        #onglet pour le sort
        self.onglets_sorts = ttk.Frame(self.onglets) 
        self.onglets_sorts.pack()
        self.onglets.add(self.onglets_sorts, text='spells')     

        #onglet pour le sort
        self.onglet_map = ttk.Frame(self.onglets)      
        self.onglet_map.pack()
        
        self.onglets.add(self.onglet_map, text='map')
        
    def create_tableau_spell(self):
        self.tableau = ttk.Treeview(self.onglets_sorts, columns=("ID", "NAME", "LVL"))
        #self.tableau.heading("ICONE", text="icone")
        self.tableau.heading("ID", text="ID")
        self.tableau.heading("NAME", text="name")
        self.tableau.heading("LVL", text="lvl")
        self.tableau["show"] = "headings" 
        self.scrollbar2 = Scrollbar(self.tableau)
        self.scrollbar2.pack( side = RIGHT, fill=Y)
        self.tableau.place(relx=0.05, rely=0.1, relwidth=0.85, relheight=0.75) #self.tableau.pack()
        
    def add_spell(self,id_,name,lvl):
        self.tableau.insert('', 'end', values=(id_,name,lvl))        

    def launch(self):
        self.bot = Tk()
        self.bot.title('bot')
        self.bot.geometry('1200x900')

        self.create_notebook()
        self.create_text()
        
        
        self.create_tableau_spell()
        self.create_canvas_character()
        
        #Button(onglets_personnage, text='test', command=None).pack(padx=100, pady=100)
        self.map = MapInterface(self.onglet_map)

        
        self.bot.mainloop()
        
    def update_map(self, map_change):
        self.map.update_map(map_change)
    
    def update_entity(self, entity, entitie_remove):
        self.map.update_entity(entity, entitie_remove)
        
    def update_resource(self, cells_id):
        self.map.update_resource(cells_id)
        


       
  
