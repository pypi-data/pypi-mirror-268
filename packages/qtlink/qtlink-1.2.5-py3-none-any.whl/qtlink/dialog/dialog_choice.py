from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout


def show_dialog_choice(text: str,
                       click_btn_confirm,
                       title: str = '提示',
                       show_or_exec: str = 'exec',
                       parent=None):
    """以函数形式直接启动对话框
    :param text: 对话框的消息文本
    :param click_btn_confirm: 点击确定按钮后自动调用的函数
    :param title: 对话框顶部标题
    :param show_or_exec: 对话框的运行方式，'exec' or 'show'
    :param parent: 对话框所属的ui父类
    """
    dialog = DialogChoice(text=text, click_btn_confirm=click_btn_confirm,
                          title=title, parent=parent)
    if show_or_exec == 'exec':
        dialog.exec()
    else:
        dialog.show()


class DialogChoice(QDialog):
    """带有确定/取消按钮的对话框类"""

    def __init__(self, text: str, click_btn_confirm, title: str = '提示', parent=None):
        """
        :param text: 对话框的文本消息
        :param click_btn_confirm: 点击确定按钮后自动调用的函数
        :param parent: 对话框所属的父类
        """
        super().__init__(parent=parent)
        vLayout = QVBoxLayout()
        self.click_btn_confirm = click_btn_confirm
        label = QLabel(text, self)
        label.setWordWrap(True)
        vLayout.addWidget(label)

        hLayout = QHBoxLayout()
        btn_confirm = QPushButton('确定', self)
        btn_confirm.clicked.connect(self.on_clicked_btn_confirm)
        hLayout.addWidget(btn_confirm)

        btn_cancel = QPushButton('取消', self)
        btn_cancel.clicked.connect(self.close)
        hLayout.addWidget(btn_cancel)
        vLayout.addLayout(hLayout)

        self.setWindowTitle(title)
        self.setLayout(vLayout)

    def on_clicked_btn_confirm(self):
        self.click_btn_confirm()
        self.close()
