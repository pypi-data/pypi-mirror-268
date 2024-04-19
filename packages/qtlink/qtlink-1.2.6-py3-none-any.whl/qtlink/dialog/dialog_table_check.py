from PySide6.QtWidgets import QPushButton

from qtlink import create_signal
from qtlink.dialog.dialog_table_display import DialogTableDisplay
from qtlink.table.table_controller_multiple_check import TableControllerMultipleCheck
from qtlink.table.table_controller_single_check import TableControllerSingleCheck


class DialogTableCheck(DialogTableDisplay):
    """可以显示并选择表格数据的对话框"""

    def __init__(self, text: str,
                 table_data: list[dict],
                 check_type: str = 'single',
                 parent=None,
                 title: str = '选择',
                 *args, **kwargs):
        """
        :param text: 对话框的消息文本
        :param table_data: 表格数据
        :param check_type: 表格数据的选择方式，单选：'single'，多选：'multiple'
        :param parent: 对话框所属的父类
        :param args: 表格控制器可能使用的其他参数
        :param kwargs: 表格控制器可能使用的其他参数
        """
        super().__init__(text=text, table_data=table_data, parent=parent)

        self.btn_ok = QPushButton('确定')
        self.v_layout.addWidget(self.btn_ok)

        self.setWindowTitle(title)
        self.setLayout(self.v_layout)

        if check_type == 'single':
            self.table_controller = TableControllerSingleCheck(tableview=self.tableview)
        elif check_type == 'multiple':
            self.table_controller = TableControllerMultipleCheck(tableview=self.tableview)
        else:
            raise ValueError(f"check_type的值只允许是：'single' 或 'multiple'，但得到的是：{check_type}")
        self.table_controller.update_table_data(table_data, *args, **kwargs)

        self.signal_checked_rows = create_signal(list)
        self.btn_ok.clicked.connect(self.click_btn_ok)

    def click_btn_ok(self):
        checked_data = self.table_controller.get_checked_rows()
        self.signal_checked_rows.signal.emit(checked_data)
        self.close()
