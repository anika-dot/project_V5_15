"""
Module to initialize and define all functions used in the PlayGame.
"""

import random
from pathlib import Path
import numpy as np
from .Class_Fill import Field, Street, House, Business, Water, Car


class Game:
    """
    Class that implements the core simulation logic for a simple city environment.
    It handles board initialization, loading predefined or random maps,
    simulating population growth, and basic traffic movement.
    """

    def __init__(self):
        self.board = []
        self.car_step = 0
        self.right = True
        self.lines = []
        self.temp_row = -1
        self.temp_col = -1

    def load_winterthur_map(self):
        """
        Load the predefined map 'Winterthur_neu.txt' and fill the game board accordingly.
        Each character in the file corresponds to a specific cell type (Field, Street, House, etc.).
        The board is built as a 2D list of cell objects.
        """
        file_path = Path(__file__).parent / "Winterthur_neu.txt"

        f = open(file_path, "r", encoding="utf-8")

        self.lines = f.readlines()
        f.close()

        self.lines = [line.rstrip("\n") for line in self.lines]
        for line in range(len(self.lines)):
            self.board.append([])
            for j in range(len(self.lines[0])):
                self.fill_field(line, j)

    def fill_field(self, i, j):
        """
        Create and append the correct cell object based on a character from the map.
        Args:
            i (int): Row index.
            j (int): Column index.
        """
        if self.lines[i][j] == "G":
            self.board[i].append(Field())
        elif self.lines[i][j] == "S":
            self.board[i].append(Street())
        elif self.lines[i][j] == "R":
            self.board[i].append(House())
        elif self.lines[i][j] == "T":
            self.board[i].append(Business())
        elif self.lines[i][j] == "w":
            self.board[i].append(Water())
        elif self.lines[i][j] == "a":
            self.board[i].append(Car())

    def load_random_city(self):
        """
        Randomly generate a new 30x30 city board using cell types from the 'figures' list.
        The generated map is saved to a NumPy binary file named 'random_map.npy'.
        """
        self.board = [
            [(figures[random.randrange(5)]) for x in range(30)] for y in range(30)
        ]
        np.save("random_map.npy", self.board)

    def display_board(self):
        """
        Print the current board to the console as a grid of characters.
        Each cell is represented by its 'character' property.
        """
        output = []
        for i in range(len(self.board)):
            line = "".join(
                [self.board[i][j].character for j in range(len(self.board[0]))]
            )
            output.append(line)
        print("\n".join(output))

    def population_growth(self):
        """
        Simulate one step of population growth and housing changes.
        Houses with one or more inhabitants grow in population.
        If a house reaches a certain threshold, a new house may appear nearby.
        Houses with zero inhabitants are turned into empty fields.
        """
        temp_row = -1
        temp_col = -1
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                cell = self.board[i][j]

                # Accessing an attribute raises an AttributeError when the value is None
                _ = cell.character

                if isinstance(cell, Field):
                    temp_row = i
                    temp_col = j
                if isinstance(cell, House):
                    # Population growth: increase the number of residents when >= 1
                    if cell.resident >= 1:
                        cell.resident += 1
                    # death rate applied each generation
                    cell.resident -= 0.5
                    # create new house on nearest empty field when population reaches threshold
                    if cell.resident == 5 and temp_row >= 0:
                        self.board[temp_row][temp_col] = House()

                    if cell.resident == 0:
                        self.board[i][j] = Field()

    def simulate_traffic(self):
        """
        Simulate one step of traffic movement across the board.
        Moves car objects along the street cells from top to bottom
        and reverses direction when reaching the end of the board.
        """
        car_position = 11
        self.right = True
        for i in range(30):  # pylint: disable=unused-variable
            if self.right:
                for j in range(30):  # pylint: disable=unused-variable
                    if self.car_step != 0:
                        if isinstance(
                            self.board[self.car_step - 1][car_position], Street
                        ):
                            self.board[self.car_step][car_position] = Car()
                            self.board[self.car_step - 1][car_position] = Street()
                        else:
                            self.board[self.car_step - 1][car_position] = Street()
                            self.board[self.car_step][car_position - 1] = Car()
                            self.board[self.car_step][car_position - 1] = Street()
                            car_position -= 1
                    if self.car_step == 29:
                        self.right = False
                        self.car_step = 0

    def check_population_safety(self):
        """
        Placeholder for a future safety check implementation.
        Intended to detect overpopulated or unsafe areas in the city.
        Currently does nothing.
        """
        pass  # pylint: disable=W0107


figures = [Field(), Water(), House(), Business(), Street(), Car()]
