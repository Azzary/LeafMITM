import os
import json
import character.job as job

class Script():

    def __init__(self,character):
        self.character = character
        self.script = None
        with open("D:/Users/cremi/Desktop/Leaf/test.json", "r") as file:
            self.script = json.load(file)
        
    def load_script(self, path):
        with open(path, "r") as file:
            self.script = json.load(file)
        


    def action(self):
        map_id = self.character.map.mapID
        if map_id in self.script: 
            #Verifier la map
            #Avoir l'action (combat,recole,mouv)
            #Action suiv ...

            if self.script[map_id] == "recolte":
                for cell in self.character.map.cells:
                    if cell.isInteractive:
                        job.recole(self.character,cell.CellID)
            elif self.script[map_id] == "combat":
                print("Combat")



            self.changer_map()

    def changer_map(self):
        pass