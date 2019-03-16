import unittest
import time

from models.actor import Actor
from models.guardian import Guardian
from models.obstacles import Wall
from models.protections import Protection
from models import labyrinth as script


class TestLabyrinth(unittest.TestCase):
    def setUp(self):
        self.labyrinth = script.Labyrinth()
        self.actor = self.labyrinth.actor

    # test if Protection, Wall are in grid, and test position of guardian and actor
    def test_grid_composition(self):
        assert isinstance(self.labyrinth.grid[(1, 1)], Actor)
        assert isinstance(self.labyrinth.grid[(14, 1)], Guardian)
        assert Wall in list(set([type(v) for c, v in self.labyrinth.grid.items()]))
        assert Protection in list(set([type(v) for c, v in self.labyrinth.grid.items()]))

    # test move down actor method
    def test_move_actor(self):
        self.actor.move([0, 1])
        assert isinstance(self.labyrinth.grid[(1, 2)], Actor)

    # test move_right actor method is not possible when a wall is at right
    def test_move_actor1(self):
        self.actor.move([1, 0])
        assert isinstance(self.labyrinth.grid[(1, 1)], Actor)

    # test front method with protection and guardian
    def test_front_obstacle(self):
        ether, needle, plastic_tub = None, None, None
        for (a, b), v in self.labyrinth.grid.items():
            if v.name == 'ether':
                ether = v
                ether.x = 1
                ether.y = 2

                self.labyrinth.grid[(a, b)] = None
            elif v.name == 'plastic_tub':
                plastic_tub = v
                plastic_tub.x = 1
                plastic_tub.y = 3

                self.labyrinth.grid[(a, b)] = None
            elif v.name == 'needle':
                needle = v
                needle.x = 1
                needle.y = 4

                self.labyrinth.grid[(a, b)] = None
        self.labyrinth.grid[1, 2] = ether
        self.labyrinth.grid[1, 3] = plastic_tub
        self.labyrinth.grid[1, 4] = needle

        assert self.labyrinth.actor.protections == []
        self.actor.move([0, 1])
        assert len(self.labyrinth.actor.protections) == 1
        self.actor.move([0, 1])
        assert len(self.labyrinth.actor.protections) == 2
        self.actor.move([0, 1])
        assert len(self.labyrinth.actor.protections) == 3
        self.assertTrue(self.labyrinth.actor.winner)

        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([-1, 0])
        self.actor.move([-1, 0])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([-1, 0])
        self.actor.move([-1, 0])
        self.actor.move([-1, 0])
        self.actor.move([-1, 0])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([0, 1])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([1, 0])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([-1, 0])
        self.actor.move([0, -1])
        self.actor.move([0, -1])
        self.actor.move([1, 0])
        self.actor.move([1, 0])
        self.assertTrue(self.labyrinth.game_over)
        time.sleep(5)
