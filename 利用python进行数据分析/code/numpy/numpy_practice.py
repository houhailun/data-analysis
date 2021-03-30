#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
numpy练习：numpy是python的科学计算和数据处理的包，主要功能：
    ndarray：多维数据，可进行矢量运算
    快速操作处理数组/矩阵的函数
    线性代数、随机数、傅里叶变换等功能
    集成其他语言的代码
"""

import numpy as np


def numpy_test():
    # 创建一维数组
    arr = np.array([1, 2, 3])
    #print(arr, type(arr))

    # 多维数组
    arr1 = np.array([[1,2,3], [4,5,6]])
    #print(arr1)
    #print(arr1.shape)
    #print(arr1.dtype)

    arr2 = np.array(np.arange(12).reshape(3,4))
    #print(arr2)

    # 全0数据
    #print(np.zeros((2,3)))

    # 全1数组
    #print(np.ones((2,3)))

    # 单位数组
    # print(np.eye(2,3))

    # 数组与标量的运算
    arr = np.array([[1,2,3], [4,5,6]])
    #print(arr * arr)  # 对应元素相乘
    #print(arr - arr)  # 对应元素减
    #print(1 / arr)    # 除以每个元素
    #print(arr ** 0.5)  # 作用于每个元素

    # 数组索引与切片
    arr = np.array(np.arange(10))
    # print(arr[4])
    # print(arr[2:5])

    arr2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
    # print(arr2d.shape)
    # print(arr2d[2])
    # print(arr2d[2][:2])
    # print(arr2d[2][2])  # 数组两种索引都ok
    # print(arr2d[2,2])

    # 切片索引
    # print(arr2d[:2])
    # print(arr2d[:2, 1:])  # 子数组

    # 布尔型索引
    names = np.array(['bob', 'joe', 'will', 'bob'])
    print(names == 'bob')  # 数组比较是矢量化的，对所有元素比较，相等为True，否则为false [true false falsr true]

    # 数组转置与轴对称
    arr = np.arange(15).reshape((3, 5))
    # print(arr)    # 3 X 5
    # print(arr.T)  # 5 X 3

    arr = np.random.randn(6, 3)
    # print(np.dot(arr.T, arr))   # 内积

    # 通用函数：对元素级做操作的数组函数
    # np.sqrt  np.exp

    # 输入输出


def numpy_know():
    # 创建数组
    # array = np.array([1, 2, 3, 4])
    # print(array)
    # print(array.dtype)
    # print(array.shape)
    # print(array[0])

    # 0数组
    # arr = np.zeros((5))
    # print(arr)

    # 单位数据
    # arr = np.ones(5)
    # print(arr)

    # 随机数组
    # arr = np.random.random(5)
    # print(arr)

    # 二维数组
    # arr_2d = np.zeros((2, 3))
    # print(arr_2d)
    # print(arr_2d[0][1])  # 2中下标索引都可以
    # print(arr_2d[0, 1])

    # 提取多为数组的行列
    # arr = np.array([[4, 5], [6, 1]])
    # print(arr)
    # print(arr[0, :])  # 第1行
    # print(arr[:, 1])  # 第2列

    # 数组的操作：单个元素进行操作
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    # sum = a + b
    # diff = a - b
    # product = a * b
    # quotient = a / b
    # print('sum:\n', sum)
    # print('diff:\n', diff)
    # print('product:\n', product)
    # print('quotient:\n', quotient)

    # matrix_product = a.dot(b)  # 矩阵乘法
    # print(matrix_product)


def numpy_start_learn():
    """简单入门教程"""
    # PART1: 数组基础
    # 以不同方式创建数组  --向量
    # a = np.array([0, 1, 2, 3, 4])
    # b = np.array((0, 1, 2, 3, 4))
    # c = np.arange(5)
    # d = np.linspace(0, 2*np.pi, 5)

    # 多维数组
    a = np.array([[11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25],
                  [26, 27, 28, 29, 30],
                  [31, 32, 33, 34, 35]])
    # print(a[0, 1:4])  # [12, 13, 14]
    # print(a[1:4, 0])  # [16, 21, 26]
    # print(a[::2, ::2])  # [[11, 13, 15], [21, 23, 25], [31, 33, 35]]
    # print(a[:, 1])  # [12, 17, 22, 27, 32]

    # 数组属性
    # print(type(a))
    # print(a.dtype)  # 元素类型
    # print(a.size)   # 元素个数
    # print(a.shape)
    # print(a.itemsize)  # 单个元素所占内存字节数
    # print(a.ndim)      # 维度
    # print(a.nbytes)    # 所占内存字节数 = a.size * a.itemsize

    # PART2 使用数组
    # 基本操作符
    a = np.arange(25).reshape((5, 5))
    b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
                  4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
                  56, 3, 56, 44, 78])
    b = b.reshape((5, 5))

    # print(a + b)  # 对应位置的元素相加
    # print(a - b)
    # print(a * b)
    # print(a / b)
    # print(a ** 2)
    # print(a < b)  # 布尔型数组
    # print(a.dot(b))  # 矩阵乘法，点积

    # 数组特殊运算符
    # a = np.arange(10)
    # print(a.sum())
    # print(a.min())
    # print(a.max())
    # print(a.cumsum())

    # PART3 索引进阶
    # 花式索引 --使用整型数组作为索引
    # a = np.arange(0, 100, 10)
    # indices = [1, 5, -1]
    # b = a[indices]  # 获取a中下标为1，5，最后一个数字
    # print(a)
    # print(b)

    # 布尔屏蔽  --通过一个布尔数组来索引目标数组，以此找出与布尔数组中值为True的对应的目标数组中的数据
    # import matplotlib.pyplot as plt
    # a = np.linspace(0, 2*np.pi, 50)
    # b = np.sin(a)
    # plt.plot(a, b)
    # mask = b >= 0
    # plt.plot(a[mask], b[mask], 'bo')
    # mask = (b >= 0) & (a <= np.pi / 2)
    # plt.plot(a[mask], b[mask], 'go')
    # plt.show()

    # 缺省索引  --不完全索引是从多维数组的第一个维度获取索引或切片的一种方便方法
    # a = np.arange(0, 100, 10)
    # print(a[:5])       # [ 0 10 20 30 40]
    # print(a[a >= 50])  # [50 60 70 80 90]

    # Where函数 --where() 函数是另外一个根据条件返回数组中的值的有效方法。只需要把条件传递给它，它就会返回一个使得条件为真的元素的列表。
    a = np.arange(0, 100, 10)
    b = np.where(a < 50)
    c = np.where(a >= 50)[0]
    print(b)  # (array([0, 1, 2, 3, 4]),)
    print(c)  # [5 6 7 8 9]


def numpy_course():
    """numpy教程"""
    # 广播Broadcasting
    # 广播是一种强大的机制，它允许numpy在执行算术运算时使用不同形状的数组。
    # 通常，我们有一个较小的数组和一个较大的数组，我们希望多次使用较小的数组来对较大的数组执行一些操作
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    # y = np.empty_like(x)   # y和x有相同shape，元素为0
    #
    # for i in range(4):
    #     y[i, :] = x[i, :] + v
    # print(y)

    # vv = np.tile(v, (4, 1))
    # y = x + vv

    # 广播允许我们在不创建v的多个副本的情况下计算
    y = x + v
    print(y)
    """
    数组维度不同，后缘维度的轴长相符
    数组维度相同，其中有个轴为1
    """


def numpy_document():
    """ https://www.numpy.org.cn/article/basics/python_numpy_tutorial.html """
    numpy_know()  # 理解Numpy

    numpy_start_learn()  # Numpy简单入门教程

    numpy_course()  # Numpy教程


if __name__ == "__main__":
    # numpy_test()

    numpy_document()