import os

def inc(x):
    return x + 1


def test_answer():
    os.mkdir(".")
    assert inc(3) == 4
