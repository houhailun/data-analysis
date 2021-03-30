#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/4/26 18:44
# Author: Hou hailun

import datetime
import numpy as np
import pandas as pd

# --------------- 一:习惯用法 ---------------
def part1():
    df = pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]})
    # print(df)

    # if-then
    # 作用于一列:如果AAA大于等于5, BBB列等于-1
    df.ix[df.AAA >= 5, 'BBB'] = -1
    # print(df)

    # 作用于多列
    df.ix[df.AAA >= 5, ['BBB','CCC']] = 555
    # print(df)

    # 或者我们可以设置一个遮罩（mask），学过ps的同学应该有直观印象，没学过望文生义也能猜个差不多
    df_mask = pd.DataFrame({'AAA': [True]*4, 'BBB':[False]*4, 'CCC':[True,False]*2})
    df_mask = df_mask.where(df_mask, -1000)
    print(df_mask)
    # 遮罩为False的都被赋值为-1000

    # python
    # if-then-else 用numpy的where()
    df = pd.DataFrame({'AAA':[4,5,6,7],'BBB':[10,20,30,40],'CCC':[100,50,-30,-50]})
    df['logic'] = np.where(df['AAA']>5, 'high', 'low')
    print(df)


# --------------- 二:切分dataframe ---------------
def part2():
    pass

# --------------- 十:时间序列分析 ---------------
class DateSeriesAnalysis(object):
    def python_vs_pandas_date(self):
        # python和pandas的日期工具的区别
        # date = datetime.date(year=2013, month=6, day=7)
        # time = datetime.time(hour=12, minute=30, second=19, microsecond=463198)
        # dt = datetime.datetime(year=2013, month=6, day=7,
        #                        hour=12, minute=30, second=19, microsecond=463198)
        #
        # diff = datetime.timedelta(weeks=2, days=5)
        # print(date + diff)

        # pandas的Timestamp对象。Timestamp构造器比较灵活，可以处理多种输入
         print(pd.Timestamp(year=2012, month=12, day=21, hour=5, minute=10, second=8, microsecond=99))
         print(pd.Timestamp('2016/1/10'))
         print(pd.Timestamp('2014-5/10'))
         print(pd.Timestamp('Jan 3, 2019 20:45.56'))
         print(pd.Timestamp('2016-01-05T05:34:43.123456789'))


obj = DateSeriesAnalysis()
obj.python_vs_pandas_date()