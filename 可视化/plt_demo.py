#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/3/31 9:51
# Author: Hou hailun

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 显示中文
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False


class MyPlt:
    def __init__(self):
        pass

    def title(self):
        # 添加标题
        x = np.arange(0, 10)
        plt.title("这是一个示例标题")
        plt.plot(x, x*x)
        plt.show()

    def text(self):
        # 添加文字
        x = np.arange(-10, 11, 1)
        y = x * x
        plt.plot(x, y)
        plt.title("这是一个示例标题")
        plt.text(x=-2.5, y=30, s='function y=x*x')  # 添加文字：设置坐标和文字
        plt.show()

    def annotate(self):
        # 添加注释
        x = np.arange(-10, 11, 1)
        y = x * x
        plt.plot(x, y)
        plt.title("这是一个示例标题")
        plt.plot(x, y)
        plt.annotate("这是一个示例注释", xy=(0, 1), xytext=(-2, 22), arrowprops={'headwidth':10,'facecolor':'r'})
        plt.show()

    def twinx(self):
        # 双坐标轴
        x = np.arange(1, 20)
        y1 = x * x
        y2 = np.log(x)
        plt.plot(x, y1)

        # 共享X轴
        plt.twinx()
        plt.plot(x, y2, 'r')
        plt.show()


if __name__ == "__main__":
    my_plt = MyPlt()

    # my_plt.title()
    # my_plt.text()
    # my_plt.annotate()
    my_plt.twinx()