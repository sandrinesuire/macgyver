# -*-coding:Utf-8 -*

"""
main activity of labyrinthe
"""

from labyrinthe import Labyrinthe
import sys

# create labyrinthe instance
labyrinthe = Labyrinthe()

# loop during game_over == False, it will be True when actor arrive front of guardian
while not labyrinthe.game_over:
    print(labyrinthe.display())
    direction = input("Please enter your mooving : ")
    direction_sens = direction[:1].lower()

    if direction_sens == "q":
        print("You exit the game")
        labyrinthe.game_over = True
        pass

    elif direction_sens in ["n", "e", "s", "w"]:
        win = labyrinthe.moove_actor(direction_sens)

    else:
        print("I don't understand your choice.")

if labyrinthe.actor.inlife  == True:
    print("You win this play")



