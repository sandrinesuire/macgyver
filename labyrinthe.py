import pygame
from random import choice

from pygame.constants import RESIZABLE

from obstacles import Wall, Guardian, Actor, Protection, Space


class Labyrinthe:
    """
    The labyrinth class corresponds to the platform of the game, it converts the file map.txt into obstalcles and
    positions the guardian, the protections and the actor (macgyver).

    For this activity there is only one map so for this reason I load it at initialization, in a more complex case we
    could initialize the labyrinth with the file name parameter, and adding a card model to construct the map.
    """
    # find below the parameters for the map_file. You can change the width (limit_x) and the length (limit_y).
    # you can change the symbols of the obstacles (Wall, Guardian, Actor, Space), you can adapte the file name 's map...
    limit_x = 15
    limit_y = 15
    protections = [
        {"needle": "ressource/needle.png"},
        {"plastic_tub": "ressource/plastic_tub.png"},
        {"ether": "ressource/ether.png"}
    ]
    symbols = {
        "o": Wall,
        "u": Guardian,
        "x": Actor,
        " ": Space
    }
    map_file = "map.txt"
    width = 0
    height = 0
    bloc_y = 0
    bloc_x = 0
    display_message = None

    def __init__(self):
        """
        Method initializing the data and construct the grid. The grid is a dictionnary composed of "key" coordinate
        tuple and "value" obstacle instance. An obstacle instance can be the guardian, a wall, a protection, the actor.
        """
        # pygame initialization
        pygame.init()
        self.window = pygame.display.set_mode((600, 600), RESIZABLE)
        self.background = pygame.image.load("ressource/background.jpg").convert_alpha()
        self.son = pygame.mixer.Sound("ressource/test.wav")
        self.icon = pygame.image.load("ressource/logo.png")

        # calculate all dimensions
        self.resize()

        self.myfont = pygame.font.SysFont('Comic Sans MS', int(self.bloc_x / 4 * 3))
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("MacGyver need your help !")
        pygame.key.set_repeat(400, 30)

        self.grid = {}
        self.game_over = False

        self._place_obstacles()

        self._place_protections()

        self.display()

    def _place_obstacles(self):
        """
        Method reading the map.txt and create an instance for all obstacle and place then in the grid
        :return: Nothing
        """
        with open(self.map_file, "r") as f:
            content = f.read()
            obstacles, self.actor, self.guardian = self._creating_obstacles(content)
        for obstacle in obstacles:
            if (obstacle.x, obstacle.y) in self.grid:
                raise ValueError("The x={} and y={} coordonates are already used.".format(obstacle.x, obstacle.y))

            if obstacle.x > self.limit_x or obstacle.y > self.limit_y:
                raise ValueError("The coordinates x={} or y={} of the obstacle exceed the grid".format(obstacle.x,
                                                                                                       obstacle.y))
            self.grid[obstacle.x, obstacle.y] = obstacle

    def resize(self, size=None):
        """
        Methode calculate the window size and bloc

        :param size: the tupple of size
        """
        # calculate size of a block and window
        print("resize")
        if size:
            self.width, self.height = size
            self.window = pygame.display.set_mode(size, RESIZABLE)
        else:

            self.width, self.height = pygame.display.get_surface().get_size()
        self.width = int(self.width)
        self.height = int(self.height)
        self.bloc_y = int(self.height / self.limit_y)
        self.bloc_x = int(self.width / self.limit_x)
        # the window size is configurable, the number of bloc too so we need to scale all image for correspondind to
        # window size and bloc size
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.window.blit(self.background, (0, 0))

    def _creating_obstacles(self, file_content):
        """
        Private method creating a list of obstacles coordonates from a map content file. Private just mean this method
        should not be use outside this class, in python nothing will prevent in spite of everything, its use

        :param file_content: the content file of the map
        :return: the list of obstacles coordonates, and the actor instance
        """
        x = 0
        y = 0
        obstacles = []
        actor = None
        guardian = None
        for letter in file_content:
            # if I  find a \n it is because i am at the end of the line in map file, so x must be set to 0 and i must
            # add 1 to y coordonnate
            if letter == "\n":
                x = 0
                y += 1
                continue
            elif self.symbols[letter.lower()] == Space:
                # I do nothing for space, the model exist but I don't need to instancie it, I need the model to
                # parameter the symbol in file
                pass
            elif self.symbols[letter.lower()] == Actor:
                actor = Actor(x, y)
                obstacles.append(actor)
            elif self.symbols[letter.lower()] == Guardian:
                guardian = Guardian(x, y)
                obstacles.append(guardian)
            elif letter.lower() in self.symbols.keys():
                model = self.symbols[letter.lower()]
                obstacle = model(x, y)
                obstacles.append(obstacle)
            else:
                raise ValueError("unknown symbol {}".format(letter))

            x += 1
        return obstacles, actor, guardian

    def display(self):
        """
        Method returning the string representing of the map.
        We take the limits to display the grid. Obstacles and actor are displayed using their class attribute
        'repr'.
        """
        y = 0

        while y < self.limit_y:
            x = 0
            while x < self.limit_x:
                case = self.grid.get((x, y))
                if case:
                    piece = pygame.image.load(case.repr).convert_alpha()
                    piece = pygame.transform.scale(piece, (self.bloc_x, self.bloc_y))
                    self.window.blit(piece, (x*self.bloc_x, y*self.bloc_y))
                x += 1
            y += 1

        pygame.display.flip()

    def display_the_rules_message(self):
        """
        Method display the message
        """
        # we display a info bulle to give the number of missing protections, the coordonates of display depending
        # of the coordonates of the actor, while being careful not to go over the window
        bulle = pygame.image.load("ressource/bulle.png").convert_alpha()
        bulle = pygame.transform.scale(bulle, (self.width, self.height))

        rules = "Règles du jeu : Vous devez aider"
        rules1 = "MacGyver à récupérer des objects"
        rules2 = "(aiguille, tube plastique et ether)"
        rules3 = "s'il manque un des objets à  MacGyver"
        rules4 = "lorsqu'il arrive à la sortie c'est PERDU"
        rules5 = "Dirigez vous avec les flèches du clavier"
        rules6 = "Appuyer sur la touche 'A' pour jouer"

        myfont = pygame.font.SysFont('Comic Sans MS', int(self.bloc_x))
        self.window.blit(bulle, (0, 0))
        self.window.blit(myfont.render(rules, False, (0, 0, 0)), (20, self.bloc_x *2))
        self.window.blit(myfont.render(rules1, False, (0, 0, 0)), (20, self.bloc_x * 3))
        self.window.blit(myfont.render(rules2, False, (0, 0, 0)), (20, self.bloc_x * 4))
        self.window.blit(myfont.render(rules3, False, (0, 0, 0)), (20, self.bloc_x * 5))
        self.window.blit(myfont.render(rules4, False, (0, 0, 0)), (20, self.bloc_x * 6))
        self.window.blit(myfont.render(rules5, False, (0, 0, 0)), (20, self.bloc_x * 7))
        self.window.blit(myfont.render(rules6, False, (0, 0, 0)), (20, self.bloc_x * 8))

    def display_the_message(self):
        """
        Method display the message
        """
        # we display a info bulle to give the number of missing protections, the coordonates of display depending
        # of the coordonates of the actor, while being careful not to go over the window
        bulle = pygame.image.load("ressource/bulle.png").convert_alpha()
        bulle = pygame.transform.scale(bulle, (3 * self.bloc_x, 1 * self.bloc_y))

        loc_x_bulle = self.display_message[0] * self.bloc_x

        # i place the message above the actor so i remove 1 to the y coordonate
        loc_y_bulle = (self.display_message[1] - 1) * self.bloc_x

        # to not display the message outside the window I recalculate the message position
        if loc_x_bulle > self.width - 3 * self.bloc_x:
            loc_x_bulle = self.width - 3 * self.bloc_x
        if loc_y_bulle > self.height - 1 * self.bloc_y:
            loc_y_bulle = self.height - 1 * self.bloc_y

        self.window.blit(bulle, (loc_x_bulle, loc_y_bulle))
        self.window.blit(self.myfont.render(self.display_message[2], False, (0, 0, 0)),
                         (loc_x_bulle + 5, loc_y_bulle + 5))
        self.son.play()

    def refresh(self):
        """
        Method refreshing all positions of obstacles
        """
        self.display()

    def _place_protections(self):
        """
        Private method random placing all the actor needed protections.
        """
        grid = self.grid
        frees = []
        x = 0
        y = 0

        # for each case in width and each case in length, if the tuple of coordonnate are not find in grid, so iy is a
        # free case
        for x in range(self.limit_x):
            for y in range(self.limit_y):
                if(x, y) not in grid:
                    frees.append((x, y))

        for protection in self.protections:
            title, repr = list(protection.items())[0]
            # i choose by chance a free place to place one of the needed protection, i remove this free place, and add
            # the instance in the grid
            x, y = choice(frees)
            frees.remove((x, y))
            obj_protect = Protection(x, y, title, repr)
            self.grid[x, y] = obj_protect

    def moove_actor(self, direction):
        """
        Method moving actor.
        The direction is to specify in the form of coordonnate (x, y).
        If actor encounters an obstacle we deal with the confrontation.

        :param direction: the direction to moove this actor
        """
        # affected the change of direction to coords
        coords = [self.actor.x, self.actor.y]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if direction in directions:
            coords[0] += direction[0]
            coords[1] += direction[1]
        else:
            raise ValueError("unknown direction {}".format(direction))

        x, y = coords
        if x >= 0 and x < self.limit_x and y >= 0 and y < self.limit_y:
            # trying to move actor
            # checking if obstacle
            obstacle = self.grid.get((x, y))

            if obstacle is None or isinstance(obstacle, Protection) or isinstance(obstacle, Guardian):
                # Calling front method of the obstacle if existing
                if obstacle:
                    obstacle.front(self)
                if self.display_message:
                    self.display_the_message()

                # registre the new position of actor in the grid only if not arrive to exit because i need to display
                # the front between actor and guardian
                if not self.game_over:
                    # delete old position of actor in the self.grid
                    del self.grid[self.actor.x, self.actor.y]
                    self.grid[x, y] = self.actor
                    self.actor.x = x
                    self.actor.y = y

        self.window.blit(self.background, (0, 0))
        self.refresh()
