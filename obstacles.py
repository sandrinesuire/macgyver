class Obstacle:
    """
    Class representing all obstacles class.
    """
    name = "obstacle"
    repr = ""

    def __init__(self, x, y, name=None, repr=None):
        self.x = x
        self.y = y
        if name:
            self.name = name
        if repr:
            self.repr = repr

    def __repr__(self):
        return "<{name} (x={x}, y={y})>".format(name=self.name, x=self.x, y=self.y)

    def __str__(self):
        return "{name} ({x}.{y})".format(name=self.name, x=self.x, y=self.y)

    def front(self, labyrinthe):
        """
        Method call when actor arrive in case of with an obstacle instance. This method must be redefined in 
        child class.
        """
        pass


class Space(Obstacle):
    """
    Class representing a a space in labyrinthe. Just use for understanding the file map, to know where is the space.
    """
    name = "space"
    repr = " "


class Wall(Obstacle):
    """
    Class representing a piece of wall.
    """
    name = "wall"
    repr = "ressource/wood.png"


class Guardian(Obstacle):
    """
    Class representing the guardian (this is the exit), he will sleep only if actor arrive with all the protections.
    """
    name = "guardian"
    repr = "ressource/guardian.png"

    def front(self, labyrinthe):
        """
        If actor arrive with all the protections the gardian must sleep, if not the guardian will kill actor, so set
        the inlife parameter in fonction. For all case set the game_over at True
        
        :param labyrinthe: the labyrinthe instance
        """

        labyrinthe.actor.inlife = all(protection in labyrinthe.protections for protection in
                                      [e.name for e in labyrinthe.actor.protections])
        labyrinthe.game_over = True


class Protection(Obstacle):
    """
    Class representing the protections that actor must collect to put the guardian to sleep.
    """
    name = "protection"
    repr = "ressource/wood.png"

    def front(self, labyrinthe):
        """
        Recovers the protections in the actor protections parameter and frees the passage

        :param labyrinthe: the labyrinthe instance
        """
        labyrinthe.grid[self.x, self.y] = None
        labyrinthe.actor.protections.append(self)


class Actor(Obstacle):
    """
    Class representing actor (like a wall or a protection, actor is an obstacle in the labyrinthe he have
    coordonates too)
    """
    name = "macgyver"
    repr = "ressource/actor.png"
    inlife = True
    protections = []
