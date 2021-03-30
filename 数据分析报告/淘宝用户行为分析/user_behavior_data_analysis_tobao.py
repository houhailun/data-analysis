#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/9/18 13:24
# Author: Hou hailun

# 淘宝用户行为分析
# 数据集包含了2017年11月25日至2017年12月3日之间，有行为的约一百万随机用户的所有行为（行为包括点击、购买、加购、喜欢）。
# 数据主要包括5个字段，用户ID，商品ID，商品类目ID，行为类型，时间戳。一共有100,150,807条记录。
# column	description
# user_id	用户身份，脱敏
# item_id	商品id，脱敏
# behavior_type	用户行为类型（包括点击，收藏，加购物车和付款四种行为，相应的值分别为1,2,3和4）
# user_geohash	地理位置
# item_category	品类ID（商品所属的品类）
# time	用户行为发生的时间

# 提出问题（目标）
# 1、基础数据统计
# 总PV、总UV、有购买行为的用户数量、复购率、跳失率

# 2、用户行为转化漏斗
# 点击 - -收藏 - -加购物车 - -支付各环节转化率如何？

# 3、购买次数占前80 % 的品类有多少？

# 4、从时间维度了解用户的行为习惯：每天的PV、UV

# 结论：
# 1、大部分用户的主要活跃时间段为9：00-22：00，其中18：00-22：00开始逐渐增加，达到一天之中的顶峰。每周的主要活跃时间为周二至周四，运营人员可根据活跃时间进行相关的活动。
# 2、收藏或者加购物车的概率在5%左右，而最后真正的购买率在1%，购买转化率与行业的标准进行比较，后面可以采取活动（用户细分，转化路径细查）提高购买转化率。
# 3、针对不同品类的购买转化率采取不同的策略，提高已购品类的转化率，一方面，对未被购买的品类进行分析，找出原因，促成购买。

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Funnel  # 新版本1V，Funnel放到了charts中


