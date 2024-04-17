import os

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures")


def openImg(filename: str):
    with open(filename, "rb") as f:
        d = f.read()
    return d
