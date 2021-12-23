#!/usr/bin/env python3
from hashlib import md5
from getpass import getpass
from base64 import b64encode


def get_params() -> tuple:
    print("\033[1;31mTemplate: www.<website>.<domain>\033[0m")
    print(
        "\033[1;31m[IMPORTANT!]\033[0m Use the website address template. The "
        "generated passwords will be different for google.com and www.google."
        "com!"
    )

    site = input("Enter site address: ")
    login = input("Enter login [optional]: ") or ""
    passwd = getpass("Enter master password: ")

    return (site, login, passwd)


def generator(params: tuple) -> str:
    seed = b"".join([b.encode() for b in params])
    seed = md5(seed)
    hash = seed.hexdigest().encode()
    related_passwd = b64encode(hash)[:32].decode()
    return related_passwd


def main():
    p = get_params()
    passwd = generator(p)
    print(f"\033[32m{passwd}\033[0m")


if __name__ == '__main__':
    main()
