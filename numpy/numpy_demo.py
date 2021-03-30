#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/3/26 10:59
# Author: Hou hailun

# Numpy 库
# 功能强大的N维数组对象。
# 精密广播功能函数。
# 集成 C/C+和Fortran 代码的工具。
# 强大的线性代数、傅立叶变换和随机数功能。
import sys
import numpy as np

#
# ------------ 基础知识 ------------
#
# a = np.array([[1,0,0], [2,3,4]])  # 用array()来构建ndarray
# print(a.ndim)  # 维度，轴的个数
# print(a.shape)  # 2X3
# print(a.size)   # 元素个数
# print(a.dtype.name)  # 数据类型
# print(a.data)   # 缓冲区包含数组的实际元素
# print(a.itemsize)  # 每个元素的字节大小

# ------------ 数组创建 ------------
# 方法1：python列表或者元组创建数组
a = np.array([2,3,4])             # 一维数组
b = np.array([(1,2,3), (4,5,6)])  # 二维数组
c = np.array([[2,3], [4,5]], dtype=complex)  # 显示指定数组类型

# 方法2：np的函数创建有初始占位符内容的数组
# print(np.zeros((3,4)))  # 注意参数为列表或者元组
# print(np.ones((2,3)))
# print(np.empty((2,3)))

# 方法3：创建数字数组
# print(np.arange(10, 30, 5))  # 数组，非列表
# print(np.arange(0, 2, 0.3))  # float数组，由于有限的浮点精度，通常不可能预测所获得的元素的数量
# print(np.linspace(0, 2, 9))  # 在指定的间隔内返回均匀间隔的数字，num执行个数
#
# print(np.arange(10000).reshape(100, -1))
# np.set_printoptions(threshold=sys.maxsize)
# print(np.arange(10000).reshape(100, -1))  # 强制NumPy打印整个数组

# ------------ 基本操作 ------------
# 矩阵的算数操作(应用在元素级)
a = np.array([10,20,30,40])
b = np.arange(4)
# print(a-b)
# print(a*b)  # 乘法运算符，对应元素相乘
# print(a@b)  # 矩阵相乘，py>3.5
# print(np.dot(a,b))  # 同上

# 一元操作
# a = np.random.random((2, 3))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.min())
# print(a.min(axis=0))
# print(a.min(axis=1))
# print(a.max())
# print(a.max(axis=0))
# print(a.max(axis=1))
# axis=0，跨行
# axis=1，跨列

# ------------ 通用函数ufunc: 函数在数组上按元素进行运算，产生一个数组作为输出 ------------
# b = np.arange(3)
# print(np.exp(b))
# print(np.sqrt(b))
# print(np.all([1,1,1,0]))  # 测试数组全部元素是否为真
# print(np.any([1,1,1,0]))  # 测试数组元素是否有一个为真
# print(np.argmax([[1,2,3], [5,4,3]]))  # 返回最大值的索引
# print(np.argmax([[1,2,3], [5,4,3]], axis=0))  # 跨行
# print(np.argmax([[1,2,3], [5,4,3]], axis=1))  # 跨列
# print(np.argsort([[1,2,3], [5,4,3]]))  # 索引排序索引
# print(np.sort([[1,2,3], [5,4,3]]))
# print(np.average([1,2,3,4]))  # 带weights的平均
# print(np.average([1,2,3,4], weights=[0,1,2,3]))  # (1*0+2*1+3*2+4*3) / 4
# print(np.bincount([1,1,1,1]))  # 统计bin在x出现的次数，what is bin？长度是x中最大值的+1
# print(np.ceil(1.2))  # 向上取整
# print(np.corrcoef([1,2,3], [4,5,6]))  # 相关系数

# ------------ 索引、切片和迭代 ------------
# 一维数组可以索引、切片和迭代。和python操作相同
a = np.arange(10) ** 3
# print(a)
# print(a[2])
# print(a[2:5])
# print(a[::-1])
# for i in a:
#     print(i)

# 多维数组,每个轴都有一个索引
def f(x, y):
    return 10*x + y
