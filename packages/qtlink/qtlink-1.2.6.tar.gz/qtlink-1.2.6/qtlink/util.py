from PySide6.QtCore import QObject, Signal


def force_draw():
    """强制绘制挂起的事件，如弹窗，如果一次调用仍然存在未绘制的情况，可以多调用几次，在show前show后均调用"""
    from PySide6.QtWidgets import QApplication
    QApplication.processEvents()


def create_signal(signal_type):
    """根据传入类型，创建相应的信号类。
    :param signal_type: 任意的数据类型，如int, str, list等
    :return: qt信号类
    """

    class CustomSignal(QObject):
        signal = Signal(signal_type)

    return CustomSignal()


class ProgressSignalSlot:
    """需要某个类继承它，并连接response_signal方法到tuple类型的信号。
    然后根据需要实现各种when_xxx方法，即可根据不同状态自动调用相应的处理方法。"""

    def response_signal(self, state: tuple):
        """内置方法，直接连接外部的qt信号"""
        flag, data = state
        if flag == Progress.flag_start:
            self.when_start(data)
        elif flag == Progress.flag_doing:
            self.when_doing(data)
        elif flag == Progress.flag_success:
            self.when_success(data)
        elif flag == Progress.flag_failed:
            self.when_failed(data)
        elif flag == Progress.flag_end:
            self.when_end(data)
        elif flag == Progress.flag_info:
            self.when_info(data)
        elif flag == Progress.flag_error:
            self.when_error(data)
        elif flag == Progress.flag_other1:
            self.when_other1(data)
        elif flag == Progress.flag_other2:
            self.when_other2(data)
        elif flag == Progress.flag_other3:
            self.when_other3(data)
        else:
            raise ValueError(f'传递的信号数据错误。应该是 tuple ，但得到的是 {type(state)}')

    def when_start(self, data: list = None):
        """事件刚开始
        :param data: 当需要传输数据时，使用此参数
        """
        pass

    def when_doing(self, data: list = None):
        """事件正在进行中
        :param data: 当需要传输数据时，使用此参数
        """
        pass

    def when_success(self, data: list = None):
        """事件成功
        :param data: 当需要传输数据时，使用此参数
        """
        pass

    def when_failed(self, data: list = None):
        """事件失败
        :param data: 当需要传输数据时，使用此参数
        """
        pass

    def when_end(self, data: list = None):
        """事件结束
        :param data: 当需要传输数据时，使用此参数
        """
        pass

    def when_info(self, data: list = None):
        """事件信息
        :param data: 当需要传输数据时，使用此参数
        """
        pass

    def when_error(self, data: list = None):
        """事件错误
        :param data: 当需要传输数据时，使用此参数
        """
        pass

    def when_other1(self, data: list = None):
        """预留的任意状态
        :param data: 当需要传输数据时，使用此参数
        """
        pass

    def when_other2(self, data: list = None):
        """预留的任意状态
        :param data: 当需要传输数据时，使用此参数
        """
        pass

    def when_other3(self, data: list = None):
        """预留的任意状态
        :param data: 当需要传输数据时，使用此参数
        """
        pass


class Progress:
    """搭配ProgressSignalSlot使用，发射信号时应该使用此类来传输数据。

    Example:
        # 具体数据应使用list包裹，这利于处理复杂形态的数据。
        some_signal.emit(Progress.start(['处理开始']))

    """
    flag_start = 0
    flag_doing = 1
    flag_end = 2
    flag_success = 3
    flag_failed = 4
    flag_info = 5
    flag_error = 6
    # 预留的其他状态量
    flag_other1 = 7
    flag_other2 = 8
    flag_other3 = 9

    @staticmethod
    def start(data: list = None) -> tuple:
        return Progress.flag_start, data

    @staticmethod
    def doing(data: list = None) -> tuple:
        return Progress.flag_doing, data

    @staticmethod
    def end(data: list = None) -> tuple:
        return Progress.flag_end, data

    @staticmethod
    def success(data: list = None) -> tuple:
        return Progress.flag_success, data

    @staticmethod
    def failed(data: list = None) -> tuple:
        return Progress.flag_failed, data

    @staticmethod
    def info(data: list = None) -> tuple:
        return Progress.flag_info, data

    @staticmethod
    def error(data: list = None) -> tuple:
        return Progress.flag_error, data

    @staticmethod
    def other1(data: list = None) -> tuple:
        return Progress.flag_other1, data

    @staticmethod
    def other2(data: list = None) -> tuple:
        return Progress.flag_other2, data

    @staticmethod
    def other3(data: list = None) -> tuple:
        return Progress.flag_other3, data
