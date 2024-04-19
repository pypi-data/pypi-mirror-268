from PySide6.QtWidgets import QFrame


class Frame(QFrame):
    def __init__(self, id="frame",background_color='#fff') -> None:
        super().__init__()
        self._id = id
        self._background_color = background_color
        self.__config__()

    def __config__(self):
        self.setObjectName(self._id)
        self.setDefaultStyleSheet()

    def setStyleSheetFile(self, file):
        with open(file, "r") as f:
            css = f.read()
            self.setStyleSheet(css)

    def click(self, target):
        """Every function expects to receive an event"""
        self.mousePressEvent = target

    def setDefaultStyleSheet(self):
        style = f"""
                #frame {{
                        background-color: {self._background_color};
                }}
                """
        self.setStyleSheet(style)
