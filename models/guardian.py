from models.obstacles import Obstacle


class Guardian(Obstacle):
    """
    Class representing the guardian (this is the exit), he will sleep only if actor arrive with all the protections.
    """
    name = "guardian"
    image = "ressource/guardian.png"
