#!/usr/bin/env python3

sum = 0

with open("input.txt") as fp:
    for line in fp:
        value = ""

        for char in line:
            if char.isdigit():
                value += char

        value = value[0] + value[-1]
        sum += int(value)

print(sum)
