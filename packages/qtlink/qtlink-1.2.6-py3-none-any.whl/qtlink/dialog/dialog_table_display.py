from PySide6.QtWidgets import QDialog, QTableView, QLabel, QVBoxLayout, QAbstractItemView

from qtlink.table.table_controller import TableController


def show_dialog_table_display(text: str,
                              table_data: list[dict],
                              show_or_exec: str = 'exec',
                              parent=None, *args, **kwargs):
    """以函数形式直接启动对话框
    :param text: 对话框的消息文本
    :param table_data: 表格数据
    :param show_or_exec: 对话框的运行方式，'exec' or 'show'
    :param parent: 对话框所属的父类
    :param args: 表格控制器可能使用的其他参数
    :param kwargs: 表格控制器可能使用的其他参数
    """
    dialog = DialogTableDisplay(text, table_data=table_data, parent=parent, *args, **kwargs)
    if show_or_exec == 'exec':
        dialog.exec()
    else:
        dialog.show()


class DialogTableDisplay(QDialog):
    """可以显示表格数据的对话框"""

    def __init__(self, text: str,
                 table_data: list[dict],
                 parent=None,
                 title: str = '提示',
                 *args, **kwargs):
        """
        :param text: 对话框的文本消息
        :param table_data: 表格数据
        :param parent: 对话框所属的父类
        :param args: 表格控制器可能使用的其他参数
        :param kwargs: 表格控制器可能使用的其他参数
        """
        super().__init__(parent=parent)
        self.v_layout = QVBoxLayout()
        label = QLabel(text, self)
        label.setWordWrap(True)
        self.tableview = QTableView(self)
        self.tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.v_layout.addWidget(label)
        self.v_layout.addWidget(self.tableview)

        self.setWindowTitle(title)
        self.setLayout(self.v_layout)
        self.table_controller = TableController(tableview=self.tableview)
        self.table_controller.update_table_data(table_data=table_data, *args, **kwargs)
