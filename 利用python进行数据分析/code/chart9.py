#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
第9章：数据聚合与分组运算
主要内容:
    1、根据一个或多个键拆分pandas对象
    2、计算分组摘要统计，如计数、平均值、标准差，用户自定义函数
    3、对df的列应用各种函数
    4、应用组内转换或其他运算，如规格化、线性回归、排名、选取子集等
    5、计算透视表或交叉表
    6、执行分位数分析以及其他分组分析
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


def group_skill():
    """groupBY"""
    df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                    'key2': ['one', 'two', 'one', 'two', 'one'],
                    'data1': np.random.randn(5),
                    'data2': np.random.randn(5)})
    # print(df)
    # series作为分组键
    # grouped = df['data1'].groupby(df['key1'])
    # print(grouped.mean())  # 按key1分组
    # means = df['data1'].groupby([df['key1'], df['key2']]).mean()

    # 数组作为分组建
    # states = np.array(['bj', 'hb', 'hb', 'bj', 'bj'])
    # years = np.array([2005, 2005, 2006, 2005, 2006])
    # print(df['data1'].groupby([states, years]).mean())

    # 列名作为分组建
    # print(df.groupby(['key1', 'key2']).mean())

    # 2 对分组进行迭代
    # for name, group in df.groupby('key1'):
        # print('-' * 50)
        # print(name)  # a,b
        # print('-' * 50)
        # print(group)
        # print('-'*50)

    # for (k1, k2), group in df.groupby(['key1', 'key2']):
    #     print(k1, k2)
    #     print(group)

    # 3 把数据片段当作字段
    # print(dict(list(df.groupby('key1'))))
    # print(df.dtypes)

    # 4 需求一个或一组列
    # print(df.groupby('key1')['data1'])
    # print(df.groupby('key1')[['data2']])
    # print(df['data1'].groupby(df['key1']))
    # print(df[['data2']].groupby(df['key1']))
    # print(df.groupby(['key1', 'key2'])['data2'].mean())

    # 5 通过字段或Series进行分组
    people = DataFrame(np.random.randn(5, 5),
                       columns=['a', 'b', 'c', 'd', 'e'],
                       index=['Joe', 'Steve', 'Wes', 'Jim', 'Traavis'])
    people.ix[2:3, ['b', 'c']] = np.nan  # 第3行的'b,'c'列设置为Nan
    mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f': 'orange'}
    print(people.groupby(mapping, axis=1).sum())


def data_group():
    """数据聚合：任何能够从数组产生标量值的转换过程"""
    df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                    'key2': ['one', 'two', 'one', 'two', 'one'],
                    'data1': np.random.randn(5),
                    'data2': np.random.randn(5)})


if __name__ == "__main__":
    # group_skill()

    data_group()