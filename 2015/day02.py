#!/usr/bin/env python3


def get_area(dimensions: str) -> int:
    dimensions = dimensions.split("\n")
    total = 0

    for dim in dimensions:
        l, w, h = sorted([int(n) for n in dim.split("x")])
        # area of smallest side
        total += l * w
        total += 2 * l * w
        total += 2 * w * h
        total += 2 * l * h

    return total


def get_length(dimensions: str) -> int:
    dimensions = dimensions.split("\n")
    total = 0

    for dim in dimensions:
        l, w, h = sorted([int(n) for n in dim.split("x")])

        # perimeter of smallest face
        total += 2 * l + 2 * w

        # volume
        total += l * w * h

    return total
