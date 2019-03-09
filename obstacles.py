import time


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
        # complexe, need explication
        # [e.name for e in labyrinthe.actor.protections] get the name obstacle of all object in list of obstacle
        # all(protection in ... for protection in ... the before list of name) return true if all name is find
        # [k for d in labyrinthe.protections for k in d] make a list of keys for exemple :
        # [{"needle": "a"}, {"needle1": "a1"}]

        labyrinthe.actor.inlife = all(x in [e.name for e in labyrinthe.actor.protections] for x in [k for d in labyrinthe.protections for k in d])
        print(labyrinthe.actor.inlife)
        end_message = "You Won" if labyrinthe.actor.inlife else "You Lost"
        labyrinthe.display_message = [self.x, self.y, end_message]
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
        if self not in labyrinthe.actor.protections:
            labyrinthe.actor.protections.append(self)
        # needed corresponding to the missing protection to stay in alive
        needed = len(labyrinthe.protections) - len(labyrinthe.actor.protections)
        # display_message corresponding to the message of needed because it will be display later
        labyrinthe.display_message = [self.x, self.y, "Plus que {}".format(needed)]

        # if all the protection are checked, so the guardian sleep
        all_checked = all(x in [e.name for e in labyrinthe.actor.protections] for x in [k for d in labyrinthe.protections for k in d])
        if all_checked:
            labyrinthe.guardian.repr = "ressource/sleep_guardian.png"



class Actor(Obstacle):
    """
    Class representing actor (like a wall or a protection, actor is an obstacle in the labyrinthe he have
    coordonates too)
    """
    name = "macgyver"
    repr = "ressource/actor.png"
    inlife = True
    protections = []
