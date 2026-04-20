class Field:
    def __init__(self):
        self.character = ("\x1b[66;30;42m" + "." + "\x1b[0m")
    
class Street(Field):
    def __init__(self):
        self.character = "-"   
        
class House(Field):
    def __init__(self):
        self.character = ("\x1b[1;21;41m" +"☖" + "\x1b[0m")
        self.bewohner = 1

class Business(Field):
    def __init__(self):
        self.character = ("\x1b[1;34;43m" + "*" + "\x1b[0m")
        
class Water(Field):
    def __init__(self):
        self.character = ("\x1b[1;37;44m" + "~" + "\x1b[0m")

class Car(Field): 
    def __init__(self):
        self.character = "🝞"