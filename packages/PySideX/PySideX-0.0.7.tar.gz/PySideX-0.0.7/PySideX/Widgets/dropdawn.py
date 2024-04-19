from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Qt


class Dropdown(QComboBox):
    def __init__(self, id="dropdown") -> None:
        super().__init__()
        self._id = id
        self.__config__()

    def __config__(self):
        self.setObjectName(self._id)
        self.setDefaultStyleSheet()

    def selectionEvent(self, target):
        self.currentTextChanged.connect(target)

    def setStyleSheetFile(self, file):
        with open(file, "r") as f:
            css = f.read()
            self.setStyleSheet(css)

    def setDefaultStyleSheet(self):
        style = """
                #dropdown {
                        text-align: center;
                        border: 1px solid #c1c1c1;
                        min-height: 26px;
                        padding: 3x;
                        padding-left: 5px;
                        border-radius: 3px;
                        background-color: transparent;
                }

                #dropdown:focus {
                        border: 3px solid #8dbeff;
                }
                """
        self.setStyleSheet(style)
