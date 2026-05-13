class Field:
    def __init__(self):
        self.character = "."
        self.color = (34, 139, 34)  # Forest Green


class Street(Field):
    def __init__(self):
        self.character = "-"
        self.color = (80, 80, 80)  # Dark Grey


class House(Field):
    def __init__(self):
        self.character = "☖"
        self.resident = 1
        self.color = (200, 0, 0)  # Red


class Business(Field):
    def __init__(self):
        self.character = "*"
        self.color = (255, 165, 0)  # Orange


class Water(Field):
    def __init__(self):
        self.character = "~"
        self.color = (0, 105, 148)  # Sea Blue


class Car(Field):
    def __init__(self):
        self.character = "🝞"
        self.color = (255, 255, 0)  # Yellow