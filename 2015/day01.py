#!/usr/bin/env python3


def get_floor(chars):
    floor = 0
    for char in chars:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    return floor


def get_basement_position(chars):
    floor = 0
    for n, char in enumerate(chars):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            return n + 1
