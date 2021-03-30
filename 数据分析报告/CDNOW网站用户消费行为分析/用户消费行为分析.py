#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/5/22 10:46
# Author: Hou hailun

# 用户ID，购买日期，购买数量，购买金额
# 趋势分析：每月销售金额，每周销量量，每周销售次数，每周消费用户数
# 用户分析：
#   用户个体消费能力：消费金额，消费次数
#   用户消费行为分析：用户第一次消费，最后一次消费，新老客占比，用户分层（RFM 或 新/老/活跃/流失），用户购买周期，生命周期


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyecharts
plt.style.use('ggplot')                       # 更改设计风格
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来显示中文标签


class UserOrderAnalysis:
    def __init__(self):
        self.data = pd.read_csv('data.csv', names=['user_id', 'order_dt', 'order_products', 'order_amount'], sep='\s+')

    def eda(self):
        # 数据eda
        print(self.data.info())  # 不存在空值
        print(self.data.describe())
        # order_products列：用户平均每笔订单购买2.4个商品，标准差在2.3，故有一定的波动性。中位数在2个商品，75分位数在3个商品，
        # 说明绝大部分订单的购买量都不多。最大值为99，受极值影响

        self.data['order_products'].plot.hist(bins=200)
        self.data['order_amount'].plot.hist(bins=200)
        plt.show()

    def process(self):
        # 为了便于处理，把order_dt转换datetime类型, 增加week，month列便于分析
        self.data['order_dt'] = pd.to_datetime(self.data['order_dt'], format='%Y%m%d')
        self.data['month'] = self.data['order_dt'].values.astype('datetime64[M]')

    def order_trend_analysis(self):
        # 消费趋势分析，按每个月分析
        grouped_month = self.data.groupby('month')

        _, axes = plt.subplots(nrows=2, ncols=2, figsize=(22, 10), sharex=True)
        print(' 每个月的消费金额总和 '.center(40, '*'))
        grouped_month['order_amount'].sum().plot(ax=axes[0, 0], title='每个月的消费金额总和')

        # 本次数据时间跨度为18个月（199701 - 199806），消费金额总体描述分析如下：由上图可知，消费金额在前三个月
        # {1997 - 01 - 01: 299060.17, 1997 - 02 - 01: 379590.03, 1997 - 03 - 01: 393155.27}
        # 增长至峰值，在3-4月出现断崖式下滑，后续消费金额较为平稳，但有轻微下降趋势。原因分析如下：
        # 前3个月的增长，推测是由于CD网站的促销活动；
        # 而3 - 4月的异常下跌，推测是受促销活动结束的影响较大。同时由于暂缺乏详细数据，所以未对3 - 4月的异常收入下滑进行实际细剖与分析。
        # 收入异常下跌的其他原因整理如下：比如：
        # （1）【竞争对手】方面，近期是否出现其他竞争与替代产品；
        # （2）【渠道】方面，可从用户数量、渠道收入（环比、下滑）两个维度来评判渠道质量，可从查看不同渠道的等数据指标。不同渠道如web端直接访问、搜索引擎渠道、第三方合作渠道等，进一步定位是否是渠道推广有问题；
        # （3）【用户来源】方面，从新老客构成、流失客户的特征、聚类与分类等角度；
        # （4）【CD产品体验】方面，针对客户的评价、网站评论及主动与用户沟通收集反馈意见问题，对产品体验进行分析，如是包装不流行、价格没优惠了等等进行优化。
        # （5）【用户体验流程】方面，通过埋点数据查看流失客户在网站上的行为数据：启动次数、停留时长、流程不畅（如流失客户大部分在支付环节未完成支付，那么就需要回访部分客户、进行优化改进）；

        print(' 每月消费订单数 '.center(40, '*'))
        grouped_month['user_id'].count().plot(ax=axes[0, 1], title='每月消费订单数')
        # 前三个月消费订单数在10000笔左右，后续月份的平均则在2500笔。

        print(' 每月产品购买数 '.center(40, '*'))
        grouped_month['order_products'].sum().plot(ax=axes[1, 0], title='每月产品购买数')
        # 前三个月产品购买数在20000以上，后续月份的产品购买量在6000~8000左右

        print(' 每月消费人数 '.center(40, '*'))
        grouped_month['user_id'].apply(lambda x: len(x.unique())).plot(ax=axes[1, 1], title='每月消费人数')
        plt.show()
        # 前三个月每月的消费人数在8000 - 10000之间，后续月份平均消费人数在2000人不到

        print(' 数据透视表分析 ')
        pivot_df = self.data.pivot_table(index='month',
                                         values=['order_amount', 'user_id', 'order_products'],
                                         aggfunc={'order_amount': 'sum', 'user_id': 'count', 'order_products': 'sum'})
        pivot_df.plot()
        plt.show()
        # 趋势分析：总体来看，消费总金额、消费次数、产品购买量、消费人数的趋势想似：均先上升、下跌、趋于平稳并下降。
        # 可以看出网站的流失用户在增加，采用开源（拉新）节流（留存）的运营方式，来增加销售收入。

    def user_purchase_ability_analysis(self):
        # 用户购买力分析
        # 上一部分是按月分析，主要看趋势；本部分按用户个体分析，来看消费能力
        _, axes = plt.subplots(nrows=2, ncols=2, figsize=(22, 10), sharex=True)

        # 用户消费金额、消费数量的描述统计
        grouped_user = self.data.groupby('user_id')
        print(' 用户消费金额 '.center(40, '*'))
        print(grouped_user.sum().describe())
        # 【order_products数量】用户平均购买了7张CD，但中位数只有3，说明小部分用户购买了大量的CD
        # 【order_amount金额】用户平均消费106元，中位数为43，判断同上，有极值干扰
        # 消费、金融和钱相关的数据，基本上都符合二八法则，小部分的用户占了消费的大头

        grouped_user.sum().plot.scatter(x="order_amount", y="order_products", ax=axes[0, 0], title='用户消费金额和消费数量')

        print(' 用户消费金额分布图 '.center(40, '*'))
        grouped_user['order_amount'].sum().plot.hist(bins=200, ax=axes[0, 1], title='用户消费金额分布图')
        # 从直方图可知，用户消费金额，绝大部分呈现集中趋势
        # 部分异常值干扰了判断。可以使用【切比雪夫定理】过滤异常值，计算95%(mean ± 5std)的数据的分布情况

        print(' 用户累计消费金额占比 '.center(40, '*'))
        user_cumsum = grouped_user.sum().sort_values('order_amount', ascending=False).apply(lambda x: x.cumsum() / x.sum())
        user_cumsum.reset_index().order_amount.plot(ax=axes[1, 0], title='用户累计消费金额占比')  # reset_index()去掉索引 ,才能作图
        # 按用户消费金额进行降序排列，由图可知，共计约25000个用户：
        # 20%（约5000）的客户贡献了70% 的消费额度，近似符合二八定律。
        # 50%的客户贡献了90% 的消费额度（即剩余50%的客户仅贡献10% 的消费额度）。
        # 启发，只要维护好这5000个用户（占比20%）就可以把业绩KPI完成70%，如果能把5000个用户运营的更好就可以占比更高
        plt.show()

    def user_purchase_behavior_analysis(self):
        # 用户消费行为分析
        # 通过以上基本数据描述分析可以清楚该网站整体的消费趋势和用户消费能力，现在进一步挖掘用户消费行为数据，通过RFM模型、生命周期等方法对用户进行分层，为后续运营管理提供依据。
        print(' 用户第一次消费 '.center(40, '*'))
        _, axes = plt.subplots(nrows=2, ncols=2, figsize=(22, 10), sharex=True)
        grouped_user = self.data.groupby('user_id')
        grouped_user.min().order_dt.value_counts().plot(ax=axes[0, 0], title='用户第一次消费')  # 时间对应的首购人数
        # 用户第一次购买分布，集中在前三个月(1997年1-3月)；其中，在2月11日至2月25日有一次剧烈波动

        print(' 用户最后一次消费 '.center(40, '*'))
        grouped_user.max().order_dt.value_counts().plot(ax=axes[0, 1], title='用户最后一次消费')
        # 用户最后一次购买分布（1997年1月-1998年6月）比第一次分布（1997年1-3月）广；
        # 大部分最后一次购买，集中在前三个月，说明很多用户购买了一次后就不再进行购买。
        # 随着时间的增长，用户最后一次购买数略微增加

        print(' 新老客消费比 '.center(40, '*'))
        print(' 多少用户仅消费了1次 '.center(40, '*'))
        user_life = grouped_user.order_dt.agg(['min', 'max'])
        print((user_life['min'] == user_life['max']).value_counts())
        # True     12054
        # False    11516
        # 有一半用户就消费了一次，可以通过定期发送邮件、信息等方式进行用户唤回

        print(' 每月新客户占比 '.center(40, '*'))
        # 按month分组下的userid分组，求每月每个用户的最早购买日期和最晚消费日期
        grouped_um = self.data.groupby(['month', 'user_id']).order_dt.agg(['min', 'max']).reset_index()
        grouped_um['new'] = grouped_um['min'] == grouped_um['max']
        grouped_um1 = grouped_um.groupby('month')
        grouped_um2 = grouped_um1['new'].apply(lambda x: x.value_counts() / x.count()).reset_index()
        grouped_um2[grouped_um2['level_1']].plot(y='new', x="month", ax=axes[1, 0], title='每月新客户占比')
        # 由图可知，1997年1-4月新用户数量由90%跌落至80%以下；之后几个月的新用户量保持在80~82%区间。
        plt.show()

    def rfm_model(self):
        # 用户分层RFM
        # R: Recency, 最近购买
        # F: frequency, 消费频率
        # M: Monetary, 消费金额
        rfm = self.data.pivot_table(index='user_id',
                                    values=['order_products', 'order_amount', 'order_dt'],
                                    aggfunc={'order_dt': 'max', 'order_amount': 'sum', 'order_products': 'sum'})
        rfm['R'] = -(rfm['order_dt'] - rfm['order_dt'].max()) / np.timedelta64(1, 'D')
        rfm.rename(columns={'order_products': 'F', 'order_amount': 'M'}, inplace=True)

        def rfm_func(x):
            print(x)
            level = x.apply(lambda x: '1' if x >= 0 else '0')
            label = level.R + level.F + level.M
            d = {
                '111': '重要价值客户',
                '011': '重要保持客户',
                '101': '重要挽留客户',
                '001': '重要发展客户',
                '110': '一般价值客户',
                '010': '一般保持客户',
                '100': '一般挽留客户',
                '000': '一般发展客户'
            }
            result = d[label]
            return result

        rfm['label'] = rfm[['R', 'F', 'M']].apply(lambda x: x - x.mean()).apply(rfm_func, axis=1)
        # axis = 1是逐行应用  #默认axis=0，即表示apply函数逐列应用。

        # 根据RFM分层模型对所有用户分层
        rfm_sum = rfm.groupby('label').agg({'R': 'count', 'F': 'sum', 'M': 'sum'})

        plt.figure(figsize=(6, 6))
        patches, l_text, p_text = plt.pie(rfm_sum['R'],
                                          labels=rfm_sum.index,
                                          explode=(0, 0, 0, 0.1, 0, 0, 0, 0),
                                          colors=plt.cm.rainbow(np.arange(len(rfm_sum['R'])) / len(rfm_sum['R'])),
                                          labeldistance=1.1,
                                          autopct='%3.1f%%',
                                          shadow=False,
                                          textprops={'fontsize': 12},
                                          startangle=0,
                                          pctdistance=0.9)
        for t in l_text:
            t.set_size = 30
        for t in p_text:
            t.set_size = 20
        plt.title('RFM分层用户数占比', fontsize=20)
        plt.axis('equal')
        plt.legend(bbox_to_anchor=(1.6, 0.7))
        plt.show()

    def user_status_analysis(self):
        # 用户行为分析
        # 利用数据透视表，以user_id为横坐标，month为纵坐标，统计用户每月的消费次数
        pivoted_counts = pd.pivot_table(self.data, index='user_id', columns='month', values='order_dt', aggfunc='count').fillna(0)

        # 统计每月的用户状态，1为消费，0为未消费
        df_purchase = pivoted_counts.applymap(lambda x: 1 if x > 0 else 0)  # applymap()逐个元素判断

        # 将用户状态分为unreg（未注册）、new（新客）、active（活跃用户）、return（回流用户）和 unactive（不活跃用户）
        def active_status(data):
            status = []
            x = len(data)
            for i in range(x):
                if data[i] == 0:  # 若本月未消费
                    if len(status) == 0:  # 首月，用户状态设置为未注册
                        status.append('unreg')
                    else:
                        if status[i-1] == 'unreg':  # 上月用户为未注册，本月未消费，则用户状态设置为未注册
                            status.append('unreg')
                        else:
                            status.append('unactive')  # 上月有注册，本月未消费，则设置为不活跃用户
                else:  # 本月有消费
                    if len(status) == 0:  # 首月有消费，则为新用户
                        status.append('new')
                    elif status[i-1] == 'unactive':  # 上月为不活跃用户，本月有消费，则设置为回流用户
                        status.append('return')
                    else:
                        status.append('active')  # 活跃用户
            return status

        purchase_status = df_purchase.apply(active_status, axis=1, raw=True)  # 逐行判断用户状态

        # 统计每月的新客，活跃用户，回流用户，不活跃用户
        purchase_status_ct = purchase_status.replace('unreg', np.NaN).apply(lambda x: pd.value_counts(x))
        purchase_stack = purchase_status_ct.fillna(0).T
        print(purchase_stack.head())
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.stackplot(purchase_stack.index, purchase_stack['active'], purchase_stack['new'], purchase_stack['return'],
                     purchase_stack['unactive'])
        plt.title('每月用户类型占比面积图')
        plt.legend(['active', 'new', 'return', 'unactive'], loc='center')
        # 根据每月不同用户的计数统计做面积图：
        #
        # 前三个月用户人数不断增加，新增用户数量占比较大，活跃用户数量上升
        # 1997年4月开始无新用户注册
        # 1997年4月开始活跃用户数量下降，最后趋于稳定，回流用户趋于稳定水平,该两层的用户为消费主力，约2000人上下浮动
        # 不活跃用户始终占大部分

        #
        fig = plt.figure(figsize=(16, 4))

        ax1 = fig.add_subplot(121)
        purchase_status_pct = purchase_status_ct.apply(lambda x: x / x.sum()).loc[['active', 'return']].T
        plt.plot(purchase_status_pct)
        plt.legend(['活跃用户', '回流用户'])
        plt.title('每月回流用户与活跃用户占比')

        ax2 = fig.add_subplot(122)
        purchase_status_pie = purchase_status_ct.T.apply(lambda x: x.sum()).loc[['active', 'return']]
        plt.pie(purchase_status_pie, autopct='%3.1f%%', startangle=90)
        plt.legend(['活跃用户', '回流用户'], bbox_to_anchor=(1.4, 0.7))
        plt.title('消费用户中回流用户与活跃用户的占比')
        plt.show()
        # 回流用户与活跃用户后期占比分别在4%-7%、2%-3%之间波动，均有下降趋势，有客户流失的预警
        # 后期消费用户中，回流用户占比60%，活跃用户占比40%，整体消费用户质量一般

    def user_purchase_period(self):
        # 用户购买周期
        def user_purchase_period_describe():
            # 用户购买周期描述
            order_diff = self.data.groupby('user_id').apply(lambda x: x.order_dt-x.order_dt.shift())
            # shift(): 默认axis=0，行往下移动，axis=1,列往左移动

            # print(order_diff.describe())
            # 用户平均购买周期为68天，标准差为91天，说明用户的购买周期波动较大
            # 用户购买周期中位数为31天，远小于其平均值，数据右偏，且购买周期最大值有533天，说明有小部分用户购买周期超长，存在极值干扰

            # 用户消费周期分布
            (order_diff / np.timedelta64(1, 'D')).hist(bins=20, figsize=(12, 4))
            plt.title('用户消费周期分布')
            plt.xlabel('天数')
            plt.ylabel('人数')
            # Text(0, 0.5, '人数')
            plt.show()

        user_purchase_period_describe()

obj = UserOrderAnalysis()
# obj.eda()
obj.process()
# obj.order_trend_analysis()
# obj.user_purchase_ability_analysis()
# obj.user_purchase_behavior_analysis()
# obj.rfm_model()
# obj.user_status_analysis()
obj.user_purchase_period()