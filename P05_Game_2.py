import random
import numpy as np
import os
import time
import keyboard
from Class_Fill import Field, Street, House, Business, Water, Car


class Game:
    def __init__(self):
        self.board = []
            
    def load_board_winterthur(self):
        # Hier wird die Karte von Winterthur geladen
        f = open("Winterthur_neu.txt","r")
        self.lines = f.readlines()
        f.close()
        self.lines = [line.rstrip('\n') for line in self.lines]
        
        for line in range(len(self.lines)):
            self.board.append([])
            for j in range(len(self.lines[0])):
                self.fill_field(line,j)
                
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

    def play(self):
        # Spiel mit Karte von Winterthur
        self.load_board_winterthur()
        self.print_board()
        self.counter = 0
        self.drivetime = 0

        while True:
            os.system("clear")
            self.print_board()
            self.drivetime += 1
            self.counter += 1
            print()
            print("Generation: ", self.counter, "  House(☖), Business(*), Water(~), Land(.), Car(🝞), Street(=)")
            print()
            g.populationSubT()
            g.driveSubT()
            g.pupsafeSubT()        
            time.sleep(0.5)
            if keyboard.read_key() == "q":
                print("You pressed q")
                break

    def play_random(self):
        # Spiel mit zufälligem Spielfeld
        self.random_city()
        self.print_board()
        self.counter = 0
        self.drivetime = 0
        
        while True:
            os.system("clear")
            self.print_board()
            self.drivetime += 1
            self.counter += 1
            print()
            print("Generation: ", self.counter, "  House(☖), Business(⌷), Water(~), Land(.), Car(🝞), Street(=)")
            print()
            g.populationSubT()
            g.driveSubT()
            g.pupsafeSubT()        
            time.sleep(0.5)
            if keyboard.read_key() == "q":
                print("You pressed q")
                break         
               
    def populationSubT(self):
        # Bewohner werden hinzugefügt und sie sterben.
        tempi = -1
        tempj = -1
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):                
                if isinstance(self.board[i][j], Field):
                    tempi = i
                    tempj = j    
                if isinstance(self.board[i][j], House):
                    self.board[i][j].bewohner -= 0.5     #Sterberate
                        
                    if self.board[i][j].bewohner == 5 and tempi >= 0:
                        self.board[tempi][tempj] = House()
                        
                    if self.board[i][j].bewohner == 0:
                        self.board[i][j] = Field()
                    else:
                        self.board[i][j].bewohner += 1

    def driveSubT(self):
        # Auto kann auf den Strassen fahren
        y = 11
        self.right = True
        for i in range(30):
            if self.right == True:    
                for j in range(30):                   
                    #self.board[self.drivetime][y] = Car() #Auto wird gesetzt 
                    if self.drivetime != 0:
                        if self.lines [self.drivetime-1][y] == "S":
                            self.board[self.drivetime][y] = Car()
                            self.board[self.drivetime-1][y] = Street()  #Strasse zieht mit
                        else:
                            self.board[self.drivetime-1][y] = Street()
                            self.board[self.drivetime][y-1] = Car()
                            self.board[self.drivetime][y-1] = Street()
                            y -= 1
                    if self.drivetime == 29:
                        self.right = False
                        self.drivetime = 0
                        
    def pupsafeSubT(self):
        pass        


figures = [Field(), Water(), House(), Business(), Street(), Car()]

g = Game()
g.play()
