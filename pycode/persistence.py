import random
from itertools import (takewhile,repeat)
from tkinter import filedialog


def open_file(filename):
    try:
        lines = count(filename)
        file = open(filename, 'r')
        open_files = {}
        open_files["open"] = file
        __input = file.readlines()
        categories = __input.pop(0).split("\t")
        questions = []
        for i in __input:
            print("Processing line",i,"of",lines)
            questions.append(dict(zip(categories,i.split("\t"))))
        for i in questions:
            print(i)
        act = __input.pop(random.randrange(len(__input))).split("\t")
    except FileNotFoundError:
        pass


def count(filename):
    """Credits to Michael Bacon/Quentin Pradet from Stackoverflow

    filename -- Name of the file, of which the amount of lines shall be counted
    """
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum(buf.count(b'\n') for buf in bufgen)
