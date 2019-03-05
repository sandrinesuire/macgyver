from random import choice

from obstacles import Wall, Guardian, Macgyver, Protection


class Labyrinthe:
    """
    The labyrinth class corresponds to the platform of the game, it converts the file map.txt into obstalcles and
    positions the guardian as well as macgyver.

    For this activity there is only one map so for this reason I load it at initialization, in a more complex case we
    could initialize the labyrinth with the file name parameter.
    """
    limit_x = 15
    limit_y = 15
    protections_titles = ["needle", "plastic_tube", "ether"]
    obstacles_symbols = {
        "o": Wall,
        "u": Guardian
    }

    def __init__(self):
        """
        Method initializing the data and construct the grid
        """
        self.macgyver = None
        self.grid = {}
        self.game_over = False

        with open("map.txt", "r") as f:
            content = f.read()
            obstacles, self.macgyver = self._creating_obstacles(content)

        for obstacle in obstacles:
            if (obstacle.x, obstacle.y) in self.grid:
                raise ValueError("The x={} and y={} coordonate are already used.".format(obstacle.x, obstacle.y))

            if obstacle.x > self.limit_x or obstacle.y > self.limit_y:
                raise ValueError("The coordinates x={} or y={} of the obstacle exceed the grid".format(obstacle.x,
                                                                                                       obstacle.y))
            self.grid[obstacle.x, obstacle.y] = obstacle

        self._place_protections()

    def _creating_obstacles(self, file_content):
        """
        Static method creating a list of obstacles coordonates from a map content file
        :param file_content:
        :return: the list of obstacles coordonates
        """
        x = 0
        y = 0
        obstacles = []
        macgyver = None
        for letter in file_content:
            if letter == "\n":
                x = 0
                y += 1
                continue
            elif letter.lower() == " ":
                pass
            elif letter.lower() == "x":
                macgyver = Macgyver(x, y)
            elif letter.lower() in self.obstacles_symbols:
                model = self.obstacles_symbols[letter.lower()]
                obstacle = model(x, y)
                obstacles.append(obstacle)
            else:
                raise ValueError("unknown symbol {}".format(letter))

            x += 1
        return obstacles, macgyver

    def display(self):
        """
        Method returning the string representing the labyrinth.
        We take the limits to display the grid. Obstacles and macgyver are displayed using their class attribute
        'symbol'.
        """
        y = 0
        printer_grid = ""

        while y < self.limit_y:
            x = 0
            while x < self.limit_x:
                case = self.grid.get((x, y))
                if case:
                    printer_grid += case.symbol
                else:
                    printer_grid += " "

                x += 1

            printer_grid += "\n"
            y += 1

        return printer_grid

    def move_macgyver(self, direction):
        """
        Method moving macgyver.
        The direction is to specify in the form of chain, "north", "east", "south", or "west".
        If macgyver encounters an obstacle we deal with the confrontation.
        """
        coords = [self.macgyver.x, self.macgyver.y]
        directions = {"north": [1, -1], "east": [0, 1], "south": [1, 1], "west": [0, -1]}
        if direction in directions:
            coords[directions[direction][0]] == directions[direction][1]
        else:
            raise ValueError("unknown direction {}".format(direction))

        x, y = coords
        if x >= 0 and x < self.limit_x and y >= 0 and y < self.limit_y:
            # trying to move macgyver
            # checking if obstacle
            obstacle = self.grid.get((x, y))
            if obstacle is None:
                # delete old position of macgyver in the self.grid
                del self.grid[self.macgyver.x, self.macgyver.y]

                # registre the new position of macgyver in the grid
                self.grid[x, y] = self.macgyver
                self.macgyver.x = x
                self.macgyver.y = y

                # Calling front method of the obstacle if existing
                if obstacle:
                    obstacle.front(self)
                return True

        return False

    def _place_protections(self):
        """
        Method random placing all the macgyver needed protections.
        :return: Nothing
        """
        grid = self.grid
        frees = []
        x = 0
        y = 0

        # Finding the limits x and y of the grid
        l_x = self.limit_x
        l_y = self.limit_y
        while l_x > 0:
            if (l_x, 0) in grid:
                break
            l_x -= 1

        while l_y > 0:
            if (0, l_y) in grid:
                break
            l_y -= 1

        while y < l_y:
            x = 0
            while x < l_x:
                if (x, y) not in grid:
                    frees.append((x, y))
                x += 1
            y += 1

        for protection_title in self.protections_titles:
            x, y = choice(frees)
            frees.remove((x, y))
            protection = Protection(x, y, protection_title)
            self.grid[x, y] = protection
