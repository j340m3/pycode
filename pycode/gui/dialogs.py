from sys import version_info
if version_info[0] == 2:
    # We are using Python 2.x
    import Tkinter as tk
    import tkSimpleDialog as sdg
elif version_info[0] == 3:
    # We are using Python 3.x
    import tkinter as tk
    from tkinter import simpledialog as sdg


def NameDialog():
    return sdg.askstring("Name dialog","Please insert Name:")
