import random
import numpy as np
from pathlib import Path
from Class_Fill import Field, Street, House, Business, Water, Car


class Game:
    def __init__(self):
        self.board = []
            
    def load_board_winterthur(self):
        # Hier wird die Karte von Winterthur geladen
        
        # f = open("Winterthur_neu.txt","r")
        #f = open(r"C:\Users\anika\OneDrive\Desktop\ZHAW_Master\Developing_Software_as_a_Product\Project\project_V5_15\Winterthur_neu.txt", "r")
        #self.lines = f.readlines()
        #f.close()
        #self.lines = [line.rstrip('\n') for line in self.lines]
        
        #for line in range(len(self.lines)):
        #    self.board.append([])
        #    for j in range(len(self.lines[0])):
        #        self.fill_field(line,j)
        
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
        # Hier wird das Spielbrett gefüllt
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
     
    def random_city(self):
        # Hier wird eine zufällige Karte geladen
        self.board = [[(figures[random.randrange(5)]) for x in range(30)] for y in range(30)]
        np.save("random_map.npy", self.board)
        
    def print_board(self):        
        for i in range(len(self.board)):
          for j in range(len(self.board[0])):
              print(self.board[i][j].character,end = "")
          print()

    def populationSubT(self):
        # Bewohner werden hinzugefügt und sie sterben
        temp_row = -1
        temp_col = -1
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):                
                if isinstance(self.board[i][j], Field):
                    temp_row = i
                    temp_col = j    
                if isinstance(self.board[i][j], House):
                    self.board[i][j].resident -= 0.5     #Sterberate
                        
                    if self.board[i][j].resident == 5 and temp_row >= 0:
                        self.board[temp_row][temp_col] = House()
                        
                    if self.board[i][j].resident == 0:
                        self.board[i][j] = Field()
                    else:
                        self.board[i][j].resident += 1

    def driveSubT(self):
        # Auto kann auf den Strassen fahren
        car_position = 11
        self.right = True
        for i in range(30):
            if self.right == True:    
                for j in range(30):                   
                    #self.board[self.drivetime][y] = Car() #Auto wird gesetzt 
                    if self.car_step != 0:
                        #if self.lines [self.drivetime-1][y] == "S":
                        if isinstance(self.board[self.car_step-1][car_position], Street):
                            self.board[self.car_step][car_position] = Car()
                            self.board[self.car_step-1][car_position] = Street()  #Strasse zieht mit
                        else:
                            self.board[self.car_step-1][car_position] = Street()
                            self.board[self.car_step][car_position-1] = Car()
                            self.board[self.car_step][car_position-1] = Street()
                            car_position -= 1
                    if self.car_step == 29:
                        self.right = False
                        self.car_step = 0
                        
    def pupsafeSubT(self):
        pass        

figures = [Field(), Water(), House(), Business(), Street(), Car()]