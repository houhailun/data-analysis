#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
pandas库练习测试

pandas两大数据结构：
    Series: 类似于list，由一组数据以及一组与之相关的索引组成
    DataFrame：类似于二维多维数组，由数据和行/列坐标索引组成
"""

import numpy as np
import pandas as pd
import datetime
from pandas import Series, DataFrame


def series_test():
    # 创建Series,默认索引
    obj = Series([4, 7, -5, 3])
    # print(obj)  # 索引在左(默认为0~n)，值在右

    # print(obj.values)  # 通过values属性获取数据
    # print(obj.index)   # 通过index属性获取索引

    # 创建Series，设置索引
    obj2 = Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
    # print(obj2)

    # 通过索引获取值、赋值
    # print(obj2['a'])
    # print(obj2[['a', 'b', 'c']])

    # 数组运算
    # print(obj2[obj2 > 0])
    # print(obj2 * 2)
    # print(np.exp(obj2))

    # 把Series看作字典
    # print('a' in obj2)

    # 通过字典来创建,key作为索引，values作为值
    sdata = {'ohio': 35000, 'texas': 71000, 'oregon': 16000, 'utah': '5000'}
    obj3 = Series(sdata)
    # print(obj3)

    obj4 = Series(sdata, index=['sss', 'ohio', 'texas', 'utah'])
    # print(obj4)

    # print(pd.isnull(obj4))  # 检测缺失数据
    # print(pd.notnull(obj4))

    # 重要功能：series在算术运算中会自动对齐不同索引的数据
    # print(obj3)
    # print(obj4)
    # print(obj3 + obj4)

    # series对象及其索引都有一个name属性
    obj4.name = 'population'
    obj4.index.name = 'state'
    # print(obj4.name)
    # print(obj4.index.name)


def dateframe_test():
    # DataFrame是一个表格型数据结构，含有一组有序的列，每列可以是不同的值类型，既有行索引，又有列索引
    # 构建df：字典创建,key作为列索引
    data = {'state': ['ohio', 'ohio', 'ohio', 'nevada', 'nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    # print(frame)

    # 指定列顺序
    # print(DataFrame(data, columns=['year', 'state', 'pop']))

    # 通过字典标记方式或者属性的方式，把df转换为series
    # print(frame['state'])
    # print(frame.year)

    # 行可以通过使用索引字段ix通过行标签或者行号索引数据
    # print(frame.ix[2])

    # 列可以通过赋值的方式进行修改,不存在的列自动创建新列
    frame['debt'] = np.array(5)
    # print(frame)

    # del删除列
    del frame['debt']

    # 列标签,返回列表
    # print(frame.columns)

    # 索引对象：负责管理轴标签和其他元数据


def basic_skill():
    """介绍series和dataframe的基本功能"""

    obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    # print(obj)

    # 1、重新索引:使用reindex函数来重新设置索引, fill_value表示索引不存在填充指定值(默认为Nan)
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
    # print(obj2)

    # 2、重新索引，插值（method=‘ffill’表示前向填充，即把缺失前面的值复制）
    obj3 = Series(['blue', 'red', 'yellow'], index=[0, 1, 4])
    # print(obj3)
    # print(obj3.reindex(range(5), method='ffill'))

    # Dataframe，reindex会修改行、列
    frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['hebei', 'henna', 'beijing'])
    # print(frame)

    # frame2 = frame.reindex(['a', 'b', 'c', 'd'])
    # print(frame2)

    # 使用columns关键字重新索引列
    states = ['beijing', 'hebei', 'henna']
    # print(frame.reindex(columns=states))

    # 2、丢弃指定轴上的项
    obj = Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
    # print(obj)

    new_obj = obj.drop('a')
    # print(new_obj)

    # print(frame.drop(['c', 'a']))  # 删除行, axis=0表示行
    # print(frame.drop('henna', axis=1))  # 删除列，axis=1表示列

    # 3、索引、选取和过滤
    # Series索引类似numpy数组的索引
    obj = Series(np.arange(4.0), index=['a', 'b', 'c', 'd'])
    # print(obj)

    # print(obj['b'])  # 通过index索引
    # print(obj[1])    # 通过行号索引
    # print(obj[2: 4])
    # print(obj[obj > 2])

    # DataFrame的索引其实就是获取一个或多个列
    data = DataFrame(np.arange(16).reshape((4, 4)),
                     index=['beijing', 'hebei', 'henan', 'sichuan'],
                     columns=['one', 'two', 'three', 'four'])
    # print(data[['two', 'one']])

    # 选取行
    # print(data[:2])  # 选取前2行
    # print(data['three'] > 5)  # 选取three列大于5的数据

    # df行上进行标签索引
    # print(data.ix['beijing', ['one', 'two']])
    # print(data.ix[2])  # 第3行

    """
    小结：
    obj[val]: 选取df的单个列或一组列
    obj.ix[val]: 选取df的单个行货一组行
    obj.ix[:, val]: 选取单个列或者列子集
    obj.ix[val1, val2]: 同时选取行和列
    reindex(): 重新索引
    """

    # 4、算术运算和数据对齐
    # 4.1 对不同索引的对应进行算术运算时，如果存在不同的索引对，则结果的索引就是改索引对的并集
    s1 = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = Series([5, 6, 7, 8], index=['b', 'd', 'e', 'f'])
    # print(s1 + s2)  # 自动的数据对齐操作在不重叠的索引处引入了NaN

    # df对齐同时发生在行和列上
    df1 = DataFrame(np.arange(9).reshape((3, 3)),
                    columns=list('bcd'),
                    index=['beijing', 'tianjin', 'hebei'])
    df2 = DataFrame(np.arange(12).reshape((4, 3)),
                    columns=list('bde'),
                    index=['beijing', 'tianjin', 'xian', 'cd'])
    # print(df1 + df2)

    # 4.2 在算术中添加填充值(问题：只填充了部分，并且填充的不是0)
    # print(df1.add(df2, fill_value=0))

    # 4.3 df与series的运算
    arr = np.arange(12).reshape((3, 4))
    # print(arr - arr[0])  # 第一行为0，广播

    frame = df2
    series = frame.ix[0]
    # print(frame - series)  # 将series的索引匹配到df的列，沿着行一直向下广播(第一行为0)
    series = frame['d']
    # print(series)
    # print(frame.sub(series, axis=0))  # 匹配行，沿着列广播(也就是每列减去指定列元素，axis=0表示匹配行)

    # 5、函数应用和映射
    # 5.1 numpy的ufuncs（元素级数组方法）也可用于pandas
    frame = DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['bj', 'tj', 'hb', 'cd'])
    # print(np.abs(frame))

    # 5.2 将函数应用到列/行形成一维数组
    f = lambda x: x.max() - x.min()
    # print(frame.apply(f))  # 列
    # print(frame.apply(f, axis=1))  # 行

    # 5.3 元素级的oython函数
    format = lambda x: '%.2f' %x
    # print(frame.applymap(format))
    # print(frame['e'].map(format))

    # 6、排序和排名
    # 6.1 对行或列索引进行排序，使用sort_index()
    obj = Series(range(4), index=list('dabc'))
    # print(obj.sort_index())

    # df可以对任一轴上的索引排序
    frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=list('dabc'))
    # print(frame.sort_index())  # 对行索引排序
    # print(frame.sort_index(axis=1, ascending=False))  # 对列索引排序,默认升序，可指定降序

    # 6.2 按值对series排序，sort_values(), 默认值被放到Series末尾
    obj = Series([4, 7, -3, 2])
    # print(obj.sort_values())
    obj = Series([4, np.nan, 7, np.nan, -3, 2])
    # print(obj.sort_values())

    frame = DataFrame({'b': [4, 7, -3, 2],
                       'a': [0, 1, 0, 1]})
    # print(frame.sort_values(by=['a', 'b']))

    # 6.2 排名rank(): 表示在这个数在原来的Series中排第几名，有相同的数，取其排名平均（默认）作为值
    obj = Series([7, -5, 7, 4, 2, 0, 4])
    # print(obj.rank())
    # print(obj.rank(method='first'))  # 根据值在原数据中的顺序给出排名(由小到大排序后的顺序)
    # print(obj.rank(ascending=False, method='max'))  # 按降序排名，使用分组的最大排名

    # 7、带有重复值的轴索引
    obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
    print(obj.index.is_unique)  # 检查索引是否唯一
    # 数据选取会对应多个值


def summary_and_calculation_description_statistics():
    """
    汇总和计算描述统计
    pandas对象有一组常用的数学和统计方法，用于从series中提取某个值，或从df的行或列中提取series，是基于没有缺失数据的假设构建的
    """
    df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                    [np.nan, np.nan], [0.75, -1.3]],
                   index=['a', 'b', 'c', 'd'],
                   columns=['one', 'two'])
    # print(df.sum())  # 按列求和，axis=1 为按行求和(NA会自动派出)

    # 1、sum,mean,cursum
    # 2、describe()：描述数据，产生多个汇总统计，如数据量，均值，方差等等
    # 3、相关系数与协方差 corr(), cov()
    '''
    import pandas_datareader.data as web
    all_data = {}
    start = datetime.datetime(2000, 1, 1)
    end = datetime.datetime(2000, 1, 2)

    for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
        all_data[ticker] = web.DataReader(ticker, 'yahoo', start, end)
    print(all_data)
    '''

    # 4、唯一值、值计数以及成员资格
    obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
    # print(obj.unique())  # 得到series的唯一值数组
    # print(obj.value_counts())  # 计算各值出现的频率
    # print(pd.value_counts(obj.values, sort=False))  # 按频次降序排列
    # print(obj.isin(['b', 'c']))  # 判断矢量化集合的成员资格

    # DataFrame用来输入两列数据，同时value_counts将每列中相同的数据频率计算出来
    df = DataFrame({'a': ['Tokyo', 'Osaka', 'Nagoya', 'Osaka', 'Tokyo', 'Tokyo'],
                    'b': ['Osaka', 'Osaka', 'Osaka', 'Tokyo', 'Tokyo', 'Tokyo']})
    # print(df.apply(pd.value_counts).fillna(0))


def nan_data():
    """处理缺失数据"""

    # 1、过滤缺失数据
    data = Series([1, np.nan, 3.5, np.nan, 7])
    # print(data.isnull())  # 检查是否为Nan
    # print(data.dropna())  # 删除Nan数据
    # print(data[data.notnull()])  # 过滤nan数据

    data = DataFrame([[1, 6, 3], [1, np.nan, np.nan], [np.nan, np.nan, np.nan]])
    # print(data)
    # print(data.dropna())  # 默认情况下丢弃含有NAN的行
    # print(data.dropna(how='all'))  # 丢弃全部为NAN的行
    data[4] = np.nan
    # print(data)
    # print(data.dropna(axis=1, how='all'))  # 只丢弃全部为NAN的列

    # 2、填充缺失数据 fillna()
    print(data.fillna(0))  # 缺失值填充为0
    print(data.fillna({1: 0.5, 4: -1}))  # 通过字典实现不同列填充不同值
    # fillna()会返回新对象，可以直接在当前对象上进行修改
    df.fillna(0, inplace=True)


def hierarchical_index():
    """
    层次化索引：使得在一个轴上拥有多个索引级别，也就是能以低维度形式处理高纬度数据
    """
    data = Series(np.random.randn(10),
                  index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                         [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
    # print(data)
    # print(data.index)
    # print(data['b'])  # 选择一级索引b的数据子集
    # print(data['b':'c']) # data.ix[['b', 'c']]

    # 1、层次化索引在数据重塑和基于分组的操作中非常重要,比如:通过unstack转换为df
    # print(data.unstack())
    # print(data.unstack().stack())


    # 2、重新分级顺序 swaplevel(), sortlevel()
    # 3、根据级别汇总统计
    # df.sum(level='key1')

    # 4、使用dataFrame的列
    frame = DataFrame({'a': range(7),
                       'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                       'd': [0, 1, 2, 0, 1, 2, 3]})
    # print(frame)
    # set_index()把其中一个或多个列转换为行索引，创建一个新的df
    frame2 = frame.set_index(['c', 'd'], drop=False)  # 默认会删除掉变为行索引的列
    # print(frame2)
    # reset_index(): 把层次化索引的级别转移到列里



if __name__ == "__main__":
    # series_test()

    # dateframe_test()

    # basic_skill()

    # summary_and_calculation_description_statistics()

    # nan_data()

    # hierarchical_index()