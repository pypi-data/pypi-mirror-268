from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


def show_dialog_info(text: str, enable_btn_confirm: bool = False, show_or_exec: str = 'exec'):
    """以函数形式直接启动对话框
    :param text: 对话框的消息文本
    :param enable_btn_confirm: 是否启用确定按钮，默认不启用
    :param show_or_exec: 对话框的运行方式，'exec' or 'show'
    """
    dialog = DialogInfo(text, enable_btn_confirm)
    if show_or_exec == 'exec':
        dialog.exec()
    else:
        dialog.show()


class DialogInfo(QDialog):
    """仅显示文本消息的对话框类"""

    def __init__(self, text: str, enable_btn_confirm: bool = False, parent=None):
        """
        :param text: 对话框的文本消息
        :param enable_btn_confirm: 是否启用确定按钮（只有关闭对话框的作用），默认不启用
        :param parent: 对话框所属的父类
        """
        super().__init__(parent=parent)
        vLayout = QVBoxLayout()

        label = QLabel(text, self)
        label.setWordWrap(True)
        vLayout.addWidget(label)

        if enable_btn_confirm:
            btn_confirm = QPushButton('确定', self)
            btn_confirm.clicked.connect(self.close)
            vLayout.addWidget(btn_confirm)

        self.setLayout(vLayout)
