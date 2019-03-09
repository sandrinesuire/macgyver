"""
main activity of labyrinthe
"""

from labyrinthe import Labyrinthe

# create labyrinthe instance and display
labyrinthe = Labyrinthe()
window = labyrinthe.display()

# loop during game_over == False, it will be True when actor arrive front of guardian
while not labyrinthe.game_over:
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

if labyrinthe.actor.inlife:
    print("You win this play")

