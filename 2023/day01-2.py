#!/usr/bin/env python3

sum = 0

spelled_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("input.txt") as fp:
    for n, line in enumerate(fp):
        for k, v in spelled_numbers.items():

            while line.find(k) >= 0:
                # insert digit at index 1 of match
                # prevents edge cases if words share the same first/last letter
                line = line[0 : line.find(k) + 1] + str(v) + line[line.find(k) + 1 :]

        value = ""
        for char in line:
            if char.isdigit():
                value += char

        value = value[0] + value[-1]
        sum += int(value)

print(sum)
