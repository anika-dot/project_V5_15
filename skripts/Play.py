import cProfile     #for profiling
import pstats       #for saving profiling data
from skripts.Class_PlayGame import PlayGame


def start_simulation():
    """
    Starts the Game of Life simulation with user input.
    Unser input "1": uses the winterthur map. User input "2" uses a randomly generated map.
    """

    user_choice = int(input("Mit welcher Karte möchten Sie weiterfahren?\
                                         \n 1:Winterthur\
                                             \n 2:Zufällig generierte Karte\
                                                 \n wählen Sie 1 oder 2."))

    if user_choice == 1:
        simulation = PlayGame()
        simulation.play_winterthur_map()

    elif user_choice == 2:
        simulation = PlayGame()
        simulation.play_random_map()


if __name__ == "__main__":
    # Initializing the profiler
    profiler = cProfile.Profile()

    try:
        # Starting the recording and running the simulation
        profiler.enable()
        start_simulation()
    except KeyboardInterrupt:
        print("\nSimulation gestoppt. Erstelle Profiling-Bericht...")
    finally:
        # Stopping recording and processing stats
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('cumtime')

        print("\n--- PROFILING ERGEBNISSE (Top 20) ---")
        stats.print_stats(20)

        # Saving to file so we can use it for a flamegraph later
        stats.dump_stats("game_profile.prof")