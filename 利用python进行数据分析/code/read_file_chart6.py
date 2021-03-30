#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
数据加载、存储与文件格式

pandas中的解析函数:
    read_csv        读取csv文件，逗号分隔符
    read_table      读取制表符
    read_fwf        读取定宽列格式数据(没有分隔符)
文本->dataFrame的技术：
    1、索引：将一个或多个列当作返回的df处理，以及是否从文件、用户获取列明
    2、类型推断和数据转换：包括用户定义值的转换、缺失值标记列表等
    3、日期解析：包括组合功能
    4、迭代：支持对大文件进行逐快迭代读取
    5、不规整数据问题：跳过一些行、页脚、注释等
"""

import pandas as pd

def read_file():
    # 两种读取csv文件方法
    # df = pd.read_csv('text.csv')
    # df = pd.read_table('text.csv', sep=',')
    # print(df.count())
    # print(df.head())

    # 逐块读取文本文件
    # df = pd.read_csv('text.csv', nrows=5)  # 读取5行
    # chunker = pd.read_csv('text.csv', chunksize=1000)  # 逐快读取，每次读取1000行
    # for x in chunker:  # 遍历读取


def write_file():
    # 写到csv文件
    df.to_csv('text1.csv')
    df.to_csv(sys.stdout, sep='|')  # |分隔符


def json_file():
    pass

if __name__ == "__main__":
    read_file()