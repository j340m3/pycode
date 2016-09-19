from pycode.gui.core import MainFrame
from pycode.gui.widgets import TrueFalseWidget
from pycode.gui.dialogs import NameDialog
from pycode.persistence import open_file


if __name__ == "__main__":
    open_file()
    widgets = [TrueFalseWidget("Has the question been answered?"),
           TrueFalseWidget("Is the answer correct?"), ]
    w = MainFrame(widgets)
    while w.user is None:
        w.user = NameDialog()
    w.start()
