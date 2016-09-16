from pycode.gui.core import Mainframe
from pycode.gui.widgets import TrueFalseWidget

if __name__ == '__main__':
    widgets = [TrueFalseWidget("Has the question been answered?"),
               TrueFalseWidget("Is the answer correct?"), ]
    w = Mainframe(widgets)
