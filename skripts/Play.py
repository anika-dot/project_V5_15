from Class_PlayGame import PlayGame

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
