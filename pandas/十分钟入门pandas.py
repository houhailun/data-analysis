#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/4/7 18:03
# Author: Hou hailun


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class PandasDemo:
    # 十分钟入门Pandas
    def apply_demo(self):
        # apply函数
        df = pd.DataFrame([[1,2], [3,4]], columns=['A', 'B'])
        print(df.head())

        print(df.apply(np.cumsum))
        print(df.apply(lambda x: x.max() - x.min()))

    def hist_demo(self):
        # 直方图
        s = pd.Series(np.random.randint(0, 7, size=10))
        print(s.value_counts())  # 值的个数

    def str_demo(self):
        # 字符串方法: series的str属性包含一组字符串处理功能
        s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
        print(s.str.lower())

    def merge_demo(self):
        # 合并
        # concat: 连接pandas对象
        def concat_demo():
            df = pd.DataFrame(np.random.randn(10, 4))
            pieces = [df[:3], df[3:7], df[7:]]
            print(pd.concat(pieces, axis=0))  # 跨行上下拼接
        # concat_demo()

        def join_demo():
            # sql风格的合并
            left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
            right = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [4, 5]})
            print(pd.merge(left, right, on='key'))  # 类似于sql的join

            left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
            right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
            print(pd.merge(left, right, on='key'))
        # join_demo()

        def append_demo():
            # append(): 追加行
            df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
            s = df.iloc[3]
            print(df.append(s, ignore_index=True))

        append_demo()

    def group_demo(self):
        # 分组groupby:
            # 1、分割：按条件把数据分割为多组
            # 2、应用：为每组单独应用函数
            # 3、将处理结果组合成一个数据结构
        df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                           'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                           'C': np.random.randn(8),
                           'D': np.random.randn(8)})
        print(df.groupby('A').sum())  # 对A列分组，每个分组应用sum(), 组合为df
        print(df.groupby(['A', 'B']).sum())  # 多層索引

    def reshape_demo(self):
        # 重塑: reshape
        pass


if __name__ == "__main__":
    obj = PandasDemo()

    # obj.apply_demo()
    # obj.hist_demo()
    # obj.str_demo()
    # obj.merge_demo()
    obj.group_demo()