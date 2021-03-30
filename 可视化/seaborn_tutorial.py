#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/9/24 10:55
# Author: Hou hailun

# 数据可视化: seaborn 案例
# 图形分类：
#     因子变量绘图
#         箱线图boxplot，小提琴图violinplot, 散点图striplot, 带分布的赛典图swarmplot
#         直方图barplot, 计数的直方图countplot, 两变量关系图factorplot
#     数值变量绘图
#     两变量关系绘图
#     时间序列图: taplot
#     热力图: heatmap
#     分面绘图: FacetGrid
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class SeabornTutorial:
    def __init__(self):
        # sns.set_style("whitegrid")
        pass

    # 箱型图
    def draw_box(self):
        tips = sns.load_dataset('tips')
        # print(tips.head(5))
        # ax = sns.boxplot(y=tips["total_bill"])  # 竖着放的箱线图(上下)

        # 分组绘制箱型图，分组因子是day，在x轴不同位置绘制
        # ax = sns.boxplot(x='day', y='total_bill', data=tips)

        # 分组箱线图，分子因子是smoker，不同的因子用不同颜色区分
        # 相当于分组之后又分组
        # ax = sns.boxplot(x='day', y='total_bill', hue='smoker', data=tips, palette='Set3')

        # 对df的每个变量都绘制一个箱型图
        # ax = sns.boxplot(data=tips, orient='h', palette="Set2")

        # 箱线图+有分布趋势的散点图
        # 图形组合也就是两条绘图语句一起运行就可以了，相当于图形覆盖了
        ax = sns.boxplot(x='day', y='total_bill', data=tips)
        ax = sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")

        plt.show()

    # 直方图
    def draw_hist(self):
        data = pd.Series(np.random.randn(1000))  # 生成1000个点的符合正态分布的随机数
        # plt
        # plt.hist(data)  # 直方图，也可以通过plot(),修改里面kind参数实现
        # data.plot(kind='kde')  # 密度图

        # seaborn
        # 前两个默认就是True, rug是在最下方显示出频率情况，默认为False
        sns.distplot(a=data, bins=20, hist=True, kde=True, rug=True)
        sns.kdeplot(data, shade=True, color='r')  # shade表示线下颜色为阴影,color表示颜色是红色
        sns.rugplot(data)  # 在下方画出频率情况
        plt.show()

    # 柱状图
    def draw_bar(self):
        df = sns.load_dataset('flights')
        print(df.head(5))


if __name__ == "__main__":
    sns_obj = SeabornTutorial()
    # sns_obj.draw_box()
    # sns_obj.draw_hist()
    sns_obj.draw_bar()