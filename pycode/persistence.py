from itertools import (takewhile,repeat)
import os

def obtain(filename):
    with open(filename, 'r') as file:
        categories = []
        res = []
        for i, line in enumerate(file):
            if i == 0:
                categories = line.strip().split("\t")
            else:
                res.append(dict(zip(categories, line.strip().split("\t"))))
    return res

def persist(filename,dict,mode="a",split="\t"):
    order = None
    if filename in os.listdir(os.getcwd()):
        with open(filename) as file:
            order = file.readline().strip().split(split)
    with open(filename,mode) as file:
        if order is None:
            order = list(dict.keys())
            file.write(split.join(order))
            file.write("\n")
        file.write(split.join([str(dict[i]) for i in order]))
        file.write("\n")


def count(filename):
    """Credits to Michael Bacon/Quentin Pradet from Stackoverflow

    filename -- Name of the file, of which the amount of lines shall be counted
    """
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum(buf.count(b'\n') for buf in bufgen)
