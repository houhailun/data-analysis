#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/5/15 10:32
# Author: Hou hailun

# 透视表：对数据进行动态排布 并 分类汇总

import os
import sys
import numpy as np
import pandas as pd

"""
pd.pivot_table(data,                # dataframe
               values=None,         # 对指定数据进行筛选
               index=None,          # 索引，即对指定的index进行分组汇总
               columns=None,        # columns参数允许我们定义一个或多个列
               aggfunc="mean",      # 默认mean函数，可以指定其他汇总函数
               fill_value=None,
               margins=False,       # margins=True进行汇总, 查看总数
               dropna=True,
               margins_name="All",
               observed=False,)
"""

class PivotTableDemo:
    # 透视表
    def __init__(self):
        self.file_name = 'James_Harden.csv'
        self.data_path = os.path.join(os.getcwd(), 'data')
        self.file_path = os.path.join(self.data_path, self.file_name)

    def load_data(self):
        return pd.read_csv(self.file_path, encoding='GBK')

    def pivot_table_demo(self):
        df = self.load_data()
        print(df.head())

        print(pd.pivot_table(df, index='对手').head())  # 实际上就是把对手作为index
        print(pd.pivot_table(df, index=['对手', '主客场']).head())  # 二层索引：对手，主客场
        # 小结：Index就是层次字段，要通过透视表获取什么信息就按照相应的顺序设置字段

        # values: 对指定数据进行筛选
        print(pd.pivot_table(df, index=['主客场', '对手'], values=['助攻', '得分', '篮板']))

        # aggfunc: 设置对数据聚合时应用的函数操作 默认aggfunc='mean'
        print(pd.pivot_table(df,
                             index=[u'主客场', u'胜负'],
                             values=[u'得分', u'助攻', u'篮板'],
                             aggfunc=[np.sum, np.mean]))

        # columns: 类似于index，可以设置列层次字段，它不是一个必要参数，作为一种分割数据的可选方式。
        # fill_value填充空值,margins=True进行汇总
        print(pd.pivot_table(df,index=[u'主客场'],columns=[u'对手'],values=[u'得分'],aggfunc=[np.sum],fill_value=0,margins=1))


if __name__ == "__main__":
    obj = PivotTableDemo()
    obj.pivot_table_demo()