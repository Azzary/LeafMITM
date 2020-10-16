

class Entity():
    
    
    def __init__(self, type_, cell=0, **kwargs):
        self.type = type_
        self.cell = cell
        self.isMainCharacter = False
        self.__dict__.update(kwargs)

