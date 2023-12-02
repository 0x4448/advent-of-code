#!/usr/bin/env python3

import re

from dataclasses import dataclass

header_pattern = re.compile(r"^Game \d+: ")
red_pattern = re.compile(r"(\d+) red")
green_pattern = re.compile(r"(\d+) green")
blue_pattern = re.compile(r"(\d+) blue")


@dataclass
class Sample:
    red: int
    green: int
    blue: int


def parse_sample(sample: str) -> Sample:
    def get_value(p, s) -> int:
        match = re.search(p, s)
        if match:
            return int(match.group(1))
        return 0

    red = get_value(red_pattern, sample)
    green = get_value(green_pattern, sample)
    blue = get_value(blue_pattern, sample)
    return Sample(red, green, blue)


with open("input.txt") as fp:
    game_id_sum = 0

    for game_id, line in enumerate(fp, 1):
        line = re.sub(header_pattern, "", line).strip()

        samples = [parse_sample(sample) for sample in line.split(";")]

        red = 0
        green = 0
        blue = 0

        for sample in samples:
            red = sample.red if sample.red > red else red
            green = sample.green if sample.green > green else green
            blue = sample.blue if sample.blue > blue else blue

        if red <= 12 and green <= 13 and blue <= 14:
            game_id_sum += game_id

    print(game_id_sum)
