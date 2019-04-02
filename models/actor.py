from models.guardian import Guardian
from models.obstacles import Obstacle
from models.protections import Protection


class Actor(Obstacle):
    """
    Class representing actor (like a wall or a protection, actor is an obstacle in the labyrinth he have
    coordonates too)
    """
    name = "macgyver"
    image = "actor.png"
    winner = False
    protections = []
    labyrinth = None

    def move(self, direction):
        """
        Method moving actor.
        The direction is to specify in the form of coordonnate (x, y).
        If actor encounters an obstacle we deal with the confrontation.

        :param direction: the direction to moove this actor
        """
        # affected the change of direction to coords
        coords = [self.x, self.y]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if direction in directions:
            coords[0] += direction[0]
            coords[1] += direction[1]
        else:
            raise ValueError("unknown direction {}".format(direction))

        x, y = coords
        if x >= 0 and x < self.labyrinth.limit_x and y >= 0 and y < self.labyrinth.limit_y:
            # trying to move actor
            # checking if obstacle
            obstacle = self.labyrinth.grid.get((x, y))

            if obstacle is None or isinstance(obstacle, Protection) or isinstance(obstacle, Guardian):
                # Calling front method of the obstacle depending of protection or guardian instance
                if obstacle:
                    obstacle.front(self)

                # registre the new position of actor in the grid only if not arrive to exit because i need to display
                # the front between actor and guardian
                if not self.labyrinth.game_over:
                    # delete old position of actor in the self.grid
                    del self.labyrinth.grid[self.x, self.y]
                    self.labyrinth.grid[x, y] = self
                    self.x = x
                    self.y = y

    def get_protection(self, protection):
        """
        Method getting protection in parameter protections

        :param protection: the protection
        :return:
        """
        self.protections.append(protection)

    def end_of_the_game(self, won):
        """
        Method call at the end of the game, if the actor has all protections, he change his image with the syringe, to
        explain that he endures the guardian, if not he change his image with the dead

        :param won: the result of the game
        :return:
        """
        if won:
            self.image = "syringe.png"
        else:
            self.image = "die.png"
