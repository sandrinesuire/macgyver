from models.guardian import Guardian
from models.obstacles import Obstacle
from models.protections import Protection


class Actor(Obstacle):
    """
    Class representing actor (like a wall or a protection, actor is an obstacle in the labyrinthe he have
    coordonates too)
    """
    name = "macgyver"
    image = "ressource/actor.png"
    inlife = True
    protections = []
    labyrinthe = None

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
        if x >= 0 and x < self.labyrinthe.limit_x and y >= 0 and y < self.labyrinthe.limit_y:
            # trying to move actor
            # checking if obstacle
            obstacle = self.labyrinthe.grid.get((x, y))

            if obstacle is None or isinstance(obstacle, Protection) or isinstance(obstacle, Guardian):
                # Calling front method of the obstacle depending of protection or guardian instance
                if obstacle and isinstance(obstacle, Protection):
                    self.front_protection(obstacle)
                elif obstacle and isinstance(obstacle, Guardian):
                    self.front_guardian()

                # registre the new position of actor in the grid only if not arrive to exit because i need to display
                # the front between actor and guardian
                if not self.labyrinthe.game_over:
                    # delete old position of actor in the self.grid
                    del self.labyrinthe.grid[self.x, self.y]
                    self.labyrinthe.grid[x, y] = self
                    self.x = x
                    self.y = y

    def front_protection(self, protection):
        """
        Method managing face to face with an protection (protection), the actor recovers the protection and continues
        his way

        :param protection: the protection instance
        """
        self.labyrinthe.grid[protection.x, protection.y] = None
        if protection not in self.protections:
            self.protections.append(protection)
        # needed corresponding to the missing protection to stay in alive
        needed = len(self.labyrinthe.protections) - len(self.protections)
        # display_message corresponding to the message of needed because it will be display later
        if needed > 0:
            self.labyrinthe.display_message = [protection.x, protection.y, "Plus que {}".format(needed)]
        else:
            self.labyrinthe.display_message = [protection.x, protection.y, "Objets OK"]

    def front_guardian(self):
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

        self.inlife = all(x in [e.name for e in self.protections] for x in
                          [k for d in self.labyrinthe.protections for k in d])
        if self.inlife:
            self.image = "ressource/syringe.png"
            self.labyrinthe.guardian.image = "ressource/sleep_guardian.png"
        else:
            self.image = "ressource/die.png"

        end_message = "You Won" if self.inlife else "You Die"
        self.labyrinthe.display_message = [self.x, self.y, end_message]
        self.labyrinthe.game_over = True
