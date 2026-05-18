"""
Module containing the definition of the game logic.
"""

import os
import time
from .Class_Fill import Field, Street, House, Business, Water, Car
from .Class_Game import Game

# secure import from pynput (because of testing)
try:
    from pynput import keyboard
except ImportError:

    class DummyKeyboard:
        """
        Creating a dummy keyboard, if pynput.keyboard can not be imported.
        """

        class Listener:
            """
            Initialize dummy listener.
            """

            def __init__(self, on_press):
                pass

            def start(self):
                """
                Mock start method.
                """

            def stop(self):
                """
                Mock stop method.
                """

    keyboard = DummyKeyboard()


class PlayGame(Game):
    """
    Class to play the game.
    """

    def __init__(self):
        super().__init__()
        self.board = []
        self.running = True
        self.counter = 0
        self.drivetime = 1

    def on_press(self, key):
        """
        Definition of the stopping criteria.
        """
        try:
            if key.char == "q":
                self.running = False
        except AttributeError:
            pass

    def play_winterthur_map(self):
        """
        Function to play the game with the winterthur map.
        """
        self.load_winterthur_map()
        self.counter = 0
        self.drivetime = 1
        self.car_step = 0
        if keyboard is not None and hasattr(keyboard, "Listener"):
            listener = keyboard.Listener(on_press=self.on_press)
            listener.start()
        else:
            listener = None

        # Clear once at the very start (cross-platform)
        os.system("cls" if os.name == "nt" else "clear")

        while self.running:
            print("\033[H", end="")  # Move cursor to top-left instead of clearing
            self.display_board()
            self.car_step += 1
            self.counter += 1
            print()
            print(
                "Generation: ",
                self.counter,
                "  House(☖), Business(*), Water(~), Land(.), Car(🝞), Street(=)",
            )
            print("Press Q to quit")
            print()
            self.population_growth()
            self.simulate_traffic()
            self.check_population_safety()
            time.sleep(0.5)
        listener.stop()

    def play_random_map(self):
        """
        Function to play the game with the random map.
        """
        self.load_random_city()
        self.counter = 0
        self.drivetime = 1
        self.car_step = 0

        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        # Clear once at the very start (cross-platform)
        os.system("cls" if os.name == "nt" else "clear")

        while self.running:
            print("\033[H", end="")  # Move cursor to top-left instead of clearing
            self.display_board()
            self.car_step += 1
            self.counter += 1
            print()
            print(
                "Generation: ",
                self.counter,
                "  House(☖), Business(⌷), Water(~), Land(.), Car(🝞), Street(=)",
            )
            print()
            self.population_growth()
            self.simulate_traffic()
            self.check_population_safety()
            time.sleep(0.5)
        if listener is not None:
            listener.stop()


figures = [Field(), Water(), House(), Business(), Street(), Car()]
