from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt


class Button(QPushButton):
    def __init__(self, text="Button", id="button") -> None:
        super().__init__()
        self._id = id
        self._text = text
        self.__config__()

    def __config__(self):
        self.setObjectName(self._id)
        self.setText(self._text)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setDefaultStyleSheet()

    def click(self, target):
        self.clicked.connect(target)

    def setStyleSheetFile(self, file):
        with open(file, "r") as f:
            css = f.read()
            self.setStyleSheet(css)

    def setDefaultStyleSheet(self):
        style = """
                #button {
                        text-align: center;
                        color: #252525;
                        border: none;
                        padding: 5px;
                        border-radius: 3px;
                        background-color: #358dff;
                }

                #button:hover {
                        background-color: #2b7ae0;
                }

                #button:pressed {
                        background-color: #4a8add;
                }
                """
        self.setStyleSheet(style)
