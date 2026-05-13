import pygame
import sys
from Class_PlayGame import PlayGame

# Set constants for the window.
CELL_SIZE = 20
GRID_SIZE = 30
WINDOW_SIZE = CELL_SIZE * GRID_SIZE

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("City Simulation: Game of Life")
    clock = pygame.time.Clock()
    # Initialize font (size should be slightly smaller than CELL_SIZE)
    font = pygame.font.SysFont("segoeuisymbol", 16)

    sim = PlayGame()
    sim.load_winterthur_map() # Ensure Winterthur_neu.txt is in this folder

    while sim.running:
        # Pygame's built-in event listener (Replaces pynput)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sim.running = False

            # KEYBOARD SWITCHING LOGIC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press 'R' for Random
                    sim.board = []  # Clear existing board
                    sim.load_random_city()  # Load new random city
                    print("Map switched to: Random")

                if event.key == pygame.K_w:  # Press 'W' for Winterthur
                    sim.board = []  # Clear existing board
                    sim.load_winterthur_map()
                    print("Map switched to: Winterthur")

        # Update simulation states
        sim.population_growth()
        sim.simulate_traffic()
        #sim.car_step = (sim.car_step + 1) % 30 # Loop the car back to the top

        # Draw the colorful grid
        screen.fill((0, 0, 0))
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                obj = sim.board[i][j]
                # Each object now has a .color attribute from Class_Fill
                # 1. Draw the background color square
                rect = (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
                pygame.draw.rect(screen, obj.color, rect)

                # 2. Render the character text
                # We use white (255, 255, 255) or black (0, 0, 0) for the text
                text_surface = font.render(obj.character, True, (0, 0, 0))

                # 3. Center the text in the square
                text_rect = text_surface.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2,
                                                          i * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text_surface, text_rect)

        pygame.display.flip() # Update the full display
        clock.tick(10) # 10 frames per second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()