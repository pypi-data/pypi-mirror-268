from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap


class Image(QLabel):
    def __init__(self,img:str,id="image") -> None:
        super().__init__()
        self._img = img
        self._id = id
        self.__config__()

    def __config__(self):
        self.setObjectName(self._id)
        self.setText('')
        pixmap = QPixmap(self._img)
        self.setPixmap(pixmap)
        self.setScaledContents(True)

    def click(self, target):
        """Every function expects to receive an event"""
        self.mousePressEvent = target

    def setStyleSheetFile(self, file):
        with open(file, "r") as f:
            css = f.read()
            self.setStyleSheet(css)

