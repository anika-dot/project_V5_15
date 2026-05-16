"""
Module defining the visual and structural cell types used in the city simulation.
Each class represents one type of cell on the game board, for example
streets, houses, businesses, water, cars, and general fields.
All cell types inherit from the Field base class.
"""


class Field:
    """
    Base cell type representing empty land in the game grid.
    """

    def __init__(self):
        super().__init__()
        self.character = "\x1b[66;30;42m" + "." + "\x1b[0m"


class Street(Field):
    """
    Cell type representing a street segment.
    """

    def __init__(self):
        super().__init__()
        self.character = "-"


class House(Field):
    """
    Cell type representing a residential building.
    """

    def __init__(self):
        super().__init__()
        self.character = "\x1b[1;21;41m" + "☖" + "\x1b[0m"
        self.resident = 1


class Business(Field):
    """
    Cell type representing a commercial building.
    """

    def __init__(self):
        super().__init__()
        self.character = "\x1b[1;34;43m" + "*" + "\x1b[0m"


class Water(Field):
    """
    Cell type representing a water tile or body.
    """

    def __init__(self):
        super().__init__()
        self.character = "\x1b[1;37;44m" + "~" + "\x1b[0m"


class Car(Field):
    """
    Cell type representing a car.
    """

    def __init__(self):
        super().__init__()
        self.character = "🝞"
