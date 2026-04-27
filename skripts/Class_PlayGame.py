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
  
 
    def play_winterthur_map(self):
        self.load_winterthur_map()
        self.counter = 0
        self.drivetime = 0
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        while self.running:
            os.system("clear")
            self.display_board()
            self.drivetime += 1
            self.counter += 1
            print()
            print("Generation: ", self.counter, "  House(☖), Business(*), Water(~), Land(.), Car(🝞), Street(=)")
            print("Press Q to quit")
            print()
            self.population_growth()
            self.simulate_traffic()
            self.check_population_safety()        
            time.sleep(0.5)
        listener.stop()   

    def play_random_map(self):
        self.load_random_city()
        self.counter = 0
        self.drivetime = 0
        
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        
        while self.running:
            os.system("clear")
            self.display_board()
            self.drivetime += 1
            self.counter += 1
            print()
            print("Generation: ", self.counter, "  House(☖), Business(⌷), Water(~), Land(.), Car(🝞), Street(=)")
            print()
            self.population_growth()
            self.simulate_traffic()
            self.check_population_safety()        
            time.sleep(0.5)
        listener.stop()
            

figures = [Field(), Water(), House(), Business(), Street(), Car()]