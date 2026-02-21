
import random
import numpy as np
import re
import os
import time
import keyboard


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
        self.character = ("\x1b[1;34;43m" + "⌷" + "\x1b[0m")
        
class Water(Field):
    def __init__(self):
        self.character = ("\x1b[1;37;44m" + "~" + "\x1b[0m")

class Car(Field): 
    def __init__(self):
        self.character = "🝞"
        
class Game:
    def __init__(self):
        self.board = []
        user_choice = input("Mit welcher Karte möchten Sie weiterfahren?\
                                     \n 1:Wiezikon\
                                         \n 2:Zufällig generierte Karte\
                                             \n wählen Sie 1 oder 2.")
        self.check_user_input(user_choice)
        
    def interface(self,user_choice):
        self.user_choice = int(user_choice)
        if self.user_choice == 1:
            self.load_board_wiezikon()
            self.print_board()
            
        elif self.user_choice == 2:
            self.random_city()
            self.print_board()
            
    def load_board_wiezikon(self):
        f = open("map_of_wiezikon.txt","r")
        self.lines = f.readlines() #lines enthält nun eine Liste mit je einer Zeile des Textes
        f.close()
        self.lines = [line.rstrip('\n') for line in self.lines]
        
        for line in range(len(self.lines)):
            self.board.append([])
            for j in range(len(self.lines[0])):
                self.fill_field(line,j)
                
    def fill_field(self,i,j):
        if self.lines[i][j] == "l":
            self.board[i].append(Field()) #hier füllen Sie das Spielbrett
        elif self.lines[i][j] == "s":
            self.board[i].append(Street())
        elif self.lines[i][j] == "h":
            self.board[i].append(House())    
        elif self.lines[i][j] == "b":
            self.board[i].append(Business())
        elif self.lines[i][j] == "w":
            self.board[i].append(Water())
        elif self.lines[i][j] == "a":
            self.board[i].append(Car())
     
    def random_city(self):
        self.board = [[(figures[random.randrange(5)]) for x in range(30)] for y in range(30)]
        np.save("random_map.npy", self.board)
        
    def print_board(self):        
        for i in range(len(self.board)):
          for j in range(len(self.board[0])):
              print(self.board[i][j].character,end="")
          print()
          
    def check_user_input(self,user_choice):
        match = re.search(r'([12]+)', user_choice)
        while not match or int(user_choice) < 1 or int(user_choice) > 11:
            print("Bitte überprüfen Sie Ihren Input, etwas stimmt nicht! ")
            user_choice = input("Mit welcher Karte möchten Sie weiterfahren?\
                                     \n 1:Wiezikon\
                                         \n 2:Zufällig generierte Karte\
                                             \n wählen Sie 1 oder 2.")
            
            match = re.search(r'([12]+)', user_choice)
        self.interface(user_choice)
        

        
    def play(self):
        self.counter = 0
        self.drivetime = 0

        while True:
            os.system("clear")
            self.printer()
            self.drivetime += 1
            self.counter += 1
            print()
            print("Generation: ", self.counter, "  House(☖), Business(⌷), Water(~), Land(.), Car(🝞), Street(=)")
            print()
            g.populationSubT()
            g.driveSubT()
            g.pupsafeSubT()        
            time.sleep(0.5)
        
               
    def populationSubT(self):
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
        y = 18
        self.right = True
        for i in range(30):
            if self.right == True:    
                for j in range(30):                   
                    #self.board[self.drivetime][y] = Car() #Auto wird gesetzt 
                    if self.drivetime != 0:
                        if self.lines [self.drivetime-1][y] == "s":
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
                        
            '''if self.right == False:
                for k in range(29,0,-1):
                    self.board[k][18] = Car() #Auto
                    if k != 29:
                        self.board[k+1][18] = Street() #Strasse
                    if self.drivetime == 29:
                        self.right = True
                        self.drivetime = 0'''
                    
                

                
    def pupsafeSubT(self):
        pass
                
    def printer(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(self.board[i][j].character, end="")
            print()
        
"""class Logger ():
    def log(text):"""  
    

figures = [Field(), Water(), House(), Business(), Street(), Car()]

g = Game()
g.play()
