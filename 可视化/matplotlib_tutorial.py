#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/9/20 16:55
# Author: Hou hailun

# matplotlib examples

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class LineChart:
    # 线型图
    # 用来表示数据随着时间变化的趋势
    def draw(self):
        # 定义数据
        t = np.arange(0.0, 2.0, 0.01)
        s = np.sin(2.5 * np.pi * t)

        # 绘图
        plt.plot(t, s)

        # plt.xlabel('time(s)')      # x坐标轴
        # plt.ylabel('voltage(mV)')  # y坐标轴
        # plt.title('Sine Wave')     # 标题
        # plt.grid(True)             # 是否设置网格线
        plt.show()

        # plt.savefig('line_chart.png')

        # seaborn会折线图
        df = pd.DataFrame({'t': t, 's': s})
        sns.lineplot(x='t', y='s', data=df)
        plt.show()

    def multiple_draw_one_figure(self):
        # 在一张figure对象上绘制多个图, 只需要简单的调用plot()多次即可
        t = np.arange(0.0, 20.0, 1)
        s = np.arange(1, 21, 1)
        s2 = np.arange(4, 24, 1)
        plt.plot(t, s)
        plt.plot(t, s2)

        plt.xlabel('Item(s)')
        plt.ylabel('Values')
        plt.title('Python Line Chart')
        plt.grid(True)
        plt.show()

    def multiple_draw_figure(self):
        # 在多个figure对象上绘制
        t = np.arange(0.0, 20.0, 1)
        s = np.arange(1, 21, 1)
        s2 = np.arange(4, 24, 1)

        plt.subplot(2, 1, 1)  # 分为2行1列，使用编号1的figure
        plt.plot(t, s)
        plt.ylabel('Values')
        plt.title('First chart')
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(t, s2, color='red', linewidth=2.0, linestyle='--')  # 设置折线的颜色、宽度、style
        plt.xlabel('Item(s)')
        plt.ylabel('Values')
        plt.title('Second Chart')
        plt.grid(True)
        plt.show()


class HistChart:
    # 直方图，和柱状图相似，用来展现连续型数据分布特征的统计图形
    def draw(self):
        x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
        num_bins = 5
        # 参数说明 hist(x,bins=None,range=None, density=None, bottom=None, histtype='bar', align='mid',
        #   log=False, color=None, label=None, stacked=False, normed=None)
        # x: 数据集，直方图对数据集进行统计
        # bins: 统计的区间分布，指定bin(箱子)的个数,也就是总共有几条条状图
        # range: tuple, 显示的区间
        # histtype: 可选{'bar', 'barstacked', 'step', 'stepfilled'}之一，默认为bar，推荐使用默认配置，step使用的是梯状，stepfilled则会对梯状内部进行填充，效果与bar类似
        # align: 可选{'left', 'mid', 'right'}之一，默认为'mid'，控制柱状图的水平分布，left或者right，会有部分空白区域，推荐使用默认
        # log: bool, 默认False，即y坐标轴是否选择指数刻度
        # stackeL bool，默认False, 是否为推挤状图
        # alpha: 透明度
        # facecolor: 颜色
        n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
        plt.show()

        s = pd.Series(x)
        sns.distplot(s, kde=True)
        plt.show()

    def hist_draw(self):
        mu = 100
        sigma = 15
        x = mu + sigma * np.random.randn(10000)

        num_bins = 20
        n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=0.5)

        # add a best fit line
        y = plt.mlab.normpdf(bins, mu, sigma)
        plt.plot(bins, y, 'r--')
        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        plt.title('Histogram od IQ: $\mu=100$, $\sigma=15$')

        plt.subplots_adjust(left=0.15)
        plt.show()


class ScatterChart:
    # 散点图类
    # 把两个变量的值显示在二维坐标种，非常适合展示两个变量之间的关系
    def draw(self):
        N = 1000
        x = np.random.randn(N)
        y = np.random.randn(N)

        plt.scatter(x, y, marker='x')
        plt.show()

        # seaborn画图
        df = pd.DataFrame({'x': x, 'y': y})
        # 不仅绘制了散点图，还绘制了变量x，y的分布
        sns.jointplot(x='x', y='y', data=df, kind='scatter')
        plt.show()


class BarChart:
    # 条形图：可以查看类别的特征
    def draw(self):
        x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
        y = [5, 4, 8, 12, 7]

        plt.subplot(2, 1, 1)
        plt.bar(x, y)

        plt.subplot(2, 1, 2)
        sns.barplot(x, y)
        plt.show()


class BoxChart:
    # 箱型图：包括最大值，最小值，中位数，下四分位数，下四分位数，可以查看数据的差异性、离散程度和异常值
    def draw(self):
        data = np.random.normal(size=(10, 4))
        labels = ['A', 'B', 'C', 'D']

        plt.subplot(2, 1, 1)
        plt.boxplot(data, labels=labels)

        plt.subplot(2, 1, 2)
        df = pd.DataFrame(data, columns=labels)
        sns.boxplot(data=df)
        plt.show()


class PieChart:
    # 饼图：显示每个部分大小与总和之间的比例
    def draw(self):
        nums = [25, 37, 33, 37, 6]
        labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Others']

        plt.pie(x=nums, labels=labels)
        plt.show()


class HotChart:
    # 热力图：多元变量分析方法
    # flights = sns.load_dataset('flights')
    # data = flights.pivot('year', 'month', 'passengers')
    # print(data.head(10)) # 连接超时

    data = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]])

    sns.heatmap(data)
    plt.show()


if __name__ == "__main__":
    # 折线图
    # line_chart = LineChart()
    # line_chart.draw()
    # line_chart.multiple_draw_figure()

    # 直方图
    # hist_chart = HistChart()
    # hist_chart.draw()

    # 散点图
    # scatter_chart = ScatterChart()
    # scatter_chart.draw()

    # 条形图
    # bar_chart = BarChart()
    # bar_chart.draw()

    # 箱型图
    # box_chart = BoxChart()
    # box_chart.draw()

    # 饼图
    # pie_chart = PieChart()
    # pie_chart.draw()

    # 热力图
    # hot_chart = HotChart()
    # hot_chart.draw()

    # 蜘蛛图
