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


class Space(Obstacle):
    """
    Class representing a a space in labyrinth. Just use for understanding the file map, to know where is the space.
    """
    name = "space"
    image = " "


class Wall(Obstacle):
    """
    Class representing a piece of wall.
    """
    name = "wall"
    image = "ressource/wood.png"
