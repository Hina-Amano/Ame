from Airtest.airtest.core.cv import Template
from ._log_mod import logger
from pynput.mouse import Controller
from DrissionPage.common import Actions
import time
from ame_6._until import loop_find, imread
import logging

def close_airtest_log():
    """
    关闭多余的日志

    """

    logger = logging.getLogger("airtest")
    logger.setLevel(logging.ERROR)


class Auto:
    def __init__(self,tab):
        self.tab=tab
        # 初始化鼠标控制器
        self.mouse = Controller()
        # 初始化动作链
        # 这些操作皆为模拟，真正的鼠标不会移动，因此可以多个标签页同时操作
        self.action=Actions(self.tab)


    def _screenshot(self):
        """
        该方法用于截取当前页面的屏幕截图并将其保存到指定路径

        """
        file_path = "temp.jpg"
        self.tab.get_screenshot(file_path)
        screen = imread(file_path)
        return screen

    def touch(self, template:Template):
        """

        # cn
        通过图像识别对当前页面执行触摸操作

        Args:
              v: 要触摸的目标，可以是模板实例或绝对坐标

        Returns:
            要点击的最终位置
            :param template:


        """
        try:
            _pos = loop_find(template, timeout=10, driver=self)
        except Exception as e:
            logger.warning(f"图色识别到坐标失败:{template}:{e}")
            return None

        x, y = _pos
        logger.info(f"图色识别到坐标成功:{template}:{x,y}")
        self.action.move_to( (x,y))
        self.action.click()
        logger.info(f"{x,y}点击完成")

        time.sleep(1)

        return _pos


