from Class_PlayGame import PlayGame

user_choice = int(input("Mit welcher Karte möchten Sie weiterfahren?\
                                     \n 1:Winterthur\
                                         \n 2:Zufällig generierte Karte\
                                             \n wählen Sie 1 oder 2."))
       
if user_choice == 1:
    g = PlayGame()
    g.play()
            
elif user_choice == 2:
    g = PlayGame()
    g.play_random()