from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from PySideX.Assets import Assets
from PySideX.Widgets.frame import Frame


class Window(QMainWindow):
    def __init__(
        self,
        title="PySideX",
        min_width=240,
        min_height=90,
        width=1280,
        height=720,
        icon=Assets.ico.pysidex,
    ):
        self._title = title
        self._min_width = min_width
        self._min_height = min_height
        self._width = width
        self._height = height
        self._icon = icon
        self._centralWidget = Frame()
        self.__config__()

    def __config__(self):
        super(Window, self).__init__()
        self.setWindowTitle(self._title)
        self.resize(self._width, self._height)
        self.setMinimumSize(self._min_width, self._min_height)
        self.setWindowIcon(QIcon(self._icon))
        self.setCentralWidget(self._centralWidget)
