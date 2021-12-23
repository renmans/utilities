#!/usr/bin/env python3

import sys
# import hashlib


# def dedublicator(fdata):
#      hash = hashlib.md5()
#     with open(fdata, 'rb') as f:
#         for chunk in iter(lambda: f.read(4096), b''):
#             hash.update(chunk)
#     return hash.hexdigest()


def mapper(fsums):
    hashmap = {}
    with open(fsums, 'r') as f:
        for line in f:
            hash, name = line.split(' ', 1)
            hash = hash.strip()
            name = name.strip(' \n')
            if hash in hashmap.keys():
                hashmap[hash] += [name]
            else:
                hashmap[hash] = [name]
    return hashmap


def main():
    fsums = sys.argv[1]
    hashmap = mapper(fsums)
    for names in hashmap.values():
        if len(names) > 1:
            print(names)


main()
