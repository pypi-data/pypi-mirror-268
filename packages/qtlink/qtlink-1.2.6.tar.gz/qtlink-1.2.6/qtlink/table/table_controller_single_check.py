# -*- coding:utf-8 -*-
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem

from qtlink.table.table_controller import TableController
from qtlink.util import create_signal


class TableControllerSingleCheck(TableController):
    """QTableView的单选控制类，它继承自基本控制类，因此它也有基本控制类的属性和方法。"""

    def __init__(self, tableview, highlight_hover_row: bool = False):
        """
        :param tableview: QTableView，需要显示表格数据的ui对象。
        :param highlight_hover_row: 是否启用鼠标悬停时高亮一整行的样式，默认不启用。
        """
        super().__init__(tableview, highlight_hover_row)
        self.model.itemChanged.connect(self.on_item_changed)
        # 当勾选某一行时，会触发该信号发送该行的字典格式数据。如果需要处理这类数据，则应连接该信号到自定义的槽函数。
        self.signal_checked_rows = create_signal(list)

    def update_table_data(self, table_data: list[dict], hide_columns: list[str] = None):
        # 断开信号连接
        self.model.itemChanged.disconnect(self.on_item_changed)

        self.before_update_table_data(table_data, hide_columns=hide_columns)
        for data in table_data:
            items = [QStandardItem(str(data.get(column, None)) if data.get(column, None) is not None else '')
                     for column in self.table_columns]
            items[0].setCheckable(True)
            self.model.appendRow(items)

        self.set_table()
        # 重新连接信号
        self.model.itemChanged.connect(self.on_item_changed)
        self.on_item_changed()

    def on_item_changed(self, item: QStandardItem = None):
        """只管理数据的发送"""
        if item is None:
            return
        if item.checkState() == Qt.Checked:
            self.model.itemChanged.disconnect(self.on_item_changed)
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0) != item:
                    self.model.item(row, 0).setCheckState(Qt.Unchecked)
            self.model.itemChanged.connect(self.on_item_changed)

        checked_rows = self.get_checked_rows()
        self.signal_checked_rows.signal.emit(checked_rows)

    def get_checked_rows(self) -> list[dict]:
        """返回被选中行的字典数据。为了与多选表格控制类保持统一格式，该方法返回的是列表格式。"""
        checked_rows = []
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)  # 勾选框在第一列
            if item.checkState() == Qt.Checked:
                checked_rows.append(self.raw_data[row])
                break
        return checked_rows
