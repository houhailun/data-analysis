#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/8/20 11:30
# Author: Hou hailun

"""
北极星度量指标:
    1. 是单一指标，最能体现产品为客户提供的核心价值
    2. 指标取决于您公司的产品，职位，目标等
本示例，使用在线零售的样本数据集，选择“月收入”
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# tx_data = pd.read_csv("OnlineRetail.csv", encoding='ISO-8859-1')
# print(tx_data.shape)
# #
# # InvoiceNo   | 订单号
# # StockCode   |
# # Description | 描述
# # Quantity    | 数量
# # InvoiceDate | 发票日期
# # UnitPrice   | 单价
# # CustomerID  | 顾客ID
# # Country     | 国家
#
# # 收入 = 有效客户数量 * 订单数量 * 订单的平均收入
#
# # 转换为时间类型
# tx_data['InvoiceDate'] = pd.to_datetime(tx_data['InvoiceDate'])
#
# # 月份
# tx_data['InvoiceYearMonth'] = tx_data['InvoiceDate'].map(lambda date: 100*date.year+date.month)
#
# # 统计收入，并进行聚合
# tx_data['Revenue'] = tx_data['UnitPrice'] * tx_data['Quantity']
# tx_data.to_csv('onlineRetailRevenue.csv')

tx_data = pd.read_csv("onlineRetailRevenue.csv")

# tx_revenue = tx_data.groupby(['InvoiceYearMonth'])['Revenue'].sum().reset_index()
# tx_revenue.to_csv('onlineSaleRevenue.csv')
#
# # 可视化
# data_type = {"InvoiceYearMonth": np.str, "Revenue": np.float}  # 指定类型
# tx_revenue = pd.read_csv("onlineSaleRevenue.csv", dtype=data_type)
# # sns.lineplot(x='InvoiceYearMonth', y='Revenue', data=tx_revenue)
# # plt.title("Monthly Revenue")
# # 可以看到月收入是从11年8月开始增长，12月份数据不完整；接下来查看月收入增长率
#
# # using pct_change() function to see monthly percentage change
# # DataFrame.pct_change(periods=1, fill_method=‘pad’, limit=None, freq=None, **kwargs)
# # 表示当前元素与先前元素的相差百分比，当然指定periods=n,表示当前元素与先前n个元素的相差百分比。
# tx_revenue['MonthlyGrowth'] = tx_revenue['Revenue'].pct_change()
# print(tx_revenue.head())
#
# sns.lineplot(x='InvoiceYearMonth', y='MonthlyGrowth', data=tx_revenue.query("InvoiceYearMonth < '201112'"))
# 可以看到较上个月增长36.5%, 但是201104反而负增长，分析why
# 是由于活跃客户减小 还是 订单减少 还是 购买过多便宜的商品？

# 每月活跃客户
# 只关注英国数据(记录最多)
tx_uk = tx_data.query("Country == 'United Kingdom'").reset_index(drop=True)


# 月活跃用户
def eda_active():
    tx_monthly_active = tx_uk.groupby('InvoiceYearMonth')['CustomerID'].nunique().reset_index()
    print(tx_monthly_active.head())

    sns.barplot(x='InvoiceYearMonth', y='CustomerID', data=tx_monthly_active)
    # 4月，每月有效客户数量从923降至817(-11.5%)
# eda_active()


# 每月订单数
def eda_orders():
    tx_monthly_sales = tx_uk.groupby('InvoiceYearMonth')['Quantity'].sum().reset_index()
    print(tx_monthly_sales.head())

    sns.barplot(x='InvoiceYearMonth', y='Quantity', data=tx_monthly_sales)
    # 4月的订单数也有所下降（从27.9万降至25.7万，-8％） 我们知道有效客户数直接影响了订单数的减少
# eda_orders()


# 每笔订单的平均收入
def eda_unit_price():
    tx_monthly_avg = tx_uk.groupby('InvoiceYearMonth')['Revenue'].mean().reset_index()
    print(tx_monthly_avg.head())

    sns.barplot(x='InvoiceYearMonth', y='Revenue', data=tx_monthly_avg)
    # 4月份的订单平均收入也有所下降（从16.7降至15.8）
# eda_unit_price()


# 新客户比率, 表示是在失去现有客户还是无法吸引新客户
# 新客户定义: 在特点时间内首次购买商品的人
tx_uk['InvoiceDate'] = pd.to_datetime(tx_uk['InvoiceDate'])
tx_min_purchase = tx_uk.groupby('CustomerID').InvoiceDate.min().reset_index()  # 找客户首次购买日期
tx_min_purchase.columns = ['CustomerID', 'MinPurchaseDate']
tx_min_purchase['MinPurchaseYearMonth'] = tx_min_purchase['MinPurchaseDate'].map(lambda date: 100*date.year + date.month)

tx_uk = pd.merge(tx_uk, tx_min_purchase, on='CustomerID')
# 针对月份大于首次购买的月份的数据，打标为老用户，其余为新用户
tx_uk['UserType'] = 'New'
tx_uk.loc[tx_uk['InvoiceYearMonth'] > tx_uk['MinPurchaseYearMonth'], 'UserType'] = 'Exist'

# 每个月不同用户类型下的收入和
tx_user_type_revenue = tx_uk.groupby(['InvoiceYearMonth', 'UserType'])['Revenue'].sum().reset_index()
tx_user_type_revenue = tx_user_type_revenue.query("InvoiceYearMonth != 201012 and InvoiceYearMonth != 201112")

sns.lineplot(x='InvoiceYearMonth', y='Revenue', data=tx_user_type_revenue)
# 现有客户显示出积极的趋势，并告诉我们我们的客户群正在增长，但是新客户则有轻微的消极趋势。

# 查看新客户比率
tx_user_ratio = tx_uk.query("UserType == 'New'").groupby(['InvoiceYearMonth'])['CustomerID'].nunique()/tx_uk.query("UserType == 'Existing'").groupby(['InvoiceYearMonth'])['CustomerID'].nunique()
tx_user_ratio = tx_user_ratio.reset_index()
tx_user_ratio = tx_user_ratio.dropna()

plt.show()
