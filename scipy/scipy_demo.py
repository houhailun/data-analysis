#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/5/21 15:44
# Author: Hou hailun

# Scipy
# 内置了图像处理， 优化，统计等等相关问题的子模块
# scipy 是Python科学计算环境的核心。 它被设计为利用 numpy 数组进行高效的运行。从这个角度来讲，scipy和numpy是密不可分的。

from scipy import io as spio


def io_demo():
    # 保存mat格式文件
    spio.savemat('test.mat', {'a': 12})
    # 加载mat文件
    data = spio.loadmat('test.mat')
    print(data)


def linalg_demo():
    # 线性代数操作
