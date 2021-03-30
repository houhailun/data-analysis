#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/9/6 9:47
# Author: Hou hailun

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from pylab import *


class MyPlt:
    # matplotlib绘图类

    # 绘制正弦和余弦
    def sin_cos_picture(self):
        x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
        C, S = np.cos(x), np.sin(x)
        plt.plot(x, C)
        plt.plot(x, S)
        plt.show()


if __name__ == "__main__":
    my_plt = MyPlt()
    my_plt.sin_cos_picture()