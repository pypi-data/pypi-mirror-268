# -*- coding:utf-8 -*-
from PySide6.QtWidgets import QWidget, QListWidget, QVBoxLayout, QListWidgetItem, \
    QAbstractItemView

scrollbar_style = """
QScrollBar:vertical {
    border: none;
    background: #F1F1F1;
    width: 12px;
    margin: 0px 0px 0px 0px;
}

QScrollBar::handle:vertical {
    background: #CCCCCC;
    min-height: 20px;
}

QScrollBar:horizontal {
    border: none;
    background: #F1F1F1;
    height: 12px;
    margin: 0px 0px 0px 0px;
}

QScrollBar::handle:horizontal {
    background: #CCCCCC;
    min-width: 20px;
}
"""

list_widget_style = """
QListWidget::item:hover {
    background-color: rgb(240, 240, 240);
    border: none;
    outline: none;
}

QListWidget::item:selected {
    background-color: rgb(220, 220, 220);
    border: none;
    outline: none;
}

QListWidget:focus {
    outline: none;
}

"""


class ListWidget(QWidget):
    """只是容器"""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        # 创建QListWidget
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        layout.setContentsMargins(0, 0, 0, 0)  # 设置布局边距为0
        layout.setSpacing(0)  # 设置布局内部组件间的间距为0
        self.setLayout(layout)
        self.setStyleSheet("QWidget { border: none; }")
        # 应用滚动条样式
        self.listWidget.verticalScrollBar().setStyleSheet(scrollbar_style)
        self.listWidget.horizontalScrollBar().setStyleSheet(scrollbar_style)
        self.listWidget.setStyleSheet(list_widget_style)
        # 设置像素级的垂直滚动
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)  # noqa

    def add_widgets(self, widgets: list):
        self.listWidget.clear()
        for widget in widgets:
            item = QListWidgetItem(self.listWidget)
            item.setSizeHint(widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)
