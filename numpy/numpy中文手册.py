#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/7/22 16:32
# Author: Hou hailun

# Numpy是python的科学计算包，主要包括：
#   功能强大的N维数组对象
#   精密的广播功能函数
#   集成C/C++和Fortran代码的工具
#   强大的线性代数、傅立叶变换和随机数功能

import numpy as np

# 基础知识
data = [[1, 2, 3], [4, 5, 6]]
arr = np.array(data)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
print(arr.data)

# 数组shape固定，元素不定，起占位，避免扩展数组
print(np.ones((2, 3)))
print(np.zeros((2, 3)))
print(np.empty((2, 3)))

# 数字数组的另一方式  数组非列表
print(np.arange(10))
print(np.arange(10, 20, 2))  # 10~20范围内，间隔为2
print(np.linspace(0, 2, 8))  # 0~2范围内取8个数

print('-'*30)
# 打印
arr = np.arange(12).reshape((3, 4))
print(arr[0])

# 运算符
# 数组的运算会应用到元素级别上
arr = np.array( [20,30,40,50] )
b = np.arange(4)
print(arr - b)
print(b ** 2)

print('-'*30)
A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )
print(A * B)  # 对应元素相乘
print(A @ B)  # 矩阵相乘
print(np.dot(A, B))  # 矩阵相乘