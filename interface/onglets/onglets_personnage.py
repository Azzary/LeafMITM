import tkinter
import os
from PIL import Image, ImageTk 

class OngletsPersonnage():

    def __init__(self, main_onglets):
        self.onglets_personnage = tkinter.ttk.Frame(main_onglets)      
        self.onglets_personnage.pack()
        main_onglets.add(self.onglets_personnage, text='character')

        self.create_canvas_character()

    def set_character(self, character):
        self.character = character
        
    def create_canvas_character(self):
        self.canvas_gfx_character = tkinter.Canvas(self.onglets_personnage)
        self.create_charater("0","None","nul","nul")
        self.canvas_gfx_character.place(relx=0.03, rely=0.1, relwidth=1, relheight=1)
        
        self.canvas_vita = tkinter.Canvas(self.onglets_personnage)
        self.print_image("stats\\vitaliter.png",self.canvas_vita)
        self.canvas_vita.place(relx=0.75, rely=0.05, relwidth=0.1, relheight=0.12)

        self.canvas_sagesse = tkinter.Canvas(self.onglets_personnage)
        self.print_image("stats\\sagesse.png",self.canvas_sagesse)
        self.canvas_sagesse.place(relx=0.75, rely=0.20, relwidth=0.1, relheight=0.12)

        self.canvas_force = tkinter.Canvas(self.onglets_personnage)
        self.print_image("stats\\force.png",self.canvas_force)
        self.canvas_force.place(relx=0.75, rely=0.35, relwidth=0.1, relheight=0.12)

        self.canvas_intel = tkinter.Canvas(self.onglets_personnage)
        self.print_image("stats\\intelligence.png",self.canvas_intel)
        self.canvas_intel.place(relx=0.75, rely=0.50, relwidth=0.1, relheight=0.12)

        self.canvas_chance = tkinter.Canvas(self.onglets_personnage)
        self.print_image("stats\\chance.png",self.canvas_chance)
        self.canvas_chance.place(relx=0.75, rely=0.65, relwidth=0.1, relheight=0.12)

        self.canvas_agi = tkinter.Canvas(self.onglets_personnage)
        self.print_image("stats\\agilite.png",self.canvas_agi)
        self.canvas_agi.place(relx=0.75, rely=0.80, relwidth=0.1, relheight=0.12)


    def create_label_caracteristique(self,character):
        self.label_vita =  tkinter.Label(self.onglets_personnage, text = character.vie_max)
        self.label_vita.place(relx=0.80, rely=0.05, relwidth=0.1, relheight=0.12)

        self.label_sagesse = tkinter.Label(self.onglets_personnage, text = character.sagesse)
        self.label_sagesse.place(relx=0.80, rely=0.20, relwidth=0.1, relheight=0.12)

        self.label_force = tkinter.Label(self.onglets_personnage, text = character.force)
        self.label_force.place(relx=0.80, rely=0.35, relwidth=0.1, relheight=0.12)

        self.label_intel = tkinter.Label(self.onglets_personnage, text = character.intel)
        self.label_intel.place(relx=0.80, rely=0.50, relwidth=0.1, relheight=0.12)

        self.label_chance = tkinter.Label(self.onglets_personnage, text = character.chance)
        self.label_chance.place(relx=0.80, rely=0.65, relwidth=0.1, relheight=0.12)

        self.label_agi = tkinter.Label(self.onglets_personnage, text = character.agi)
        self.label_agi.place(relx=0.80, rely=0.80, relwidth=0.1, relheight=0.12)

    def print_image(self,path,canvas_):
        dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"resource\\" +path )
        image = Image.open(dir_path) 
        photo = ImageTk.PhotoImage(image)
        canvas_.create_image(photo.width(),photo.height(),image=photo)
        canvas_.image = photo

    def create_charater(self,gfx,speudo ,id_,lvl = ""):
        dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),f"resource\\gfx\\{gfx}.png")
        image = Image.open(dir_path) 
        photo = ImageTk.PhotoImage(image)
        self.canvas_gfx_character.create_image(photo.width()/4.5,photo.height()/2,image=photo)
        self.canvas_gfx_character.image = photo
        self.canvas_gfx_character.place(relx=0.05, rely=0.9, relwidth=0.5, relheight=0.5)
        self.canvas_gfx_character.place(relx=0.03, rely=0.1, relwidth=1, relheight=1)

        speudo_and_id ="SPEUDO: "+ speudo +"        ID: "+ id_ + "        LEVEL: "+ lvl
        name = tkinter.Label(self.onglets_personnage, text = speudo_and_id)
        name.place(relx=0.01, rely=0.017,relwidth=0.4, relheight=0.09)


