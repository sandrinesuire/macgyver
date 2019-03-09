"""
main activity of labyrinthe
"""
import pygame
from pygame.constants import *

from labyrinthe import Labyrinthe

# pygame initialisation
pygame.init()

# window size and color
window = pygame.display.set_mode((600, 600), RESIZABLE)
background = pygame.image.load("ressource/background.jpg").convert()
window.blit(background, (0, 0))
#Icone
icone = pygame.image.load("ressource/tile-crusader-logo.png")
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption("MacGyver need your help !")
pygame.key.set_repeat(400, 30)

# create labyrinthe instance and display it
labyrinthe = Labyrinthe()
labyrinthe.display(window)
pygame.display.flip()

# sound of quit
son = pygame.mixer.Sound("ressource/test.wav")

# font and message parameter
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))

# loop during game_over == False, it will be True when actor arrive front of guardian
while not labyrinthe.game_over:
    for event in pygame.event.get():  # We go through the list of all the events received
        if event.type == QUIT:  # If any of these events are of type QUIT
            window.blit(textsurface, (0, 0))
            son.play()
            pygame.display.flip()
            # labyrinthe.game_over = True  # We stop thee loop
            # son.fadeout(300)  # Fondu à 300ms de la fin de l'objet "son"

        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                labyrinthe.moove_actor("s")
            if event.key == K_UP:
                labyrinthe.moove_actor("n")
            if event.key == K_RIGHT:
                labyrinthe.moove_actor("e")
            if event.key == K_LEFT:
                labyrinthe.moove_actor("w")

            window.blit(background, (0, 0))
            labyrinthe.refresh(window)

            pygame.display.flip()

if labyrinthe.actor.inlife:
    print("You win this play")
