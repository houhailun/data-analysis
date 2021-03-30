#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/5/21 10:57
# Author: Hou hailun

# user_id,item_id,behavior_type,user_geohash,item_category,time
# 用户id | 商品id | 行为 | 用户地址 | 商品分类 | 时间
# 行为包括: 点击1，收藏2，加购物车3，支付4

# 分析
# 1、用户行为转化漏斗
# 2、基础数据统计
# 总PV、总UV、有购买行为的用户数量、复购率、跳失率


import numpy as np
import pandas as pd


class Demo:
    def __init__(self):
        self.df = pd.read_csv('tianchi_mobile_recommend_train_user.csv', nrows=1000000)

    def explore(self):
        # 数据探索
        print(self.df.info())   # user_geohash 存在比较多的null
        print(self.df.describe())

    def process(self):
        # 数据的简单处理
        # 把time转换为时间类型
        self.df['time'] = pd.to_datetime(self.df['time'])
        self.df['hour'] = self.df['time'].dt.hour         # hour
        self.df['time'] = self.df['time'].dt.normalize()  # 年-月-日

        # 为了便于观察，把行为1/2/3/4 转换为对应含义
        self.df.ix[self.df['behavior_type'] == 1, 'behavior_type'] = 'pv'
        self.df.ix[self.df['behavior_type'] == 2, 'behavior_type'] = 'collect'
        self.df.ix[self.df['behavior_type'] == 3, 'behavior_type'] = 'cart'
        self.df.ix[self.df['behavior_type'] == 4, 'behavior_type'] = 'buy'

        # 等同于map
        # self.df['behavior_type'] = self.df['behavior_type'].map({1: 'pv', 2: 'collect', 3: 'cart', 4: 'buy'})

    def basic_analysis(self):
        # 基础数据统计：总PV、总UV、有购买行为的用户数量、复购率、跳失率
        # PV: page view, 页面浏览量，每浏览一次增加1次, 这里等于点击量
        data_pv = self.df[self.df['behavior_type'] == 'pv']
        print(data_pv.shape)  # (942230, 7)

        # uv: user Visitor, 访问网站的一台电脑客户端为一个访客。00:00-24:00内相同的客户端只被计算一次。
        data_uv = self.df.drop_duplicates('user_id')['user_id'].count()
        print(data_uv)  # 8058

        # 有购买行为的用户数量
        data_buy = self.df[self.df['behavior_type'] == 'buy']
        print(data_buy.drop_duplicates('user_id')['user_id'].count())  # 4120

        # 复购率 = 购买2次或以上的用户 / 购买用户总数
        data_buy_much = data_buy.groupby('user_id').count()                # 每个用户购买的次数
        print(data_buy_much[data_buy_much['behavior_type'] >= 2].count())  # 购买次数大于2的用户数 2184

    def top_10(self):
        # 销售频次前10的品类
        df_buy = self.df[self.df['behavior_type'] == 'buy']
        print(df_buy.groupby('item_category')['item_category'].count().sort_values(ascending=False)[:10])

    def buy_convert_rate(self):
        # 用户转换率漏斗
        num_pv = self.df[self.df['behavior_type'] == 'pv']['user_id'].count()
        num_collect = self.df[self.df['behavior_type'] == 'collect']['user_id'].count()
        num_cart = self.df[self.df['behavior_type'] == 'cart']['user_id'].count()
        num_buy = self.df[self.df['behavior_type'] == 'buy']['user_id'].count()

        # 由于收藏和加入购物车都属于在点击和购买前的一个阶段，这里合并
        num_far = num_collect + num_cart


obj = Demo()
# obj.explore()
obj.process()
obj.basic_analysis()
obj.top_10()