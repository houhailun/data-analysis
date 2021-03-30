#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/4/13 10:18
# Author: Hou hailun

import matplotlib.pyplot as plt


class PyechartDemo:
    def __init__(self):
        self.columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
        self.data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

    def bar_demo(self):
        from pyecharts import Bar
        # 柱状图
        # 设置柱状图的主标题与副标题
        bar = Bar(title="柱状图", subtitle="一年的降水量与蒸发量")
        # 添加柱状图的数据及配置项
        # maxk
        bar.add("降水量", self.columns, self.data1, mark_line=["average"], mark_point=["max", "min"])
        bar.add("蒸发量", self.columns, self.data2, mark_line=["average"], mark_point=["max", "min"])
        # 生成本地文件（默认为.html文件）
        bar.render('bar.html')
        plt.show()

    def pie_demo(self):
        from pyecharts import Pie
        # 饼图
        # 设置主标题与副标题，标题设置居中，设置宽度为900
        pie = Pie(title="饼状图", subtitle="一年的降水量于蒸发量", title_pos='center', width=900)
        # 加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示
        pie.add("降水量", self.columns, self.data1, center=[25, 50], is_legend_show=False)
        # 加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签
        pie.add("蒸发量", self.columns, self.data2, center=[75, 50], is_legend_show=False, is_label_show=True)
        pie.render('pie.html')
        plt.show()

    def boxplot_demo(self):
        # 箱体图
        from pyecharts import Boxplot
        boxplot = Boxplot("箱型图", "一年的降水量与蒸发量")
        x_axis = ['降水量', '蒸发量']
        y_axis = [self.data1, self.data2]
        # prepare_data方法可以将数据转为嵌套的[min, Q1, median( or Q2), Q3, max]
        y_axis = boxplot.prepare_data(y_axis)
        boxplot.add("天气统计", x_axis, y_axis)
        boxplot.render('boxplot.html')

    def line_demo(self):
        # 折线图
        from pyecharts import Line
        line = Line(title='折线图', subtitle='一年的降水量与蒸发量')
        line.add("降水量", self.columns, self.data1, is_label_show=True, mark_line=["average"])
        line.add("蒸发量", self.columns, self.data2, is_label_show=True, mark_line=["average"])
        line.render('line.html')

    def radar_demo(self):
        # 雷达图
        from pyecharts import Radar
        radar = Radar('雷达图', subtitle='一年的降水量与蒸发量')
        # 由于雷达图传入的数据得为多维数据，所以这里需要做一下处理
        radar_data1 = [[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]]
        radar_data2 = [[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]]
        # 设置column的最大值，为了雷达图更为直观，这里的月份最大值设置有所不同
        schema = [
            ("Jan", 5), ("Feb", 10), ("Mar", 10),
            ("Apr", 50), ("May", 50), ("Jun", 200),
            ("Jul", 200), ("Aug", 200), ("Sep", 50),
            ("Oct", 50), ("Nov", 10), ("Dec", 5)
        ]
        # 传入坐标
        radar.config(schema)
        radar.add("降水量", radar_data1)
        # 一般默认为同一种颜色，这里为了便于区分，需要设置item的颜色
        radar.add("蒸发量", radar_data2, item_color="#1C86EE")
        radar.render('radar.html')

    def scatter_demo(self):
        # 散点图
        from pyecharts import Scatter
        scatter = Scatter('散点图', '一年的降水量与蒸发量')
        # xais_name是设置横坐标名称，这里由于显示问题，还需要将y轴名称与y轴的距离进行设置
        scatter.add("降水量与蒸发量的散点分布",
                    self.data1, self.data2,
                    xaxis_name="降水量",
                    yaxis_name="蒸发量",
                    yaxis_name_gap=40)
        scatter.render('sactter.html')


obj = PyechartDemo()
# obj.bar_demo()
# obj.pie_demo()
# obj.boxplot_demo()
# obj.line_demo()
# obj.radar_demo()
# obj.scatter_demo()