from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class Label(QLabel):
    def __init__(
        self, text="Label", id="label", fontSize=16, color="black", text_align="center"
    ) -> None:
        super().__init__()
        self._id = id
        self._text = text
        self._fontSize = fontSize
        self._color = color
        self._text_align = text_align
        self.__config__()

    def __config__(self):
        self.setObjectName(self._id)
        self.setText(self._text)

        if self._text_align.lower() == "center":
            self._text_align = "AlignCenter"
        elif self._text_align.lower() == "right":
            self._text_align = "AlignRight"
        else:
            self._text_align = "AlignLeft"
        self.setDefaultStyleSheet()

    def click(self, target):
        """Every function expects to receive an event"""
        self.mousePressEvent = target

    def setStyleSheetFile(self, file):
        with open(file, "r") as f:
            css = f.read()
            self.setStyleSheet(css)

    def setDefaultStyleSheet(self):
        style = f"""
                #label {{    
                        font-size: {self._fontSize}px;
                        color: {self._color};
                        qproperty-alignment: {self._text_align};
                        border: none;
                        padding: 0px;
                        background-color: transparent;
                }}
                """
        self.setStyleSheet(style)
