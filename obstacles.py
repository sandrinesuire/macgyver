from abc import ABC


class Obstacle(ABC):
    """
    Class abstract representing all obstacle class.
    """

    name = "obstacle"
    symbol = ""

    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        if name:
            self.name = name

    def __repr__(self):
        return "<{name} (x={x}, y={y})>".format(name=self.name, x=self.x, y=self.y)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)

    def front(self, labyrinthe):
        """
        Method call when macgyver arrive in front of a instance. This method must be redefined in child class.
        """
        pass


class Wall(Obstacle):
    """
    Class representing a piece of wall.
    """

    name = "wall"
    symbol = "O"


class Guardian(Obstacle):
    """
    Class representing the guardian (this is the exit), he will sleep only if macgyver arrive with all the protections.
    """

    name = "guardian"
    symbol = "U"

    def front(self, labyrinthe):
        """
        If macgyver arrive with all the protections the gardian must sleep, if not the guardian will kill macgyver
        """
        # take all protection_title in labyrinthe.protections_titles and verifying that existing in one of all
        # labyrinthe.macgyver.protections name

        labyrinthe.macgyver.inlife = all(protection_title in labyrinthe.protections_titles for protection_title in
                             [e.name for e in labyrinthe.macgyver.protections])
        labyrinthe.game_over = True


class Protection(Obstacle):
    """
    Class representing the protections that macgyver must collect to put the guardian to sleep.
    """
    name = "protection"
    symbol = "Y"

    def front(self, labyrinthe):
        """
        Recovers the protections and frees the passage
        """
        labyrinthe.macgyver.protections.append(self)


class Macgyver(Obstacle):
    """
    Class representing macgyver (like a wall or a protection, macgyver is an obstacle in the labyrinthe he have
    coordonates too)
    """
    name = "macgyver"
    symbol = "X"
    protections = []

