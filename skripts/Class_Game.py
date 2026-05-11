import random
import numpy as np
from pathlib import Path
from Class_Fill import Field, Street, House, Business, Water, Car


class Game:
    def __init__(self):
        self.board = []
            
    def load_winterthur_map(self):
        file_path = Path(__file__).parent / "Winterthur_neu.txt"
    
        f = open(file_path, "r", encoding="utf-8")

        self.lines = f.readlines()
        f.close()

        self.lines = [line.rstrip('\n') for line in self.lines]
        for line in range(len(self.lines)):
            self.board.append([])
            for j in range(len(self.lines[0])):
                self.fill_field(line, j)

                
    def fill_field(self,i,j):
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
        self.board = [[(figures[random.randrange(5)]) for x in range(30)] for y in range(30)]
        np.save("random_map.npy", self.board)

    def display_board(self):
        output = []
        for i in range(len(self.board)):
            line = "".join([self.board[i][j].character for j in range(len(self.board[0]))])
            output.append(line)
        print("\n".join(output))

    def population_growth(self):
        temp_row = -1
        temp_col = -1
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):                
                if isinstance(self.board[i][j], Field):
                    temp_row = i
                    temp_col = j    
                if isinstance(self.board[i][j], House):
                    # death rate applied each generation
                    self.board[i][j].resident -= 0.5

                    # create new house on nearest empty field when population reaches threshold
                    if self.board[i][j].resident == 5 and temp_row >= 0:
                        self.board[temp_row][temp_col] = House()
                        
                    if self.board[i][j].resident == 0:
                        self.board[i][j] = Field()
                    else:
                        self.board[i][j].resident += 1

    def simulate_traffic(self):
        car_position = 11
        self.right = True
        for i in range(30):
            if self.right == True:    
                for j in range(30):                   
                    if self.car_step != 0:
                        if isinstance(self.board[self.car_step-1][car_position], Street):
                            self.board[self.car_step][car_position] = Car()
                            self.board[self.car_step-1][car_position] = Street()
                        else:
                            self.board[self.car_step-1][car_position] = Street()
                            self.board[self.car_step][car_position-1] = Car()
                            self.board[self.car_step][car_position-1] = Street()
                            car_position -= 1
                    if self.car_step == 29:
                        self.right = False
                        self.car_step = 0
                        
    def check_population_safety(self):
        pass        

figures = [Field(), Water(), House(), Business(), Street(), Car()]