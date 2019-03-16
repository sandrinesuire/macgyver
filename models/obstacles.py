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

    def front(self, actor):
        """
        Method call when actor arrive in case of with an obstacle instance. This method must be redefined in
        child class.

        :param actor: the actor concerned by the front
        """
        pass

    def end_of_the_game(self, won):
        """
        Method call at the end of the game. This method must be redefined in
        child class.

        :param won: the result of the game
        """
        pass


class Space(Obstacle):
    """
    Class representing a a space in labyrinth. Just use for understanding the file map, to know where is the space.
    """
    name = "space"
    image = " "
