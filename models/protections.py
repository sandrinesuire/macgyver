from models.obstacles import Obstacle


class Protection(Obstacle):
    """
    Class representing the protections that actor must collect to put the guardian to sleep.
    """
    name = "protection"
    image = "ressource/wood.png"
