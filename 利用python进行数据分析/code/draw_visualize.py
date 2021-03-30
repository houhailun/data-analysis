#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
绘图和可视化：利用pandas进行绘图
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


def line_chart():
    """线型图"""
    s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
    s.plot()  # series索引作为横坐标，值为纵坐标
    plt.show()

    df = DataFrame(np.random.randn(10, 4).cumsum(0),
                   columns=['a', 'b', 'c', 'd'],
                   index=np.arange(0, 100, 10))
    df.plot()
    plt.show()


def bar_chart():
    """柱状图"""
    fig, axes = plt.subplots(2, 1)
    data = Series(np.random.rand(16), index=list('abcdefghijklmnop'))
    data.plot(kind='bar', ax=axes[0], color='k', alpha=0.7)
    data.plot(kind='barh', ax=axes[1], color='k', alpha=0.7)
    plt.show()


if __name__ == "__main__":
    bar_chart()