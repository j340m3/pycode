from sys import version_info
if version_info[0] == 2:
    # We are using Python 2.x
    import Tkinter as tk
    import tkFileDialog as filedialog
elif version_info[0] == 3:
    # We are using Python 3.x
    import tkinter as tk
    from tkinter import filedialog
from pycode import persistence
from pycode.gui.dialogs import NameDialog

class MainFrame: #pragma no cover
    def __init__(self, widgets):
        self.widgets = widgets
        self.tk = tk.Tk()
        self.tk.title("pycode")
        self.q = self.a = None
        self.__is_fullscreen = False
        self.frame = tk.Frame(self.tk)
        self.frame.grid(row=0, column=0)
        self.init_keybindings()
        self.init_menubar()
        self.init_content()
        self.open_files = {"save": None, "open": None}
        self.__input = None
        self.showResults("<No file loaded!>", "<Please open a file!>")
        self.act = None
        self.prev = []
        self.user = None

    def init(self):
        #Show NameDialog
        #validate output
        #draw gui
        pass

    def init_menubar(self):
        menubar = tk.Menu(self.tk)
        self.tk.config(menu=menubar)

        fileMenu = tk.Menu(menubar)

        fileMenu.add_command(label="Open", command=persistence.open_file)
        fileMenu.add_command(label="Save", command=self.save_file)

        fileMenu.add_separator()

        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)

    def showResults(self, q, a):
        self.q = tk.Label(self.tk, text=q)
        self.q.grid(column=2, row=1, sticky=tk.NSEW, columnspan=1)
        self.a = tk.Label(self.tk, text=a)
        self.a.grid(column=2, row=2, sticky=tk.NSEW, columnspan=1)

    def init_content(self):
        for i, j in enumerate(self.widgets):
            j.draw(self.tk, i + 3)
        self.tk.grid_rowconfigure(0, weight=1)
        self.tk.grid_rowconfigure(len(self.widgets) + 3, weight=1)
        self.tk.grid_columnconfigure(0, weight=1)
        self.tk.grid_columnconfigure(len(self.widgets) + 3, weight=1)

    def init_keybindings(self):
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.__is_fullscreen = not self.__is_fullscreen  # Just toggling the boolean
        self.tk.attributes('-fullscreen', self.__is_fullscreen)
        self.tk.overrideredirect(self.__is_fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.__is_fullscreen = False
        self.tk.attributes("-fullscreen", False)
        self.tk.overrideredirect(False)
        return "break"

    def save_file(self):
        filename = tk.filedialog.asksaveasfilename()
        try:
            file = open(filename, 'w')
            self.open_files["save"].append(file)
        except FileNotFoundError:
            pass

    def onExit(self):
        for category in self.open_files:
            self.open_files[category].close()
        self.tk.quit()

    def start(self):
        self.tk.mainloop()
