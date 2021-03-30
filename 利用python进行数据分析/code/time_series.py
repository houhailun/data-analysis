#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
时间序列：在多个时间点观察或测量到的任何事物都可以形成一段时间序列
主要分为以下几种：
    1、时间戳 timestamp,特定的时刻
    2、固定时期 period
    3、时间间隔 interval
    4、实验或过程时间，每个时间点都是相对于特定起始时间的一个度量
"""

from datetime import datetime
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


def part1():
    """日期和时间数据类型及工具"""
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)

    delta = datetime.datetime(2011, 1, 7) - datetime.datetime(2008, 6, 24)
    print(delta)


def part2():
    """时间序列基础"""
    # 1、pandas最基本的时间序列：以时间戳为索引的Series
    dates = [datetime(2011,1,2), datetime(2011,1,5), datetime(2011,1,7),
             datetime(2011,1,8), datetime(2011,1,10), datetime(2011,1,12)]
    ts = Series(np.random.rand(6), index=dates)
    # print(ts)
    # print(type(ts))
    # print(ts.index)
    # print(ts.index[0])

    # 索引、选取、子集构造
    # print(ts[ts.index[2]])  # 利用索引
    # print(ts['1/10/2011'])  # 利用被解释为日期的字符串

    longer_ts = Series(np.random.randn(1000),
                       index=pd.date_range('1/1/2000', periods=1000))
    # print(longer_ts)
    # print(longer_ts['2001-05'])  # 较长的时间序列，只需传入年或者年月，即可选取数据切片
    # print(ts[datetime(2011, 1, 7)])
    # print(ts['1/6/2011': '1/10/2011'])  # 范围查询

    dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
    long_df = DataFrame(np.random.rand(100, 4),
                        index=dates,
                        columns=['bj', 'hb', 'cd', 'hn'])
    # print(long_df.ix['2001-05'])  # 行索引

    # 带重复索引的时间序列
    dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
    dup_ts = Series(np.arange(5), index=dates)
    # print(dup_ts)
    # print(dup_ts.index.is_unique)   # index不唯一
    # print(dup_ts['1/3/2000'])  # 索引唯一，产生标量
    # print(dup_ts['1/2/2000'])  # 索引不唯一，产生切片

    # want：对具有非唯一时间戳的数据进行聚合：groupby，并传入level=0（索引的唯一一层）
    grouped = dup_ts.groupby(level=0)
    print(grouped.mean())
    print(grouped.count())


def part3():
    """日期的范围、频率以及移动"""
    dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
             datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
    ts = Series(np.random.rand(6), index=dates)

    # 问题：时间序列一般是不规则的，没有固定频率的，但是常常需要以某种固定的频率分析，这样会在时间序列中引入缺失值
    # pandas有一套标准时间序列频率以及用于重采样、频率推断、生成固定频率日期范围的工具
    # 1、把ts转换为固定频率（每日）的时间序列
    # print(ts.resample('D').asfreq())  # 新版本resample后返回DatetimeIndexResampler对象，需要通过asfreq()获取值

    # 2、生成日期范围u
    index = pd.date_range('4/1/2012', '6/1/2012')
    # print(index)  # 生成指定范围的日期数据，默认情况data_range按天计算
    # print(pd.date_range(start='4/1/2012', periods=20))  # 如果只有起始或结束日期，那么还需传入表示一段时间的数字
    # print(pd.date_range(end='4/1/2012', periods=20))
    # print(pd.date_range('1/1/2000', '12/1/2000', freq='BM'))  # 在时间范围内符合频率要求的日期(BM：每个月最后一个工作日)

    # 书上normalize=True表示规范化到午夜，实际上True会去掉时间戳的时间信息
    # print(pd.date_range('5/2/2012 12:56:31', periods=5, normalize=False))

    # 3、频率和日期偏移量
    # pandas的频率由一个基础频率(‘M’-每月，‘H’-每小时，‘D'-每天)和一个乘数组成
    # print(pd.date_range('1/1/2000', '1/3/2000', freq='4h'))  # 每间隔4小时
    # print(pd.date_range('1/1/2000', periods=10, freq='1h30min'))  # 间隔150min,产生10个数据

    # 4、WOM日期(week of month)
    rng = pd.date_range('1/1/2012', '9/1/2012', freq='WOM-3FRI')
    # print(rng)  # 每月第3个星期五

    # 5、移动(超前和滞后)数据
    ts = Series(np.random.randn(4),
                index=pd.date_range('1/1/2000', periods=4, freq='M'))
    # print(ts)
    # print('-'*30)
    # print(ts.shift(2))  # 后移
    # print(ts.shift(-2))  # 前移

    # 单纯的移位不会操作索引，所以造成部分数据丢弃，如果频率已知，可以对时间戳进行移位，这样不会丢弃数据
    # print(ts.shift(2, freq='M'))

    # 6、通过偏移量对日期进行位移


def part4():
    """时区处理"""
    import pytz
    # print(pytz.common_timezones[-5:])  # 时区名
    # print(pytz.timezone('US/Eastern'))  # 时区对象

    # 1、本地化和转换
    # 默认，pandas中德时间序列是naive时区,也就是没有时区的
    rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
    ts = Series(np.random.randn(len(rng)), index=rng)
    # print(ts.index.tz)

    rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D', tz='UTC')
    ts_utc = Series(np.random.randn(len(rng)), index=rng)
    # print(ts_utc.index.tz)

    # 通过tz_localize方法可以为没有时区的时间序列赋予时区
    ts_utc = ts.tz_localize('UTC')
    # print(ts_utc)

    # 一旦时间序列被本地化到某个特定时区，就可以用tz_convert将其转换到别的时区了
    # print(ts_utc.tz_convert('US/Eastern'))

    # 2、操作时区意识型Timestamp对象
    stamp = pd.Timestamp('2022-03-12 04:00')
    stamp_utc = stamp.tz_localize('utc')
    stamp_utc.tz_convert('US/Eastern')

    # 3、不同时区之间的运算
    # 两个不同时间序列的时区计算时会自动变为UTC


def part5():
    """时期与算术运算"""
    # 1 时期period表示的是时间区间，比如数日、数月等
    p = pd.Period(2007, freq='A-DEC')  # 表示2007/1/1~2007/12/31
    # print(p)
    # print(p+5)
    # print(pd.Period(2012, freq='A-DEC') - p)

    # 创建规则的时期范围
    rng = pd.period_range('1/1/2000', '6/20/2000', freq='M')
    # print(rng)

    # 2 时期的频率转换
    # period，periodIndex对象通过asfreq方法转换为别的频率
    p = pd.Period('2007', freq='A-DEC')
    print(p.asfreq('M', how='start'))  # 转换为当年年初的一个月度时期
    print(p.asfreq('M', how='end'))  #  转换为当年年末的一个月度时期


if __name__ == "__main__":
    # part1()

    # part2()

    # part3()

    # part4()

    part5()