b = np.fromfunction(f, (5,4), dtype=int)
# print(b)
# print(b[2,3])   #
# print(b[2][3])  # 同上
# print(b[:5, 1])  # 前5行，第1列
# print(b[:, 1])
# print(b[1:3,:])
# 行迭代
# for row in b:
#     print(row)
# # 对元素迭代
# for elem in b.flat:  # flat属性是数组的所有元素的迭代器
#     print(elem)


#
# ------------ 形状操纵 ------------
#
def array_shape_mani():
    # ------------ 改变数组的形状 ------------
    def array_shape():
        a = np.floor(10*np.random.random((3,4)))
        print(a.shape)

        print(a.ravel())  # 返回一个一维数组，相当于把多维数组展开
        print(a.reshape(6, 2))
        print(a.T)
        a.resize(2,6)  # 会改变数组本身
        print(a)

    # ------------ 将不同数组堆叠在一起 ------------
    def array_stack():
        a = np.floor(10 * np.random.random((2, 2)))
        print(a)
        b = np.floor(10 * np.random.random((2, 2)))
        print(b)

        print('-'*20)
        print(np.vstack((a, b)))  # 垂直方向堆叠
        print(np.hstack((a, b)))  # 水平方向堆叠

    # array_stack()

    # ------------ 将一个数组拆分为几个较小的数组 ------------
    def array_split():
        a = np.floor(10 * np.random.random((2, 12)))
        print(np.hsplit(a, 3))  # 沿水平轴进行分割
        print(np.vsplit(a, 2))  # 沿垂直轴进行分割

    # array_split()
# array_shape_mani()

#
# ------------ 拷贝和视图 ------------
#
def copy_and_view():
    def no_copy():
        # 完全不复制
        a = np.arange(12)
        b = a
        print(b is a)
        b.shape = 3, 4
        print(b.shape)
        print(a.shape)
    # no_copy()

    def view_or_copy():
        # 试图或者浅拷贝
        a = np.arange(12)
        c = a.view()  # view() 创建一个查看相同数据的新数组对象
        print(c is a)  # False
        print(c.base is a)  # True
        c.shape = 2, 6
        print(a.shape)
        c[0][4] = 1234
        print(a)
    # view_or_copy()

    def deepcopy():
        # 深拷贝
        # 生产数据的副本
        a = np.arange(12).reshape(3, 4)
        b = a.copy()
        print(b is a)
        b[0,0] = 9999
        print(a)
    # deepcopy()
# copy_and_view()

#
# ------------------- Less基础 -------------------
#
def less():
    # 广播规则
    # 广播允许通用功能以有意义的方式处理不具有完全相同形状的输入。
    # 广播的第一个规则是，如果所有输入数组不具有相同数量的维度，则将“1”重复地预先添加到较小数组的形状，直到所有数组具有相同数量的维度。
    # 广播的第二个规则确保沿特定维度的大小为1的数组表现为具有沿该维度具有最大形状的数组的大小。假定数组元素的值沿着“广播”数组的那个维度是相同的。
    # 应用广播规则后，所有数组的大小必须匹配。更多细节可以在广播中找到。
    pass


#
# ------------------- 花式索引和索引技巧 -------------------
#
def fancy_index():
    # 花式索引和索引技巧
    def array_index():
        # 使用索引数组进行索引
        a = np.arange(12) ** 2
        i = np.array([1,1,3,8,5])
        print(a[i])

        j = np.array([[3,4], [9,7]])
        print(a[j])
    # array_index()

    def bool_array_index():
        # 布尔数据进行索引
        a = np.arange(12).reshape(3,4)
        b = a > 4
        print(b)
        print(a[b])

        # 改属性在分配中非常有用
        a[b] = 0
        print(a)
    # bool_array_index()

    def ix_func():
        # ix_()函数可用于组合不同的向量，以便获得每个n-uplet的结果
        a = np.array([2,3,4,5])
        b = np.array([8,5,4])
        c = np.array([5,4,6,8,3])
        ax, bx, cx = np.ix_(a, b, c)
        print(ax)
        print(bx)
        print(cx)
    # ix_func()

    def linear_algebra():
        # 线性代数
        a = np.array([[1.0, 2.0], [3.0, 4.0]])
        print(a.transpose())  # 转置
        print(np.linalg.inv(a))  #

    linear_algebra()

fancy_index()