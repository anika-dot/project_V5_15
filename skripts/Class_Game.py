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
        char = self.lines[i][j]
        if char == "G":
            self.board[i].append(Field())
        elif char == "S":
            self.board[i].append(Street())
        elif char == "R":
            self.board[i].append(House())
        elif char == "T":
            self.board[i].append(Business())
        elif char.lower() == "w":  # Catch both 'w' and 'W'
            self.board[i].append(Water())
        elif char == "a":
            self.board[i].append(Car())
            # SYNC: Update the simulation's car tracking to this position
            self.car_step = i
            self.car_col = j
     
    def load_random_city(self):
        self.board = [[(figures[random.randrange(5)]) for x in range(30)] for y in range(30)]
        np.save("random_map.npy", self.board)
        
    def display_board(self):        
        for i in range(len(self.board)):
          for j in range(len(self.board[0])):
              print(self.board[i][j].character,end = "")
          print()

    def population_growth(self):
        """
        Updates residents and handles city expansion.
        Houses grow over time and spawn new houses nearby at population 5.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if isinstance(self.board[i][j], House):
                    # Natural decline/growth balance
                    self.board[i][j].resident -= 0.1

                    # Expansion logic: Find a neighboring Field to build a new House
                    if self.board[i][j].resident >= 5:
                        spawned = False
                        for di in [-1, 0, 1]:
                            for dj in [-1, 0, 1]:
                                ni, nj = i + di, j + dj
                                # Boundary check for the 30x30 grid
                                if 0 <= ni < 30 and 0 <= nj < 30:
                                    if type(self.board[ni][nj]) is Field:
                                        self.board[ni][nj] = House()
                                        self.board[i][j].resident = 2  # Reset parent population
                                        spawned = True
                                        break
                            if spawned: break

                    # Remove house if population hits zero
                    if self.board[i][j].resident <= 0:
                        self.board[i][j] = Field()
                    else:
                        self.board[i][j].resident += 0.2

    def simulate_traffic(self):
        # 1. Identify current and potential moves
        r, c = self.car_step, self.car_col
        possible_moves = []

        # Check all 4 directions (Down, Up, Right, Left)
        directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for nr, nc in directions:
            # Stay within board boundaries
            if 0 <= nr < 30 and 0 <= nc < 30:
                # Check if the target is a Street
                if isinstance(self.board[nr][nc], Street):
                    possible_moves.append((nr, nc))

        # 2. Filter out the previous position to avoid immediate U-turns
        # (Only filter if there are other choices available)
        choices = [m for m in possible_moves if m != self.last_pos]

        if not choices and possible_moves:
            # DEAD END: The only way is back where we came from
            next_move = possible_moves[0]
        elif choices:
            # MULTIPLE OPTIONS: Pick one at random
            next_move = random.choice(choices)
        else:
            # TRAPPED: No streets nearby (reset car or stay put)
            return

        # 3. Execute the Move
        # Clear current position
        self.board[r][c] = Street()

        # Store current as 'last_pos' for the next frame
        self.last_pos = (r, c)

        # Update coordinates
        self.car_step, self.car_col = next_move

        # Place car in new position
        self.board[self.car_step][self.car_col] = Car()

    def check_population_safety(self):
        pass        

figures = [Field(), Water(), House(), Business(), Street(), Car()]