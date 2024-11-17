import os
import time

import cv2
import numpy as np
from ame_6._error import FileNotExistError
from ._log_mod import logger


def get_resolution(img):
    """
    用于从输入的图像中获取其分辨率（宽度和高度）

    """
    h, w = img.shape[:2]
    return w, h

def imread(filename, flatten=False):
    """根据图片路径，将图片读取为cv2的图片处理格式."""
    if not os.path.isfile(filename):
        raise FileNotExistError("File not exist: %s" % filename)
    #  选择读取模式
    # choose image readin mode: cv2.IMREAD_UNCHANGED=-1, cv2.IMREAD_GRAYSCALE=0, cv2.IMREAD_COLOR=1,
    readin_mode = cv2.IMREAD_GRAYSCALE if flatten else cv2.IMREAD_COLOR

    img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), readin_mode)

    return img

def loop_find(query, driver=None, timeout=10, threshold=None, interval=0.5, intervalfunc=None):
    """
    函数概述：
        loop_find 函数用于在屏幕截图中查找指定的图像模板，并在找到该模板时返回它的位置。如果在指定的超时时间内没有找到图像模板，则会抛出 TargetNotFoundError 错误。

        参数说明：
        query：这是要查找的图像模板（Template 对象），可以通过图像识别来查找屏幕上的匹配项。
        driver：表示驱动对象，通常是设备的控制器（如浏览器或手机模拟器等），它的 screenshot() 方法用于获取屏幕截图。
        timeout：表示查找图像的最大时间，单位是秒，默认值是 10 秒。如果超过这个时间仍然未找到图像模板，则抛出 TargetNotFoundError 错误。
        threshold：可选的参数，表示图像匹配的阈值，默认是 None，通常用于控制图像匹配的精度（例如，值越大，要求匹配得越精确）。
        interval：每次查找之间的时间间隔，单位是秒，默认值是 0.5 秒。每次未找到图像后，函数会等待此间隔再进行下一次查找。
        intervalfunc：一个可选的函数，它会在每次未找到图像时执行（例如可以用来记录日志或者执行某些操作）。
        异常：
        TargetNotFoundError：如果在 timeout 时间内没有找到图像模板，函数将抛出这个错误。
        返回值：
        如果找到了图像模板，返回该模板在屏幕上的位置（match_pos）。
        如果超时后仍未找到图像模板，抛出 TargetNotFoundError 异常。


    """
    start_time = time.time()
    while True:
        screen = driver._screenshot()
        query.resolution = get_resolution(screen)
        if screen is None:
            logger.info("Screen is None, may be locked")


        else:
            if threshold:
                query.threshold = threshold
            match_pos = query.match_in(screen)
            if match_pos:
              return match_pos

        if intervalfunc is not None:
            intervalfunc()

        # 超时则raise，未超时则进行下次循环:
        if (time.time() - start_time) > timeout:
            raise Exception(f"Picture {query} not found in screen'")


        else:
            time.sleep(interval)