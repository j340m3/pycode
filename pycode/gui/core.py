import os
from sys import version_info
if version_info[0] == 2:
    # We are using Python 2.x
    import Tkinter as tk
    import tkFileDialog as filedialog
    from Tkinter import ttk
elif version_info[0] == 3:
    # We are using Python 3.x
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog
from pycode import persistence
from pycode.gui.widgets import ScaleWidget

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

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.statusbar = StatusBar(self)
        self.toolbar = ToolBar(parent)
        self.navbar = NavBar(self)
        self.main = Main(self)
        self.callbacks = {}

        self.statusbar.pack(side="bottom", fill="x")
        #self.toolbar.pack(side="top", fill="x")
        #self.navbar.pack(side="left", fill="y")
        self.main.pack(side="top", fill="both", expand=True)

    def add_callback(self,name,function):
        callbacks = self.get_callbacks(name)
        callbacks.append(function)
        self.callbacks[name] = callbacks

    def get_callbacks(self, name):
        return self.callbacks.get(name,[])

    def handle_callback(self,name):
        for i in self.get_callbacks(name):
            i()

class StatusBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.variable=tk.StringVar()
        self.label=tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W,
                           textvariable=self.variable,
                           font=('arial',10,'normal'))
        self.variable.set('Status Bar')
        self.label.pack(fill=tk.X)

class NavBar(tk.Frame):
    def __init__(self, master, path="."):

        tk.Frame.__init__(self, master)
        self.tree = ttk.Treeview(self)
        ysb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text=path, anchor='w')

        abspath = os.path.abspath(path)
        root_node = self.tree.insert('', 'end', text=abspath, open=True)
        self.process_directory(root_node, abspath)
        #
        # self.tree.grid(row=0, column=0)
        # ysb.grid(row=0, column=1, sticky='ns')
        # xsb.grid(row=1, column=0, sticky='ew')
        # self.grid()

        ysb.pack(side=tk.RIGHT,fill=tk.BOTH)
        xsb.pack(fill=tk.BOTH,side=tk.BOTTOM)
        self.tree.pack(fill=tk.Y,expand=1)

    def process_directory(self, parent, path):

        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = self.tree.insert(parent, 'end', text=p, open=False)
            if isdir:
                self.process_directory(oid, abspath)

class ToolBar(tk.Menu):
    def __init__(self,master):
        tk.Menu.__init__(self,master)
        master.config(menu=self)

        fileMenu = tk.Menu(self)

        fileMenu.add_command(label="Open", command=lambda: master.handle_callback("open"))
        fileMenu.add_command(label="Save", command=lambda: master.handle_callback("save"))

        fileMenu.add_separator()

        fileMenu.add_command(label="Exit", underline=0, command=lambda: master.handle_callback("exit"))
        self.add_cascade(label="File", underline=0, menu=fileMenu)

class Main(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        x = [
            {"min":0, "max":1,"label":"Do you like me?"},
            {"min":1, "max":10,"label":"How hot am I?"}
        ]
        self.widgets =[]
        for i in x:
            self.widgets.append(ScaleWidget(master,i["label"],i["min"],i["max"],))
        for i in self.widgets:
            i.pack(side=tk.TOP)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.geometry("640x480")
    root.mainloop()
