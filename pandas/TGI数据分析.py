#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/5/8 10:53
# Author: Hou hailun

# TGI：Target group index  目标用户指数
# TGI=[目标群体中具有某一特征的群体所占比例/总体中具有相同特征的群体所占比例]*标准数100

# 项目背景
# BOSS抛来一份订单明细，“小Z啊，我们最近要推出一款客单比较高的产品，打算在一些城市先试销，你看看这个数据，哪些城市的人有高客单偏好，帮我筛选5个吧”

import os
import sys
import numpy as np
import pandas as pd

data_path = os.path.abspath(os.path.join(os.getcwd(), "data"))
print(pd.__version__)


def tgi_main():
    file_path = os.path.join(data_path, 'TGI指数案例数据.xlsx')
    df = pd.read_excel(file_path)
    # df.info()
    # print(df.head())

    # 客单价：单次购买大于50元就算高客单的客户了
    # 明确需求：计算每个城市高客单价人数所占比例 / 所有城市总客户高客单价人数所占比例

    # step1：单个用户打标
    # 判断用户是否属于客单价的人群
    gp_user = df.groupby('买家昵称')['实付金额'].mean().reset_index()
    gp_user['客单类别'] = gp_user['实付金额'].apply(lambda x: "高客单" if x > 50 else "低客单")

    # step2：匹配城市
    df_dup = df.drop_duplicates(subset=['买家昵称'])  # 按买家昵称去重
    df_merge = pd.merge(gp_user, df_dup, on='买家昵称', how='left')

    # step3:高客价TGI指数计算
    df_merge = df_merge[['买家昵称', '客单类别', '省份', '城市']]
    result = pd.pivot_table(df_merge, index=['省份', '城市'], columns='客单类别', aggfunc='count')

    tgi = pd.merge(result['买家昵称']['高客单'].reset_index(),
                   result['买家昵称']['低客单'].reset_index(),
                   on=['省份', '城市'], how='inner')
    tgi['总人数'] = tgi['高客单'] + tgi['低客单']
    tgi['高客单占比'] = tgi['高客单'] / tgi['总人数']
    tgi = tgi.dropna()

    # step4: 统计总人数中，高客单人群的比例
    total_precentage = tgi['高客单'].sum() / tgi['总人数'].sum()

    tgi['高客单TGI指数'] = tgi['高客单占比'] / total_precentage * 100
    tgi = tgi.sort_values('高客单TGI指数', ascending=False)
    # 问题：高客单TGI指数排名靠前的城市，总客户数几乎不超过10人
    # TGI指数能够显示偏好的强弱，但很容易让人忽略具体的样本量大小

    # 选择总人数大于平均值的人数
    tgi = tgi.loc[tgi['总人数'] > tgi['总人数'].mean(), :]
    print(tgi.head(10))


if __name__ == "__main__":
    tgi_main()

