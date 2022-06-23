#!/usr/bin/env python3
import sys
import random


def choice(argv: list):
    return random.choice(argv[1:])


if __name__ == '__main__':
    res = choice(sys.argv)
    print(res)
