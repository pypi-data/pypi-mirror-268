from PySideX.Widgets.frame import Frame
from PySideX.Widgets.verticalBoxLayout import VBoxLayout
from PySideX.Widgets.horizontalBoxLayout import HBoxLayout
from PySideX.Widgets.spacerItem import SpacerItem


class BoxWidget(Frame):
    def __init__(
        self,
        widgets:list,
        background_color="#fff",
        orientation="v",
        id='frame'
    ) -> None:
        super().__init__(background_color=background_color)
        self._widgets = widgets
        self._background_color = background_color
        self._id = id
        self._orientation = orientation
        self.setConfig()

    def setConfig(self):
        self.setObjectName(self._id)
        self._setListWidget()
       
        if self._orientation == "v":
            self._layout = VBoxLayout(self)
        else:
            self._layout = HBoxLayout(self)

        for widget in self._widgets:
            self._list_widget.append(widget)

        for widget in self.widgets():
            if (type(widget) == SpacerItem):
                self._layout.addItem(widget)
            else:
                self._layout.addWidget(widget)

    def _setListWidget(self):
        self._list_widget = []
    
    def widgets(self):
        return self._list_widget
