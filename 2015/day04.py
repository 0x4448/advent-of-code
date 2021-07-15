#!/usr/bin/env python3

import hashlib


def md5(s: str) -> str:
    h = hashlib.md5()
    h.update(s.encode("utf-8"))
    return h.hexdigest()


def mine_coin(key: str) -> int:
    count = 1
    while not md5(key + str(count)).startswith("000000"):
        count += 1
    return count
