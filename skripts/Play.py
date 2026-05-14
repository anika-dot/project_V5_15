import cProfile  # for profiling
import pstats  # for saving profiling data
from skripts.Class_PlayGame import PlayGame


def start_simulation():
    """
    Starts the Game of Life simulation with user input.
    Unser input "1": uses the winterthur map. User input "2" uses a randomly generated map.
    """

    user_choice = int(
        input(
            "Which map would you like to use to continue?\
                                         \n 1:Winterthur\
                                             \n 2:Randomly generated map\
                                                 \n choose 1 or 2."
        )
    )

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
        print("\nSimulation stopped. Generate profiling report...")
    finally:
        # Stopping recording and processing stats
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats("cumtime")

        print("\n--- PROFILING RESULTS (Top 20) ---")
        stats.print_stats(20)

        # Saving to file so we can use it for a flamegraph later
        stats.dump_stats("game_profile.prof")

# only for testing:
# If the module is imported as part of Pytest, start_simulation() should still be executed.
import os

if "PYTEST_CURRENT_TEST" in os.environ:
    start_simulation()
