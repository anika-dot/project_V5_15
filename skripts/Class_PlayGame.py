from Class_Fill import Field, Street, House, Business, Water, Car
from Class_Game import Game
import os
import time

class PlayGame(Game):

    def __init__(self):
        super().__init__()  # This ensures the board from Class_Game is also ready
        self.board = []
        self.running = True
        self.car_step = 0  # Vertical Position (row)
        self.car_col = 11  # Horizontal position (column)
        self.moving_right = True
        self.counter = 0  # Good practice to initialize this here too
        self.last_pos = (None, None)
 
    def play_winterthur_map(self):
        self.load_winterthur_map()
        self.counter = 0
        self.car_step = 0

        while self.running:
            os.system("clear")
            self.display_board()
            self.car_step += 1
            self.counter += 1
            print()
            print("Generation: ", self.counter, "  House(☖), Business(*), Water(~), Land(.), Car(🝞), Street(=)")
            print("Press Q to quit")
            print()
            self.population_growth()
            self.simulate_traffic()
            self.check_population_safety()        
            time.sleep(0.5)

    def play_random_map(self):
        self.load_random_city()
        self.counter = 0
        self.car_step = 0
        
        while self.running:
            os.system("clear")
            self.display_board()
            self.car_step += 1
            self.counter += 1
            print()
            print("Generation: ", self.counter, "  House(☖), Business(⌷), Water(~), Land(.), Car(🝞), Street(=)")
            print()
            self.population_growth()
            self.simulate_traffic()
            self.check_population_safety()        
            time.sleep(0.5)

figures = [Field(), Water(), House(), Business(), Street(), Car()]