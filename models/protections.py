from models.obstacles import Obstacle


class Protection(Obstacle):
    """
    Class representing the protections that actor must collect to put the guardian to sleep.
    """
    name = "protection"
    image = "ressource/wood.png"

    def front(self, actor):
        """
        Method managing face to face with an protection (protection), the actor recovers the protection and continues
        his way

        :param actor: the actor concerned by the front
        """
        actor.labyrinth.grid[self.x, self.y] = None
        if self not in actor.protections:
            actor.get_protection(self)
        # needed corresponding to the missing protection to stay in alive
        needed = len(actor.labyrinth.protections) - len(actor.protections)
        # display_message corresponding to the message of needed because it will be display later
        if needed > 0:
            actor.labyrinth.display_message = [self.x, self.y, "Plus que {}".format(needed)]
        else:
            actor.labyrinth.display_message = [self.x, self.y, "Objets OK"]
            actor.winner = True
