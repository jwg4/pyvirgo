from .parse import parse


def load(filename):
    with open(filename, "r") as f:
        return loads(f.read())


def loads(data):
    return parse(data)
