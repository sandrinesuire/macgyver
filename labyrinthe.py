from random import choice

from obstacles import Wall, Guardian, Actor, Protection, Space


class Labyrinthe:
    """
    The labyrinth class corresponds to the platform of the game, it converts the file map.txt into obstalcles and
    positions the guardian, the protections and the actor (macgyver).

    For this activity there is only one map so for this reason I load it at initialization, in a more complex case we
    could initialize the labyrinth with the file name parameter, and adding a card model to construct the map.
    """
    # find below the parameters for the map_file. You can change the width (limit_x) and the length (limit_y).
    # you can change the symbols of the obstacles (Wall, Guardian, Actor, Space), you can adapte the file name 's map.
    limit_x = 15
    limit_y = 15
    protections_titles = ["needle", "plastic_tube", "ether"]
    symbols = {
        "o": Wall,
        "u": Guardian,
        "x": Actor,
        " ": Space
    }
    map_file = "map.txt"

    def __init__(self):
        """
        Method initializing the data and construct the grid. The grid is a dictionnary composed of "key" coordinate
        tuple and "value" obstacle instance. An obstacle instance can be the guardian, a wall, a protection, the actor.
        """
        self.actor = None
        self.grid = {}
        self.game_over = False

        with open(self.map_file, "r") as f:
            content = f.read()
            obstacles, self.actor = self._creating_obstacles(content)

        for obstacle in obstacles:
            if (obstacle.x, obstacle.y) in self.grid:
                raise ValueError("The x={} and y={} coordonates are already used.".format(obstacle.x, obstacle.y))

            if obstacle.x > self.limit_x or obstacle.y > self.limit_y:
                raise ValueError("The coordinates x={} or y={} of the obstacle exceed the grid".format(obstacle.x,
                                                                                                       obstacle.y))
            self.grid[obstacle.x, obstacle.y] = obstacle

        self._place_protections()

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
            elif letter.lower() in self.symbols.keys():
                model = self.symbols[letter.lower()]
                obstacle = model(x, y)
                obstacles.append(obstacle)
            else:
                raise ValueError("unknown symbol {}".format(letter))

            x += 1
        return obstacles, actor

    def display(self):
        """
        Method returning the string representing of the map.
        We take the limits to display the grid. Obstacles and actor are displayed using their class attribute
        'repr'.

        :return: the string representation of the map
        """
        y = 0
        printer_grid = ""

        while y < self.limit_y:
            x = 0
            while x < self.limit_x:
                case = self.grid.get((x, y))
                if case:
                    printer_grid += case.repr
                else:
                    printer_grid += " "

                x += 1

            printer_grid += "\n"
            y += 1

        return printer_grid

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

        for protection_title in self.protections_titles:
            # i choose by chance a free place to place one of the needed protection, i remove this free place, and add
            # the instance in the grid
            x, y = choice(frees)
            frees.remove((x, y))
            protection = Protection(x, y, protection_title)
            self.grid[x, y] = protection

    def moove_actor(self, direction):
        """
        Method moving actor.
        The direction is to specify in the form of chain, "north", "east", "south", or "west".
        If actor encounters an obstacle we deal with the confrontation.

        :param direction: the direction to moove this actor
        :return: True or False if the moove is authorized
        """
        lettre = direction
        directions = {
            "e": "east",
            "s": "south",
            "w": "west",
            "n": "north",
        }

        direction = directions[lettre]

        # affected the change of direction to coords
        coords = [self.actor.x, self.actor.y]
        directions = {"north": [1, -1], "east": [0, 1], "south": [1, 1], "west": [0, -1]}
        if direction in directions:
            coords[directions[direction][0]] += directions[direction][1]
        else:
            raise ValueError("unknown direction {}".format(direction))

        x, y = coords
        if x >= 0 and x < self.limit_x and y >= 0 and y < self.limit_y:
            # trying to move actor
            # checking if obstacle
            obstacle = self.grid.get((x, y))
            if obstacle is None or isinstance(obstacle, Protection) or isinstance(obstacle, Guardian):
                # delete old position of actor in the self.grid
                del self.grid[self.actor.x, self.actor.y]

                # registre the new position of actor in the grid
                self.grid[x, y] = self.actor
                self.actor.x = x
                self.actor.y = y

                # Calling front method of the obstacle if existing
                if obstacle:
                    obstacle.front(self)
                return True
        print("You can't moove here")
        return False
