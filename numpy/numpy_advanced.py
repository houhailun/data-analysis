#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/4/1 11:30
# Author: Hou hailun

# Numpy 进阶

# Numpy数据分析问题
# 1、导入Numpy作为np，并查看版本
import numpy as np
print(np.__version__)

# 2、创建一维数组，创建从0到9的一维数字数组
arr = np.arange(10)
print(arr)

# 3、创建一个布尔数组
# 创建一个numpy数组元素值全为True（真）的数组
bool_arr = np.full(shape=(3, 3), fill_value=True, dtype=bool)  # 利用填充函数full实现
print(bool_arr)

bool_arr2 = np.ones(shape=(3, 3), dtype=bool)  # 利用ones()函数创建全为1的数组，指定类型为bool
print(bool_arr2)

# 4、如何从一维数组中获取指定条件的元素
# 从 arr 中提取所有的奇数
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_odd = np.array([val for val in arr if val % 2 == 1])  # 利用迭代
arr_odd2 = arr[arr % 2 == 1]  # 利用bool数组索引
print(arr_odd, arr_odd2)

# 5、如何用numpy数组中的另一个值替换满足条件的元素项
# 将arr中的所有奇数替换为-1
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1  # bool数组索引，直接赋值
print(arr)

# 6、如何在不影响原始数组的情况下替换满足条件的元素项
# 将arr中的所有奇数替换为-1，而不改变arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr % 2 == 1, -1, arr)  # where(条件，条件为真取x，条件为假取y)
print(out)

# 7、如何改变数组的形状
# 将一维数组转换为2行的2维数组
arr = np.arange(8)
arr = arr.reshape((2, -1))  # 最后一个轴为-1 自动适应列
print(arr)

# 8、如何垂直叠加两个数组
print(' 垂直叠加两个数组 '.center(40, '*'))
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
print(np.vstack((a, b)))
print(np.concatenate([a, b]))  # axis=0,跨行

# 9、如何水平叠加两个数组
print(' 水平叠加两个数组 '.center(40, '*'))
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
print(np.hstack([a, b]))
print(np.concatenate([a, b], axis=1))  # axis=1，跨列

# 10、如何在无硬编码的情况下生成numpy中的自定义序列？
# 创建以下模式而不使用硬编码。只使用numpy函数和下面的输入数组a
print(' numpy中的自定义序列 '.center(40, '*'))
a = np.array([1, 2, 3])
print(np.hstack([np.repeat(a, 3), np.tile(a, 3)]))
# 注意repeat,tile的区别
# numpy.repeat(a, repeats, axis=None)
#   若axis=None，对于多维数组而言，可以将多维数组变化为一维数组，然后再根据repeats参数扩充数组元素；
#   若axis=M，表示数组在轴M上扩充数组元素
print('-'*40)
a = np.array([[1,2,3], [4,5,6]])
print(np.repeat(a,2))           # axis=None，把多维数组扩展为一维数组，然后元素顺序依次复制2次
print(np.repeat(a, 2, axis=0))  # axis=0，表示跨行，上下复制
print(np.repeat(a, 2, axis=1))  # axis=1, 表示跨列，左右复制

# 11、如何获取两个numpy数组之间的公共项
print(' 两个numpy数组的公共项 '.center(40, '*'))
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.array(set(a) & set(b)))  # set方法
print(np.intersect1d(a, b))

# 12、如何从一个数组中删除存在于另一个数组中的元素
print(' 在A不在B中的元素 '.center(40, '*'))
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print(np.setdiff1d(a, b))  # Return the sorted, unique values in `ar1` that are not in `ar2`.

# 13、如何得到两个数组元素匹配的位置
print(' a和b元素匹配的位置 '.center(40, '*'))
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.where(a==b))

# 14. 如何从numpy数组中提取给定范围内的所有数字？
# 获取5到10之间的所有项目
print(' 指定范围的数字 '.center(40, '*'))
a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5) & (a <= 10))             # where()来获取下标
print(a[index])
index = np.where(np.logical_and(a >= 5, a <= 10))  # logical_and: 逻辑与
print(a[index])

# 15、如何创建一个python函数来处理scalars并在numpy数组上工作
# 转换适用于两个标量的函数maxx，以处理两个数组
print(' 15 '.center(40, '*'))
def maxx(x, y):
    if x >= y:
        return x
    return y

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
# vectorize(pyfunc, otypes=None) 将函数向量化
#   pyfunc： python函数        otypes：输出类型
pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))

# 16、如何交换二维numpy数组中的两列？
print(' 交换数组两列 '.center(40, '*'))
arr = np.arange(9).reshape(3, 3)
print(arr[:, [1, 0, 2]])  # 行不变，交换列1和列2

# 17、如何交换二维numpy数组中的两行
print(' 交换数组两行 '.center(40, '*'))
arr = np.arange(9).reshape(3, 3)
print(arr[[1,0,2], :])   # 列顺序不变，交换行1和行2

# 18、如何反转二维数组的行
print(' 反转二维数组的行 '.center(40, '*'))
arr = np.arange(9).reshape(3, 3)
print(arr[::-1, :])  # 列顺序不变，使用[::-1]反转行

# 19、如何反转二维数组的列
print(' 反转二维数组的列 '.center(40, '*'))
arr = np.arange(9).reshape(3, 3)
print(arr[:, ::-1])   # 行顺序不变，使用[::-1]反转列

# 20、如何创建包含5到10之间随机浮动的二维数组
print(' 创建指定范围内的随机数组 '.center(40, '*'))
rand_arr = np.random.randint(low=5, high=10, size=(5, 3))  # 生成low，high之间的随机整数
rand_arr_float = np.random.random(size=(5, 3))  # 产生0，1之间的随机数
print(rand_arr+rand_arr_float)

# 方法2
rand_arr = np.random.uniform(5, 10, size=(5, 3))  # 在5，10之间的均匀分布上随机采样
print(rand_arr)

# 20、如何在numpy数组中只打印小数点后三位
print(' 设置打印精度 '.center(40, '*'))
rand_arr = np.random.random((5,3))
np.set_printoptions(precision=3)
print(rand_arr)

# 21、如何通过e式科学记数法（如1e10）来打印一个numpy数组
# Reset printoptions to default
np.set_printoptions(suppress=False)

# Create the random array
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
np.set_printoptions(suppress=True, precision=6)  # precision is optional


# 23、如何限制numpy数组输出中打印的项目数
a = np.arange(15)
np.set_printoptions(threshold=6)
print(a)

# 24、如何打印完整的numpy数组而不截断
print(' 打印完整的numpy数组 '.center(40, '*'))
a = np.arange(15)
np.set_printoptions(threshold=np.nan)  # 必须是np.nan，不能是None
print(a)

# 25、如何导入数字和文本的数据集保持文本在numpy数组中完好无损
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = np.genfromtxt(url, delimiter=',', dtype='object')
# names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
# print(iris[:3])

# 26、如何从1维元组数组中提取特定列
