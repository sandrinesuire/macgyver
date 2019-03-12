class Obstacle:
    """
    Class representing all obstacles class.
    """
    name = "obstacle"
    image = ""

    def __init__(self, x, y, name=None, image=None):
        self.x = x
        self.y = y
        if name:
            self.name = name
        if image:
            self.image = image

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
    image = " "


class Wall(Obstacle):
    """
    Class representing a piece of wall.
    """
    name = "wall"
    image = "ressource/wood.png"


class Guardian(Obstacle):
    """
    Class representing the guardian (this is the exit), he will sleep only if actor arrive with all the protections.
    """
    name = "guardian"
    image = "ressource/guardian.png"

    def front(self, labyrinthe):
        """
        If actor arrive with all the protections the gardian must sleep, if not the guardian will kill actor, so set
        the inlife parameter in fonction. For all case set the game_over at True
        
        :param labyrinthe: the labyrinthe instance
        """
        # complexe, need explication
        # [e.name for e in labyrinthe.actor.protections] get the name obstacle of all object in list of obstacle
        # all(x in ... for x in ... the before list of name) return true if all name is find
        # [k for d in labyrinthe.protections for k in d] make a list of keys for exemple :
        # [{"needle": "a"}, {"needle1": "a1"}]
        # if all the protection are checked, so the guardian sleep

        labyrinthe.actor.inlife = all(x in [e.name for e in labyrinthe.actor.protections] for x in
                                      [k for d in labyrinthe.protections for k in d])
        if labyrinthe.actor.inlife:
            labyrinthe.actor.image = "ressource/syringe.png"
            labyrinthe.guardian.image = "ressource/sleep_guardian.png"
        else:
            labyrinthe.actor.image = "ressource/die.png"

        end_message = "You Won" if labyrinthe.actor.inlife else "You Die"
        labyrinthe.display_message = [self.x, self.y, end_message]
        labyrinthe.game_over = True


class Protection(Obstacle):
    """
    Class representing the protections that actor must collect to put the guardian to sleep.
    """
    name = "protection"
    image = "ressource/wood.png"

    def front(self, labyrinthe):
        """
        Recovers the protections in the actor protections parameter and frees the passage

        :param labyrinthe: the labyrinthe instance
        """
        labyrinthe.grid[self.x, self.y] = None
        if self not in labyrinthe.actor.protections:
            labyrinthe.actor.protections.append(self)
        # needed corresponding to the missing protection to stay in alive
        needed = len(labyrinthe.protections) - len(labyrinthe.actor.protections)
        # display_message corresponding to the message of needed because it will be display later
        if needed > 0:
            labyrinthe.display_message = [self.x, self.y, "Plus que {}".format(needed)]
        else:
            labyrinthe.display_message = [self.x, self.y, "Objets OK"]


class Actor(Obstacle):
    """
    Class representing actor (like a wall or a protection, actor is an obstacle in the labyrinthe he have
    coordonates too)
    """
    name = "macgyver"
    image = "ressource/actor.png"
    inlife = True
    protections = []
