from .Class_Fill import Field, Street, House, Business, Water, Car
from .Class_Game import Game
import os
import time

# secure import from pynput (because of testing)
try:
    from pynput import keyboard
except Exception:

    class DummyKeyboard:
        class Listener:
            def __init__(self, on_press):
                pass

            def start(self):
                pass

            def stop(self):
                pass

    keyboard = DummyKeyboard()


class PlayGame(Game):
    def __init__(self):
        self.board = []
        self.running = True

    def on_press(self, key):
        try:
            if key.char == "q":
                self.running = False
        except AttributeError:
            pass

    def play_winterthur_map(self):
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
            # Move cursor to top-left instead of clearing
            print("\033[H", end="")
            # os.system("clear")
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
        self.load_random_city()
        self.counter = 0
        self.drivetime = 1
        self.car_step = 0

        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        # Clear once at the very start (cross-platform)
        os.system("cls" if os.name == "nt" else "clear")

        while self.running:
            # Move cursor to top-left instead of clearing
            print("\033[H", end="")
            # os.system("clear")
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
