#!/usr/bin/env python3

from collections import defaultdict


class Santa(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.houses = defaultdict(int)

        # first house gets a present
        self.houses[(0, 0)] += 1

    def move(self, direction):
        moves = {
            "^": "self.y += 1",
            "v": "self.y -= 1",
            ">": "self.x += 1",
            "<": "self.x -= 1",
        }
        exec(moves[direction])
        self.houses[(self.x, self.y)] += 1


def one_santa(directions: str) -> int:
    santa = Santa()
    for d in directions:
        santa.move(d)
    return len(santa.houses)


def two_santas(directions: str) -> int:
    santa = Santa()
    robot = Santa()
    for n, d in enumerate(directions):
        if n % 2 == 0:
            santa.move(d)
        else:
            robot.move(d)

    santa.houses.update(robot.houses)
    return len(santa.houses)
