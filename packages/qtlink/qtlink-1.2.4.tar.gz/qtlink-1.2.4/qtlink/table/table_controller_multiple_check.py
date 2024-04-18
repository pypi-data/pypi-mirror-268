# -*- coding:utf-8 -*-
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QStyleOptionButton, QStyle, QHeaderView

from qtlink.table.table_controller import TableController
from qtlink.util import create_signal


class TableControllerMultipleCheck(TableController):
    """QTableView的多选控制类，它继承自基本控制类，所以基本控制类有的参数和方法它都有。"""

    def __init__(self, tableview, highlight_hover_row: bool = False):
        """
        :param tableview: QTableView，需要显示表格数据的ui对象。
        :param highlight_hover_row: 是否启用鼠标悬停时高亮一整行的样式，默认不启用。
        """
        super().__init__(tableview, highlight_hover_row)
        self.model.itemChanged.connect(self.on_item_changed)
        # 当勾选若干行时，会触发该信号发送这些行的字典格式数据。如果需要处理这类数据，则应连接该信号到自定义的槽函数。
        self.signal_checked_rows = create_signal(list)
        self.header = CustomHeader(toggle_check_state=self.toggle_check_state, parent=self.tableview)
        self.tableview.setHorizontalHeader(self.header)
        self.always_checked_data = []

    def update_table_data(self, table_data: list[dict],
                          hide_columns: list[str] = None,
                          default_checked_table_data: list[dict] = None,
                          always_checked_table_data: list[dict] = None):
        """更新表格数据
        :param table_data: 原始表格数据，表格中的每一行数据都应使用字典格式，其中的键将按顺序自动识别为表格的列名。
        :param hide_columns: 需要隐藏/不显示的列名。
        :param default_checked_table_data: 默认被选中的数据
        :param always_checked_table_data: 始终被选中的数据
        """
        # 断开信号连接
        self.model.itemChanged.disconnect(self.on_item_changed)

        self.before_update_table_data(table_data, hide_columns=hide_columns)
        if default_checked_table_data is None:
            default_checked_table_data = []
        self.always_checked_data = always_checked_table_data if always_checked_table_data else []

        for data in table_data:
            items = [QStandardItem(str(data.get(column, None)) if data.get(column, None) is not None else '')
                     for column in self.table_columns]
            items[0].setCheckable(True)
            # 默认被选中
            if data in default_checked_table_data:
                items[0].setCheckState(Qt.Checked)
            # 始终被选中
            if data in self.always_checked_data:
                items[0].setCheckState(Qt.Checked)
                # 禁用交互
                for item in items:
                    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsSelectable)
            self.model.appendRow(items)

        self.set_table()
        # 重新连接信号
        self.model.itemChanged.connect(self.on_item_changed)
        self.on_item_changed()

    def toggle_check_state(self, is_checked):
        # 断开信号连接
        self.model.itemChanged.disconnect(self.on_item_changed)

        for row in range(self.model.rowCount()):
            item = self.model.item(row)
            # 重设勾选状态
            if self.raw_data[row] not in self.always_checked_data:
                item.setCheckState(Qt.Checked if is_checked else Qt.Unchecked)

        # 重新连接信号
        self.model.itemChanged.connect(self.on_item_changed)
        self.on_item_changed()

    def get_checked_rows(self) -> list[dict]:
        """返回被选中的若干行的字典数据。为了与单选表格控制类保持统一格式，该方法返回的是列表格式。"""
        checked_rows = []
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)  # 勾选框在第一列
            if item.checkState() == Qt.Checked:
                checked_rows.append(self.raw_data[row])
        return checked_rows

    def on_item_changed(self, item: QStandardItem = None):
        if self.hover_delegate is not None and self.hover_delegate.is_hovering:
            return

        checked_rows = self.get_checked_rows()
        self.signal_checked_rows.signal.emit(checked_rows)
        checked_rows_num = len(checked_rows)
        if checked_rows_num and checked_rows_num == len(self.raw_data):
            self.set_header_check_state(True)
        else:
            self.set_header_check_state(False)

    def set_header_check_state(self, is_checked: bool):
        self.header.update_check_state(is_checked)


class CustomHeader(QHeaderView):
    def __init__(self, toggle_check_state, orientation=Qt.Horizontal, parent=None):
        super(CustomHeader, self).__init__(orientation, parent)
        self.isChecked = False  # 初始化复选框状态为未选中
        self.toggle_check_state = toggle_check_state

    def update_check_state(self, is_checked):
        self.isChecked = is_checked
        self.updateSection(0)

    def mouseReleaseEvent(self, event):
        # 处理鼠标释放事件，用于切换表头复选框的状态
        index = self.logicalIndexAt(event.position().toPoint())
        if index == 0:
            self.update_check_state(not self.isChecked)  # 切换复选框状态
            self.toggle_check_state(self.isChecked)  # 更新模型中所有项的复选框状态
        else:
            super(CustomHeader, self).mouseReleaseEvent(event)

    def paintSection(self, painter, rect, logicalIndex):
        # 绘制表头的每一部分，用于绘制复选框
        painter.save()
        super(CustomHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()
        # 如果是第一列，绘制复选框
        if logicalIndex == 0:
            option = QStyleOptionButton()
            checkbox_width = 10  # 复选框宽度
            checkbox_height = 10  # 复选框高度
            checkbox_x = rect.x() + 3  # 复选框的水平位置
            checkbox_y = rect.y() + (rect.height() - checkbox_height) / 2  # 复选框的垂直位置
            option.rect = QRect(checkbox_x, checkbox_y, checkbox_width, checkbox_height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isChecked:
                option.state |= QStyle.State_On  # 设置复选框为选中状态
            else:
                option.state |= QStyle.State_Off  # 设置复选框为未选中状态
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)  # 绘制复选框
