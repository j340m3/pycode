import random

from tkinter import filedialog


def open_file(filename=filedialog.askopenfilename()):
    try:
        file = open(filename, 'r')
        open_files = {}
        open_files["open"] = file
        __input = file.readlines()
        categories = __input.pop(0).split("\t")
        questions = []
        for i in __input:
            questions.append(dict(zip(categories,i.split("\t"))))
        for i in questions:
            print(i)
        act = __input.pop(random.randrange(len(__input))).split("\t")
    except FileNotFoundError:
        pass
