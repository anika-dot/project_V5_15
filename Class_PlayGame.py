from Class_Fill import Field, Street, House, Business, Water, Car
from Class_Game import Game
import os
import time
import keyboard


class PlayGame(Game):
    
    def __init__(self):
        self.board = []
        pass
    
    def play(self):
        # Spiel mit Karte von Winterthur
        self.load_board_winterthur()
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
            self.populationSubT()
            self.driveSubT()
            self.pupsafeSubT()        
            time.sleep(0.5)
            if keyboard.is_pressed("q"):
                print("You pressed q")
                break

    def play_random(self):
        # Spiel mit zufälligem Spielfeld
        self.random_city()
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
            self.populationSubT()
            self.driveSubT()
            self.pupsafeSubT()        
            time.sleep(0.5)
            if keyboard.is_pressed("q"):
                print("You pressed q")
                break

figures = [Field(), Water(), House(), Business(), Street(), Car()]