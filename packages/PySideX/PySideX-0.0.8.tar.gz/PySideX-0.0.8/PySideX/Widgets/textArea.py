from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import Qt


class TextArea(QTextEdit):
    def __init__(self, id="textArea", placeholder=None) -> None:
        super().__init__()
        self._id = id
        self._placeholder = placeholder
        self.__config__()

    def __config__(self):
        self.setObjectName(self._id)
        self.setDefaultStyleSheet()
        if self._placeholder:
            self.setPlaceholderText(self._placeholder)

    def typingEvent(self, target):
        self.textChanged.connect(target)

    def setStyleSheetFile(self, file):
        with open(file, "r") as f:
            css = f.read()
            self.setStyleSheet(css)

    def setDefaultStyleSheet(self):
        style = """
                #textArea {
                        border: 1px solid #c1c1c1;
                        min-height: 26px;
                        max-height: 2160px;
                        padding: 3x;
                        padding-left: 5px;
                        border-radius: 3px;
                        background-color: transparent;
                }

                #textArea:focus {
                        border: 3px solid #8dbeff;
                }
                """
        self.setStyleSheet(style)
