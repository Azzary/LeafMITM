from lxml import etree
import os


class Spells():

    def __init__(self,interface,spells_data):
        for spell in spells_data[:len(spells_data)-1]:
            spell = spell.split("~")
            self.get_name(spell[0])
            interface.add_spell(spell[0],self.get_name(spell[0]),spell[1])




    def get_name(self,id_):
        dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resource/spells.xml" )
        #dir_path = "D:/Users/remic/Desktop/MyProjet/Bot_socket/resource/spells.xml"
        spell_name = "None"
        tree = etree.parse(dir_path)
        
        for spell in tree.xpath("/SPELLS/SPELL"):
            if id_ == spell.get("ID"):
                spell_name = spell.find("NAME").text

        return spell_name

