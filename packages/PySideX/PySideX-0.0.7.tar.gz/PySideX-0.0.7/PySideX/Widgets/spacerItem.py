from PySide6.QtWidgets import QSpacerItem, QSizePolicy


class SpacerItem(QSpacerItem):
    def __init__(self, width: bool = False, height: bool = False):
        self._width = width
        self._height = height

        if self._width != True:
            self._width = QSizePolicy.Policy.Minimum
        else:
            self._width = QSizePolicy.Policy.Expanding
        if self._height != True:
            self._height = QSizePolicy.Policy.Minimum
        else:
            self._height = QSizePolicy.Policy.Expanding

        super().__init__(0, 0, self._width, self._height)
