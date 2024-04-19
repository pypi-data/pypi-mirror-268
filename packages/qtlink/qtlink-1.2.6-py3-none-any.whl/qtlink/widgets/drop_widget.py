# -*- coding:utf-8 -*-
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFileDialog

from qtlink.util import create_signal


class DropWidget(QWidget):
    def __init__(self, label_text: str, parent=None, default_path: str = ""):
        super().__init__(parent)
        self.default_path = default_path
        self.signal_select_path = create_signal(str)
        self.setCursor(QCursor(Qt.PointingHandCursor))  # 设置鼠标样式为指向手势
        self.setAcceptDrops(True)

        self.setMinimumHeight(130)  # 设置最小高度
        self.setMaximumHeight(130)  # 设置最大高度

        self.label = QLabel(label_text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("border: 2px dashed #aaa;")
        self.setStyleSheet("QWidget { background-color: rgb(240, 240, 240); }")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # 设置布局边距为0
        layout.setSpacing(0)  # 设置布局内部组件间的间距为0
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_default_path(self, path: str):
        self.default_path = path

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dropEvent(self, event):
        mimeData = event.mimeData()
        if mimeData.hasUrls():
            url = mimeData.urls()[0]
            path = url.toLocalFile()
            self.signal_select_path.signal.emit(path)
            event.acceptProposedAction()
        else:
            super().dropEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 打开文件管理器选择文件夹
            path = QFileDialog.getExistingDirectory(self, "选择文件夹", self.default_path)
            if path:
                self.signal_select_path.signal.emit(path)
