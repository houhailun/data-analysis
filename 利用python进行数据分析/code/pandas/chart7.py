#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
数据规整化：清理、转换、合并、重塑
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


def merge_data():
    """合并数据集：merge，concat,combine_first"""
    # 数据库风格的df合并,默认是inner join
    # 1.1 相同列名
    df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                     'data1': range(7)})
    df2 = DataFrame({'key': ['a', 'b', 'd'],
                     'data2': range(3)})
    # print(pd.merge(df1, df2, on='key'. how='inner'))  # 和数据库的join类似

    # 1.2 列名不同
    df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                     'data1': range(7)})
    df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                     'data2': range(3)})
    # print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

    # 2 索引上的合并
    # df的连接键位于索引中
    left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                       'data1': range(6)})
    right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
    # print(pd.merge(left1, right1, left_on='key', right_index=True))

    # 3 轴向连接 concat默认是在axis=0(行)工作
    arr = np.arange(12).reshape((3, 4))
    # print(np.concatenate([arr, arr], axis=1))   # 以列方式复制(3,4)->(3,8)

    s1 = Series([0, 1], index=['a', 'b'])
    s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
    s3 = Series([5, 6], index=['f', 'g'])
    # print(pd.concat([s1, s2, s3]))  # 行连接，变为7行
    # print(pd.concat([s1, s2, s3], axis=1))  # df

    # 4 合并重复数据


def reshape_pivot():
    """重塑、轴向旋转"""
    # 重塑层次化索引: stack-将数据的列转换为行  unstack-将数据的行转换为列
    data = DataFrame(np.arange(6).reshape((2, 3)),
                     index=pd.Index(['Ohio', 'Colorado'], name='state'),
                     columns=pd.Index(['one', 'two', 'three'], name='number'))
    result = data.stack()
    print(result)
    print(result.unstack())  # 默认unstack操作的是最内层，可以传入层级编号
    print(result.unstack('state'))


def data_filter():
    """数据转换：过滤、清理、转换"""
    data = DataFrame({'k1': ['one']*3 + ['two']*4,
                      'k2': [1, 1, 2, 3, 3, 4, 4]})

    # 移除重复数据
    # 1、df的duplicated(), 返回bool型series，表示各行是否为重复行
    # print(data.duplicated())
    # print(data.drop_duplicates())  # 移除重复和，默认判断全部列
    # print(data.drop_duplicates(['k1']))  # 以指定列进行重复行删除
    # print(data.drop_duplicates(['k1', 'k2'], keep='last'))  # 保留最后一个

    # 利用函数或映射进行数据转换
    data = DataFrame({'food': ['bacon', 'pork', 'bacon', 'pastrami', 'beef', 'Bacon', 'pastrami', 'ham', 'lox'],
                      'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
    # want: 添加一列表示该肉类食物来源的动物类型
    meat_to_animal = {
        'bacon': 'pig',
        'pork': 'pig',
        'pastrami': 'cow',
        'beef': 'cow',
        'ham': 'pig',
        'lox': 'salmon'
    }

    # series的map方法可以接收一个函数或含有映射关系的字典对象
    # data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
    # print(data)

    # print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

    # 替换值
    data = Series([1, -999, 2, -999, -1000, 3])
    # print(data.replace(-999, np.nan))  # 把-999改为nan
    # print(data.replace([-999, -1000], np.nan))  # 一次性替换多个值
    # print(data.replace([-999, -1000], [np.nan, 0]))  # 不同的值进行不同的替换
    # print(data.replace({-999: np.nan, -1000: 0}))

    # 重命名轴索引：轴标签通过函数或映射进行转换
    data = DataFrame(np.arange(12).reshape((3, 4)),
                     index=["ohio", 'Colorado', 'New York'],
                     columns=['one', 'two', 'three', 'four'])
    # print(data.index.map(str.upper))  # 把index转换为大写
    # print(data.rename(index=str.title, columns=str.upper))  # 不修改原始数据
    # print(data.rename(index={'ohio': 'INDIANA'}))  # 利用字典实现部分标签轴的而更新

    # 4 离散化和面元划分
    ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
    # 4.1 want:划分为：18~25, 26~35, 35~60, 60~
    bins = [18, 25, 35, 60, 100]
    cats = pd.cut(ages, bins)
    # print(cats)
    # print(pd.value_counts(cats))

    # 4.2 自己设置面元名称
    group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
    # print(pd.cut(ages, bins, labels=group_names))

    # 4.3 cur传入的是面元的数量，会根据数据的最大值和最小值计算等长面元
    data = np.random.randn(20)
    # print(pd.cut(data, 4, precision=2))  # 分为4各面源

    # cut将根据值本身来选择箱子均匀间隔，qcut是根据这些值的频率来选择箱子的均匀间隔
    data = np.random.randn(1000)
    cats = pd.qcut(data, 4)
    # print(pd.value_counts(cats))

    # 5 检查和过滤异常值
    np.random.seed(12345)
    data = DataFrame(np.random.randn(1000, 4))
    # print(data.describe())

    # case1: 过滤某列中绝对值大于3的值
    col = data[3]
    # print(col[np.abs(col) > 3])
    # print(data[(np.abs(data) > 3).any(1)])
    # data[np.abs(data) > 3] = np.sign(data) * 3

    # 6 排列和随机采样 np.random.permutation()
    df = DataFrame(np.arange(5 * 4).reshape((5, 4)))
    sampler = np.random.permutation(5)
    # print(sampler)
    # print(df.take(sampler))  # 对行进行调整
    # print(df.take(np.random.permutation(len(df)))[:3])  # 选取子集

    # 函数shuffle与permutation都是对原来的数组进行重新洗牌（即随机打乱原来的元素顺序）；
    # 区别在于shuffle直接在原来的数组上进行操作，改变原来数组的顺序，无返回值。
    # 而permutation不直接在原来的数组上进行操作，而是返回一个新的打乱顺序的数组，并不改变原来的数组

    # 7 计算指标/哑变量
    # 将分类变量转换为哑变量矩阵或指标矩阵
    df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
    print(df)
    # print(pd.get_dummies(df['key']))
    dummies = pd.get_dummies(df['key'], prefix='key')
    # print(dummies)
    # print(df[['data1']].join(dummies))


def string():
    """字符串操作"""
    # 字符串对象方法
    val = 'a,b, guido'
    # print(val.split(','))  # split(): 字符串 -> 字符串列表
    # print([x.strip() for x in val.split(',')])  #  strrp():去除空白符

    # 字符串拼接
    # print('i' + ':' + 'py')
    # print(':'.join(['i', 'py']))  # 速度更快，更符合python风格
    # 内置的字符串方法
    # count()、startswith(),endswith(),join,index,find(),rfind().replace(),strip().split().lower(),upper(),ljust(),rjust()

    # 正则表达式
    import re
    text = "foo  bar\t baz  \tqux"
    # print(re.split('\s+', text))  # \s匹配空格
    regex = re.compile('\s+')
    regex.split(text)
    # print(regex.findall(text))  # 匹配的所有模式

    # pandas中矢量化的字符串函数



if __name__ == "__main__":
    # merge_data()
    # reshape_pivot()
    # data_filter()
    string()