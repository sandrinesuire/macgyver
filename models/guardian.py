from models.obstacles import Obstacle


class Guardian(Obstacle):
    """
    Class representing the guardian (this is the exit), he will sleep only if actor arrive with all the protections.
    """
    name = "guardian"
    image = "ressource/guardian.png"

    def front(self, actor):
        """
        If actor arrive with all the protections the gardian must sleep, if not the guardian will kill actor, so update
        the winner parameter for the actor. For all case set the game_over at True

        :param actor: the actor instance
        """
        # complexe, need explication
        # [e.name for e in labyrinth.actor.protections] get the name obstacle of all object in list of obstacle
        # all(x in ... for x in ... the before list of name) return true if all name is find
        # [k for d in labyrinth.protections for k in d] make a list of keys for exemple :
        # [{"needle": "a"}, {"needle1": "a1"}]
        # if all the protection are checked, so the guardian sleep

        won = actor.winner

        self.end_of_the_game(won)

        actor.end_of_the_game(won)

        actor.labyrinth.end_of_the_game(won)

    def end_of_the_game(self, won):
        """
        Method call at the end of the game, if the actor has all protections, he change his image with sleep

        :param won: the result of the game, won=True if actor won
        :return:
        """
        if won:
            self.image = "ressource/sleep_guardian.png"

