from PySide6.QtWidgets import QHBoxLayout


class HBoxLayout(QHBoxLayout):
    def __init__(self, parent=None, margins=[0, 0, 0, 0], spacing=10):
        super().__init__(parent)
        self.setContentsMargins(margins[0], margins[1], margins[2], margins[3])
        self.setSpacing(spacing)
