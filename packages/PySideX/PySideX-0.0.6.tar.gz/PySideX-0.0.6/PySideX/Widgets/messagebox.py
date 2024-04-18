from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon
from PySideX.Assets import Assets


class MessageBox(QMessageBox):
    def __init__(
        self,
        text:str,
        title="Notification", 
        icon=Assets.ico.pysidex,
        type=QMessageBox.Icon.Information,
    ):
        self._title = title
        self._text = text
        self._icon = icon
        self._type = type
        self.message = QMessageBox()

        super().__init__()
        self.message.setWindowTitle(self._title)
        self.message.setText(self._text)
        self.message.setIcon(self._type)
        self.message.setWindowIcon(QIcon(self._icon))

    def setNoIcon(self):
        self.message.setIcon(QMessageBox.Icon.NoIcon)
        result = self.message.exec()
        if result == QMessageBox.Ok:
            return True
        else:
            return False

    def setInformation(self):
        self.message.setIcon(QMessageBox.Icon.Information)
        result = self.message.exec()
        if result == QMessageBox.Ok:
            return True
        else:
            return False

    def setWarning(self):
        self.message.setIcon(QMessageBox.Icon.Warning)
        result = self.message.exec()
        if result == QMessageBox.Ok:
            return True
        else:
            return False

    def setCritical(self):
        self.message.setIcon(QMessageBox.Icon.Critical)
        result = self.message.exec()
        if result == QMessageBox.Ok:
            return True
        else:
            return False

    def setNoIcon(self):
        self.message.setIcon(QMessageBox.Icon.NoIcon)
        result = self.message.exec()
        if result == QMessageBox.Ok:
            return True
        else:
            return False

    def setQuestion(self):
        self.message.setIcon(QMessageBox.Icon.Question)
        result = self.message.exec()
        if result == QMessageBox.Ok:
            return True
        else:
            return False

    def setOkCancel(self):
        self.message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        result = self.message.exec()

        if result == QMessageBox.Ok:
            return True
        else:
            return False

    def setRetryCancel(self):
        self.message.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)

        result = self.message.exec()

        if result == QMessageBox.Retry:
            return True
        else:
            return False
