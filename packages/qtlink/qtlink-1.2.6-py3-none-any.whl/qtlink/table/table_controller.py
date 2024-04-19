# -*- coding:utf-8 -*-
from collections import OrderedDict

from PySide6.QtCore import QItemSelectionModel, Qt, QObject, QModelIndex, QEvent
from PySide6.QtGui import QStandardItem, QColor, QStandardItemModel

from qtlink.util import create_signal


class TableController:
    """QTableView的基础控制类，负责存储/显示/交互表格数据。"""

    def __init__(self, tableview, highlight_hover_row: bool = False):
        """
        :param tableview: QTableView，需要显示表格数据的ui对象。
        :param highlight_hover_row: 是否启用鼠标悬停时高亮一整行的样式，默认不启用。
        """
        self.tableview = tableview
        self.table_columns = []
        self.raw_data = None
        self.column_widths = None
        self.first_load = True
        self.model = QStandardItemModel()
        # 点击某行时，会用qt信号发送该行的字典格式数据。如果需要处理这类数据，则应连接该信号到自定义的槽函数。
        self.signal_click_row = create_signal(dict)
        # 连接信号
        self.tableview.clicked.connect(self.on_table_clicked)
        # 禁止上下文菜单
        scrollBar = self.tableview.verticalScrollBar()
        scrollBar.setContextMenuPolicy(Qt.NoContextMenu)
        scrollBar = self.tableview.horizontalScrollBar()
        scrollBar.setContextMenuPolicy(Qt.NoContextMenu)
        # 启用高亮一整行效果
        if highlight_hover_row:
            self.tableview.setMouseTracking(True)
            self.hover_delegate = HoverDelegate(tableview=tableview)
            self.tableview.entered.connect(self.hover_delegate.on_entered)
        else:
            self.hover_delegate = None

    def update_table_data(self, table_data: list[dict], hide_columns: list[str] = None):
        """更新表格数据
        :param table_data: 原始表格数据，表格中的每一行数据都应使用字典格式，其中的键将按顺序自动识别为表格的列名。
        :param hide_columns: 需要隐藏/不显示的列名。
        """
        self.before_update_table_data(table_data, hide_columns=hide_columns)

        for data in table_data:
            items = [QStandardItem(str(data.get(column, None)) if data.get(column, None) is not None else '')
                     for column in self.table_columns]
            self.model.appendRow(items)

        self.set_table()

    def before_update_table_data(self, table_data, hide_columns: list[str] = None):
        if not self.first_load:
            # 保存当前列宽
            self.save_current_column_widths()
        self.first_load = False
        self.raw_data = table_data
        # 传入空列表将同步清空表头，传入只有键无值的结构才保持显示表头，而无表格数据。
        self.table_columns = self.get_table_columns_from_data(table_data, hide_columns=hide_columns)
        self.model.clear()

    def set_table(self):
        self.model.setHorizontalHeaderLabels(self.table_columns)
        self.tableview.setModel(self.model)

        if self.column_widths is not None:
            for item in self.column_widths:
                index, width = item
                self.tableview.setColumnWidth(index, width)

    def get_table_columns_from_data(self, data: list[dict], hide_columns: list[str] = None):
        ordered_keys = OrderedDict()
        for d in data:
            for key in d.keys():
                if hide_columns and key in hide_columns:
                    continue
                ordered_keys[key] = None
        # 将OrderedDict的键转换为列表
        return list(ordered_keys.keys())

    def clear_table_data(self):
        """清空表格数据"""
        self.update_table_data(table_data=[])

    def save_current_column_widths(self):
        if self.column_widths is None:
            return
        for index in range(self.model.columnCount()):
            width = self.tableview.columnWidth(index)
            # 确保保存的列宽信息与列的数量相匹配
            if index < len(self.column_widths):
                self.column_widths[index] = (index, width)
            else:
                self.column_widths.append((index, width))

    def on_table_clicked(self, index):
        # index是QModelIndex类型，可以用来检索数据
        row = index.row()  # 获取行号
        # 获取该行的所有列的数据
        rowData = self.raw_data[row]
        self.signal_click_row.signal.emit(rowData)

    def set_column_width(self, column_widths: list[tuple] = None):
        """通过多个(index, width)元组指定特定列的宽度。
        注意：应该在调用update_table_data之前完成设置。
        :param column_widths: 任意个(index, width)组成的list
        """
        self.column_widths = column_widths

    def set_select_row(self, index: int):
        if len(self.raw_data) - 1 >= index:
            first_index = self.model.index(index, 0)
            self.tableview.selectionModel().select(first_index,
                                                   QItemSelectionModel.Select | QItemSelectionModel.Rows)

    def set_not_select_row(self, index: int):
        if len(self.raw_data) - 1 >= index:
            first_index = self.model.index(index, 0)
            self.tableview.selectionModel().select(first_index,
                                                   QItemSelectionModel.Deselect | QItemSelectionModel.Rows)

    def __del__(self):
        if self.hover_delegate and self.tableview.viewport():
            self.tableview.viewport().removeEventFilter(self.hover_delegate)


class HoverDelegate(QObject):
    def __init__(self, tableview):
        super().__init__(tableview)
        self.tableview = tableview
        self.row_under_mouse = -1
        self.hover_color = QColor(240, 240, 240)
        # 安装事件过滤器到表格视图的视口上
        self.tableview.viewport().installEventFilter(self)
        self.is_hovering = False

    def on_entered(self, index):
        self.is_hovering = True
        hover_row = index.row()
        # 检查当前行是否被选中
        is_row_selected = self.tableview.selectionModel().isRowSelected(hover_row, QModelIndex())
        if hover_row != self.row_under_mouse:
            # 还原上一行的背景色
            if self.row_under_mouse >= 0:
                self.set_row_background(self.row_under_mouse, self.tableview.palette().base())
            # 重设当前行背景色
            if not is_row_selected:
                self.set_row_background(hover_row, self.hover_color)
                self.row_under_mouse = hover_row
        self.is_hovering = False

    def set_row_background(self, hover_row, color):
        for column in range(self.tableview.model().columnCount()):
            index = self.tableview.model().index(hover_row, column)
            rect = self.tableview.visualRect(index)
            self.tableview.viewport().update(rect)
            self.tableview.model().setData(index, color, Qt.BackgroundRole)

    def clear_hover_style(self):
        if self.row_under_mouse >= 0:
            self.set_row_background(self.row_under_mouse, self.tableview.palette().base())
            self.row_under_mouse = -1
            self.tableview.viewport().update()  # 更新视图以反映背景色的变化

    def eventFilter(self, watched, event):
        if watched and watched == self.tableview.viewport() and event.type() == QEvent.Leave:
            self.clear_hover_style()
        return super().eventFilter(watched, event)
