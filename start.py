"""
main activity of labyrinthe
"""
import pygame
from pygame.constants import *

from labyrinthe import Labyrinthe

# pygame initialisation
pygame.init()

window = pygame.display.set_mode((600, 600), RESIZABLE)
background = pygame.image.load("ressource/background.jpg").convert()
window.blit(background, (0, 0))
pygame.key.set_repeat(400, 30)

# create labyrinthe instance and display it
labyrinthe = Labyrinthe()
labyrinthe.display(window)
pygame.display.flip()

# loop during game_over == False, it will be True when actor arrive front of guardian
while not labyrinthe.game_over:
    for event in pygame.event.get():  # We go through the list of all the events received
        if event.type == QUIT:  # If any of these events are of type QUIT
            labyrinthe.game_over = True  # We stop thee loop
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                labyrinthe.moove_actor("s")
            if event.key == K_UP:
                labyrinthe.moove_actor("n")
            if event.key == K_RIGHT:
                labyrinthe.moove_actor("e")
            if event.key == K_LEFT:
                labyrinthe.moove_actor("w")
        background = pygame.image.load("ressource/background.jpg").convert()
        window.blit(background, (0, 0))
        labyrinthe.display(window)
        pygame.display.flip()

if labyrinthe.actor.inlife:
    print("You win this play")