class UserBehaviorAnalysis:
    # 用户行为分析数据类
    def __init__(self):
        self.file_path = "tianchi_mobile_recommend_train_user.csv"
        self.data = pd.read_csv(self.file_path, nrows=1000000)  # 文件太大，限制读取100W条

    def load_data(self):
        # 为便于分析，把time列切分为2个列: 年月日、小时
        self.data['time'] = pd.to_datetime(self.data['time'])

        self.data['hour'] = self.data['time'].dt.hour         # 小时
        self.data['time'] = self.data['time'].dt.normalize()  # 只获取年月日

        # 根据行为取值赋予不同含义
        self.data.ix[self.data['behavior_type'] == 1, 'behavior_type'] = 'pv'
        self.data.ix[self.data['behavior_type'] == 2, 'behavior_type'] = 'collect'
        self.data.ix[self.data['behavior_type'] == 3, 'behavior_type'] = 'cart'
        self.data.ix[self.data['behavior_type'] == 4, 'behavior_type'] = 'buy'

    # 数据探索
    def data_explore(self):
        print(' df.info '.center(40, '*'))
        print(self.data.info())  # time列为object类型，转换为datetime类型

        print(' 查看是否有NULL '.center(40, '*'))
        print(self.data.isnull().any())

        print(' 查看数据分布 '.center(40, '*'))
        print(self.data.describe())

    def basic_analysis(self):
        # 基础数据统计: PV，UV

        # PV：Page View, 即页面浏览量或点击量，用户每次刷新即被计算一次
        data_pv = self.data[self.data['behavior_type'] == 'pv']
        print(data_pv.shape[0])  # 可以看到PV为 942230

        # UV：unique Visitor, 访问网站的一台电脑客户端为一个访客。00:00-24:00内相同的客户端只被计算一次。
        print(self.data.drop_duplicates('user_id')['user_id'].count())  # 去重统计用户数 8058

        # 有购买行为的用户数
        data_buy = self.data[self.data['behavior_type'] == 'buy']
        print(data_buy.drop_duplicates('user_id')['user_id'].count())  # 购买人数 4120

        # 复购率 = 购买2次或以上的用户 / 购买用户总数
        data_buy = self.data[self.data['behavior_type'] == 'buy']  # 发生购买行为的数据
        print(data_buy.drop_duplicates('user_id').count())

        data_buy_much = data_buy.groupby(['user_id']).count()      # 每个用户购买的次数
        print(data_buy_much[data_buy_much['behavior_type'] >= 2].count())  # 复购的用户数 2184

    def period_user_behavior(self):
        # 从时间维度了解用户的行为习惯
        # 每周的用户行为数量变化趋势
        def user_cnt_trend_week():
            self.data['week'] = [i.weekday() for i in self.data['time']]
            df = self.data.groupby(['week']).count()  # 每周X的个数
            df.index = [1, 2, 3, 4, 5, 6, 7]

            print(df)
            df['user_id'].plot()
            # ax = fig.add_subplot(111)
            # ax.plot(df.index, df.user_id)
            # 观察到周一到周二的用户行为逐渐增加，周二-周四达到一个稳定值，周四到-周六用户行为明显减少，
            # 周六为一周最低，周六后开始逐渐增加。

            plt.show()

        # user_cnt_trend_week()

        # 每日PV量
        def page_view_day():
            day_pv = self.data[self.data['behavior_type'] == 'pv']
            day_pv = day_pv.groupby(['time']).count()
            print(day_pv.head(10))

            fig = plt.figure(figsize=(20, 6))
            ax = fig.add_subplot(111)
            plt.rcParams['axes.unicode_minus'] = False
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
            plt.title(u'每日PV')
            ax.plot(day_pv.index, day_pv.user_id)
            plt.show()
            # 总结：用户总数变化趋势与PV量变化趋势类似，周末的数量逐渐增加，到工作日又逐渐降低。在双十二期间，用户总数明显上升，活动过后，人数明显下降至平稳状态。

        # page_view_day()

        # 一天不同时间点，用户行为的数量
        def user_cnt_hour():
            self.data['day'] = self.data['time'].dt.day

            # 不同小时的用户数量
            df = self.data.groupby(['hour']).count()

            fig = plt.figure(figsize=(20, 6))
            ax = fig.add_subplot(111)
            ax.plot(df.index, df.user_id)
            plt.rcParams['axes.unicode_minus'] = False
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
            plt.title(u'不同时段的用户行为数量')
            plt.xticks(np.arange(24))
            plt.show()
            # 结论：可以看到，从22：00点 - 凌晨5点，用户数量逐渐降低，降为一天之中最低，因为此段时间大多数人处于休息之中。
            # 从早上6点开始，用户行为数量逐渐增多，直至上午10点。
            # 10点 - 18：00用户行为数量一直保持一个平稳的状态，因为此段时间，大部分人在工作或者处理事情，用户行为数量很稳定。
            # 而18：00过后，很多人已经下班，有闲暇时间，用户行为数量逐渐增加，直至一天之中的最高值。如果运营人员采取活动，可以参考用户比较活跃的时间段

        user_cnt_hour()

    # 购买转化率: 用户行为转化漏斗
    def buy_convert_rate(self):
        # 浏览、收藏、加入购物车、购买的用户数
        pv_num = self.data[self.data['behavior_type'] == 'pv']['user_id'].count()
        collect_num = self.data[self.data['behavior_type'] == 'collect']['user_id'].count()
        cart_num = self.data[self.data['behavior_type'] == 'cart']['user_id'].count()
        buy_num = self.data[self.data['behavior_type'] == 'buy']['user_id'].count()

        # 由于收藏和加入购物车都为浏览和购买阶段之间确定购买意向的用户行为，且不分先后顺序，因此将其算作一个阶段
        far_num = collect_num + cart_num

        trend_map = {'环节': ['pv', 'far', 'buy'],
                     '人数': [pv_num, far_num, buy_num]}
        frame = pd.DataFrame(trend_map)

        # 计算单环节转化率
        tmp1 = np.array(frame['人数'][1:])
        tmp2 = np.array(frame['人数'][0:-1])
        single_convs = list(tmp1 / tmp2)
        single_convs.insert(0, 1)  # 在开始处插入1，因为pv阶段是没有转化率的
        single_convs = [round(x, 4) for x in single_convs]
        frame['单一环节转化率'] = single_convs

        # 绘制漏斗图
        attrs = frame['环节'].tolist()
        attr_values = (np.array(frame['单一环节转化率'] * 100).tolist())

        funnel = Funnel("单一环节转化漏斗图", width=400, height=200, title_pos='center')
        funnel.add(name="商品交易行环节",  # 指定图例名称
                    attr=attrs,  # 指定属性名称
                    value=attr_values,  # 指定属性所对应的值
                    is_label_show=True,  # 指定标签是否显示
                    label_formatter='{c}%',  # 指定标签显示的格式
                    label_pos="inside",  # 指定标签的位置
                    legend_orient='vertical',  # 指定图例的方向
                    legend_pos='left',  # 指定图例的位置
                    is_legend_show=True)  # 指定图例是否显示

        funnel.render('render.html')  # 生成html文件

        # 总体转化率
        tmp3 = np.array(frame['人数'])
        tmp4 = np.ones(len(frame['人数'])) * frame['人数'][0]  # [942230. 942230. 942230.]
        total_convs = list(tmp3 / tmp4)
        total_convs = [round(x, 4) for x in total_convs]
        frame['总体转化率'] = total_convs

        # 绘制漏斗图
        attrs = frame['环节'].tolist()
        attr_values = (np.array(frame['总体转化率'] * 100).tolist())

        funnel1 = Funnel("总体转化漏斗图", width=400, height=200, title_pos='center')
        funnel1.add(name="商品交易行环节",  # 指定图例名称
                    attr=attrs,  # 指定属性名称
                    value=attr_values,  # 指定属性所对应的值
                    is_label_show=True,  # 指定标签是否显示
                    label_formatter='{c}%',  # 指定标签显示的格式
                    label_pos="inside",  # 指定标签的位置
                    legend_orient='vertical',  # 指定图例的方向
                    legend_pos='left',  # 指定图例的位置
                    is_legend_show=True)  # 指定图例是否显示

        funnel1.render('render1.html')  # 生成html文件

    # 销售次数前10的品类
    def sale_cnt_top_ten(self):
        df = self.data[self.data['behavior_type'] == 'buy']
        print(df.groupby('item_category')['item_category'].count().sort_values(ascending=False))
        # .sort_values(ascending=False))
        # 结论：购买次数最多的品类是6344，购买次数为165.


if __name__ == "__main__":

    obj = UserBehaviorAnalysis()
    obj.load_data()
    obj.data_explore()
    obj.basic_analysis()
    obj.period_user_behavior()
    obj.sale_cnt_top_ten()
    obj.buy_convert_rate()