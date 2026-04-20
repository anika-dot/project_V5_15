from Class_Fill import Field, Street, House, Business, Water, Car
from Class_Game import Game
import os
import time
from pynput import keyboard

class PlayGame(Game):
    
    def __init__(self):
        self.board = []
        self.running = True
        
    def on_press(self, key):
        try:
            if key.char =='q':
                self.running = False
        except AttributeError:
            pass
  
 
    def play(self):
        # Spiel mit Karte von Winterthur
        self.load_board_winterthur()
        self.counter = 0
        self.drivetime = 0
        
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        while self.running:
            os.system("clear")
            self.print_board()
            self.drivetime += 1
            self.counter += 1
            print()
            print("Generation: ", self.counter, "  House(☖), Business(*), Water(~), Land(.), Car(🝞), Street(=)")
            print("Press Q to quit")
            print()
            self.populationSubT()
            self.driveSubT()
            self.pupsafeSubT()        
            time.sleep(0.5)
        listener.stop()   

    def play_random(self):
        # Spiel mit zufälligem Spielfeld
        self.random_city()
        self.counter = 0
        self.drivetime = 0
        
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        
        while self.running:
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
        listener.stop()
            

figures = [Field(), Water(), House(), Business(), Street(), Car()]