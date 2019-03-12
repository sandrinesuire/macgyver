"""
main activity of labyrinthe
"""
import time
import pygame
from pygame.constants import *
from models.labyrinthe import Labyrinthe


# create labyrinthe instance, init the pygame window and display it
labyrinthe = Labyrinthe()
actor = labyrinthe.actor
resize = None

# display the rules of this game
labyrinthe.display_the_rules_message()

# loop during game_over == False, it will be True when actor arrive front of guardian
while not labyrinthe.game_over:
    for event in pygame.event.get():  # We go through the list of all the events received

        labyrinthe.display_message = None
        pygame.display.flip()
        if event.type == QUIT:  # If any of these events are of type QUIT
            pygame.display.flip()
            labyrinthe.game_over = True  # We stop thee loop
            # son.fadeout(300)  # Fondu à 300ms de la fin de l'objet "son"

        # if begin videoresize store the size but do nothing as the resize is not finished
        elif event.type == VIDEORESIZE:
            resize = event.size

        # when the resize is finish an event activeevent arrive, so I resize only here the window,
        elif event.type == ACTIVEEVENT and resize:
                labyrinthe.resize(resize)
                labyrinthe.display()
                resize = None

        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                actor.move([0, 1])
            if event.key == K_UP:
                actor.move([0, -1])
            if event.key == K_RIGHT:
                actor.move([1, 0])
            if event.key == K_LEFT:
                actor.move([-1, 0])

            # refresh the display
            labyrinthe.window.blit(labyrinthe.background, (0, 0))
            labyrinthe.refresh()
            if labyrinthe.display_message:
                labyrinthe.display_the_message()
            pygame.display.flip()

        # delete the rules message
        elif event.type == KEYDOWN and event.key == K_a:
            labyrinthe.window.blit(labyrinthe.background, (0, 0))
            labyrinthe.refresh()


time.sleep(3)
