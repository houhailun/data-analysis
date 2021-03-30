#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/5/8 13:31
# Author: Hou hailun

# RFM,又称用户分析模型，价值分析模型
# R: Recency, 描述最近一次购买到现在间隔的天数
# F: Frequency, 描述每个客户购买频率
# M: Monetary， 描述每个客户的平均购买金额 或者 累加购买金额

import os
import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class RFMMode:
    def __init__(self):
        self.file_name = "PYTHON-RFM实战数据.xlsx"
        self.data_path = os.path.join(os.getcwd(), 'data')
        self.file_path = os.path.join(self.data_path, self.file_name)
        print(self.file_path)

    def load_data(self):
        df = pd.read_excel(self.file_path)
        return df

    def data_eda(self):
        # 数据概览
        df = self.load_data()
        print(df.head(5))  # 每条数据代表一次交易记录
        print(df.info())  # 28833行数据，城市有1条空数据
        print(df['订单状态'].unique())  # ['交易成功' '付款以后用户退款成功，交易自动关闭']

    def data_clean(self):
        # 数据清洗
        # 1、因为付款以后用户退款成功，交易自动关闭对分析没有意义，这里剔除
        df = self.load_data()
        df = df.loc[df['订单状态'] == "交易成功", :]
        print('剔除退款数据，剔除后还有:%d行' % len(df))

        # 2、筛选关心的列
        df = df[['买家昵称', '付款日期', '实付金额']]

        # 3、构造R,F,M
        # R: 最后一次下单时间到当前的天数
        df_r = df.groupby('买家昵称')['付款日期'].agg(max).reset_index()
        df_r['R'] = (pd.to_datetime('2019-7-1') - df_r['付款日期']).dt.days

        # F: 每个用户购买频次
        # 注意：把单个用户一天内多次下单行为看作整体一次，需要引入天的日期标签
        df['日期标签'] = df['付款日期'].astype(str).str[:10]
        # 单个用户一天内的订单合并
        df_f = df.groupby(['买家昵称', '日期标签'])['付款日期'].count().reset_index()
        # 对合并后的用户统计频次
        df_f = df_f.groupby('买家昵称')['付款日期'].count().reset_index()
        df_f.columns = ['买家昵称', 'F']
        # 实际上并没有把一天多次下单当作一次

        # M: 每个用户平均金额: 总金额 / 频次
        df_m = df.groupby('买家昵称')['实付金额'].sum().reset_index()
        df_m.columns = ['买家昵称', '总支付金额']
        df_fm = pd.merge(df_m, df_f, on='买家昵称')
        df_fm['M'] = df_fm['总支付金额'] / df_fm['F']

        # 合并RFM
        df_rfm = pd.merge(df_r, df_fm, on='买家昵称')
        df_rfm = df_rfm[['买家昵称', 'R', 'F', 'M']]
        print(df_rfm.head(5))
        return df_rfm

    def feature_score(self, df_rfm):
        # 维度打分
        # 以R值为例，R代表了用户有多少天没来下单，这个值越大，用户流失的可能性越大，我们当然不希望用户流失，所以R越大，分值越小。
        # F值代表了用户购买频次，M值则是用户平均支付金额，这两个指标是越大越好，即数值越大，得分越高。

        df_rfm['r_score'] = pd.cut(df_rfm['R'], bins=[0, 30, 60, 90, 120, float('inf')], labels=[5, 4, 3, 2, 1], right=False).astype(float)
        df_rfm['f_score'] = pd.cut(df_rfm['F'], bins=[1, 2, 3, 4, 5, float('inf')], labels=[1, 2, 3, 4, 5], right=False).astype(float)
        df_rfm['m_score'] = pd.cut(df_rfm['M'], bins=[0, 50, 100, 150, 200, float('inf')], labels=[1, 2, 3, 4, 5], right=False).astype(float)

        # 由于rfm可以组成125种分类，这里通过判断是否大于平均值划分为0/1，简化为8种分类
        df_rfm['R是否大于均值'] = (df_rfm['r_score'] > df_rfm['r_score'].mean()) * 1
        df_rfm['F是否大于均值'] = (df_rfm['f_score'] > df_rfm['r_score'].mean()) * 1
        df_rfm['M是否大于均值'] = (df_rfm['m_score'] > df_rfm['m_score'].mean()) * 1
        print(df_rfm.head(5))
        return df_rfm

    def make_layer(self, df_rfm):
        # 客户分层
        df_rfm['人群数值'] = df_rfm['R是否大于均值'].astype(str) + df_rfm['F是否大于均值'].astype(str) + df_rfm['M是否大于均值'].astype(str)

        def transform_label(x):
            label_map = {'111': '重要价值客户',
                         '110': '消费潜力客户',
                         '101': '频次深耕客户',
                         '100': '新客户',
                         '011': '重要价值流失预警客户',
                         '010': '一般客户',
                         '001': '高消费换回客户',
                         '000': '流失客户'}
            return label_map.get(x, None)

        df_rfm['人群类型'] = df_rfm['人群数值'].apply(transform_label)
        return df_rfm

    def rfm_mode(self, df_rfm):
        # RFM模型结果
        # 查看各分类用户占比情况
        df_count = df_rfm['人群类型'].value_counts().reset_index()
        df_count.columns = ['客户类型', '人数']
        df_count['人数占比'] = df_count['人数'] / df_count['人数'].sum()

        # 探究不同类型客户消费金额贡献占比
        df_rfm['购买总金额'] = df_rfm['F'] * df_rfm['M']
        df_mon = df_rfm.groupby('人群类型')['购买总金额'].sum().reset_index()
        df_mon.columns = ['客户类型', '消费金额']
        df_mon['消费金额占比'] = df_mon['消费金额'] / df_mon['消费金额'].sum()
        sns.lineplot(x='客户类型', y='消费金额占比', data=df_mon)


rfm = RFMMode()
rfm.data_eda()
df = rfm.data_clean()
df = rfm.feature_score(df)
df = rfm.make_layer(df)
df.to_csv('rfm.csv', index=False)
df = pd.read_csv('rfm.csv')
rfm.rfm_mode(df)