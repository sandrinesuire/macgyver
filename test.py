import pygame
import time

import labyrinthe as script

import pytest

from obstacles import Actor, Guardian, Wall, Protection


class TestLabyrinthe:
    def setup_method(self):
        self.labyrinthe = script.Labyrinthe()

    # test if Protection, Wall are in grid, and test position of guardian and actor
    def test_grid_composition(self):
        assert isinstance(self.labyrinthe.grid[(1, 1)], Actor)
        assert isinstance(self.labyrinthe.grid[(14, 1)], Guardian)
        assert Wall in list(set([type(v) for c, v in self.labyrinthe.grid.items()]))
        assert Protection in list(set([type(v) for c, v in self.labyrinthe.grid.items()]))

    # test move down actor method
    def test_grid_composition(self):
        old_x, old_y = 1, 1
        self.labyrinthe.moove_actor([0, 1])
        assert isinstance(self.labyrinthe.grid[(1, 2)], Actor)

    # test move_right actor method is not possible when a wall is at right
    def test_grid_composition(self):
        old_x, old_y = 1, 1
        self.labyrinthe.moove_actor([1, 0])
        assert isinstance(self.labyrinthe.grid[(1, 1)], Actor)

    # test front method with protection and guardian
    def test_grid_composition(self):
        for (a, b), v in self.labyrinthe.grid.items():
            if v.name == 'ether':
                ether = v
                ether.x = 1
                ether.y = 2

                self.labyrinthe.grid[(a, b)] = None
            elif v.name == 'plastic_tub':
                plastic_tub = v
                plastic_tub.x = 1
                plastic_tub.y = 3

                self.labyrinthe.grid[(a, b)] = None
            elif v.name == 'needle':
                needle = v
                needle.x = 1
                needle.y = 4

                self.labyrinthe.grid[(a, b)] = None
        self.labyrinthe.grid[1, 2] = ether
        self.labyrinthe.grid[1, 3] = plastic_tub
        self.labyrinthe.grid[1, 4] = needle

        assert self.labyrinthe.actor.protections == []
        self.labyrinthe.moove_actor([0, 1])
        assert len(self.labyrinthe.actor.protections) == 1
        self.labyrinthe.moove_actor([0, 1])
        assert len(self.labyrinthe.actor.protections) == 2
        self.labyrinthe.moove_actor([0, 1])
        assert len(self.labyrinthe.actor.protections) == 3
        assert self.labyrinthe.actor.inlife == True
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([-1, 0])
        self.labyrinthe.moove_actor([-1, 0])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([-1, 0])
        self.labyrinthe.moove_actor([-1, 0])
        self.labyrinthe.moove_actor([-1, 0])
        self.labyrinthe.moove_actor([-1, 0])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([0, 1])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([-1, 0])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([0, -1])
        self.labyrinthe.moove_actor([1, 0])
        self.labyrinthe.moove_actor([1, 0])
        assert self.labyrinthe.game_over == True
        time.sleep(5)



