#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/9/11 15:41
# Author: Hou hailun

# 数据可视化: matplotlib

import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(start=-1, stop=1, num=50)  # 定义一个数据，范围为-1，1，50个元素
# y = 2 * x + 1
# plt.figure()    # 定义图像窗口
# plt.plot(x, y)  # 绘制曲线
# plt.show()

# 2、简单的线条  figure是图像窗口对象，窗口中可以有多个小图片
# x = np.linspace(start=-3, stop=3, num=50)
# y1 = 2 * x + 1
# y2 = x ** 2
# plt.figure(num=3, figsize=(8, 5))  # 编号为3，大小为（8，5）
# plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='liner line')  # 指定颜色，线宽度，线类型
# plt.plot(x, y2, label='square line')
# plt.show()

# 3、设置坐标轴1
# plt.xlim((-1, 2))  # xlim()：设置X坐标轴范围
# plt.ylim((-2, 3))
# plt.xlabel('I am x')  # xlabel(): 设置坐标轴名称
# plt.ylabel('I am y')
#
# new_ticks = np.linspace(start=-1, stop=2, num=5)
# print(new_ticks)
# plt.xticks(new_ticks)  # 设置x轴刻度
# 设置y轴刻度，并对每个刻度指定名称
# plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
# plt.show()

# 4、设置坐标轴2
# 使用plt.gca获取当前坐标轴信息. 使用.spines设置边框：右侧边框；使用.set_color设置边框颜色：默认白色；
# 使用.spines设置边框：上边框；使用.set_color设置边框颜色：默认白色
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# plt.show()

# 调整坐标轴
# ax.xaxis.set_ticks_position('bottom')  # 设置X坐标刻度数字或名称的位置（所有位置：top，bottom，both，default，none）
# ax.spines['bottom'].set_position(('data', 0))  # spines设置边框:X轴；set_position设置边框位置：y=0的位置
#
# ax.yaxis.set_ticks_position('left')  # 设置Y坐标轴刻度数字或名称的位置
# ax.spines['left'].set_position(('data', 0))  # 使用.spines设置边框：y轴；使用.set_position设置边框位置：x=0的位置；（位置所有属性：outward，axes，data）
# plt.show()

# 5、添加图例: legend图例就是为了帮我们展示出每个数据对应的图像名称
# 在plot()中添加label参数，然后legend()显示
# plt.legend(loc='upper right')
# plt.show()

# 6、画出基本图
# x = np.linspace(start=-3, stop=3, num=50)
# y = 2 * x + 1
#
# plt.figure(num=1, figsize=(8, 5))
# plt.plot(x, y)
# plt.show()
# 移动坐标
# ax = plt.gca()
# ax.spines['right'].set_color('none')  # 设置四周边框
# ax.spines['top'].set_color('none')
# ax.spines['left'].set_position(('data', 0))
# ax.spines['bottom'].set_position(('data', 0))
# ax.xaxis.set_ticks_position('bottom')  # 设置刻度位置
# ax.yaxis.set_ticks_position('left')

# 标注出点(x0, y0)的位置信息. 用plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5) 画出一条垂直于x轴的虚线.
# x0 = 1
# y0 = 2 * x0 + 1
# plt.plot([x0, x0], [0, y0], 'k--', linewidth=2.5)  # 绘制直线
# plt.scatter([x0,], [y0,], s=50, color='b')  # 在(x0,y0)处画一个点
# plt.show()

# 添加注释 annotate
# 参数xycoords='data'：基于数据的值来选位置
# 参数xytest=(30, -30): 注释的位置
# textcoords='offset points': xy偏差值
# arrowprops: 箭头的设置
# plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(30, -30),
#              textcoords='offset points', fontsize=16,
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=0.2'))
# plt.show()

# 添加注释text
# 其中-3.7, 3,是选取text的位置, 空格需要用到转字符\ ,fontdict设置文本字体
# plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
#          fontdict={'size': 16, 'color': 'r'})
# plt.show()


def plt9_tick_visibility():
    """
    tick 能见度
    当图片中的内容较多，相互遮盖时，我们可以通过设置相关内容的透明度来使图片更易于观察，也即是通过本节中的bbox参数设置来调节图像信息
    :return:
    """
    x = np.linspace(start=-3, stop=3, num=50)
    y = 0.1 * x

    plt.figure()
    plt.plot(x, y, linewidth=10)  # zorder给plot在z方向排序
    # plt.plot(x, y, linewidth=10, zorder=1)  # zorder给plot在z方向排序
    plt.ylim(-2, 2)
    ax = plt.gca()
    ax.spines['right'].set_color('none')  # 设置四周边框
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.xaxis.set_ticks_position('bottom')  # 设置刻度位置
    ax.yaxis.set_ticks_position('left')

    # 对被遮挡的图像调节相关透明度，本例中设置 x轴 和 y轴 的刻度数字进行透明度设置
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(12)
        label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.8, zorder=2))
    plt.show()


def plt10_scatter():
    """
    散点图
    :return:
    """
    n = 2014
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)

    # 输入X和Y作为location，size=75，颜色为T，color map用默认值，透明度alpha 为 50%。 x轴显示范围定位(-1.5，1.5)，并用xtick()函数来隐藏x坐标轴，y轴
    plt.scatter(X, Y, s=75, c=T, alpha=0.5)
    plt.xlim(-1.5, 1.5)
    plt.xticks(())
    plt.ylim(-1.5, 1.5)
    plt.yticks(())

    plt.show()


def plt11_bar():
    """
    柱状图
    :return:
    """
    n = 12
    X = np.arange(n)
    Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

    # plt.bar(X, +Y1)
    # plt.bar(X, -Y2)

    plt.xlim(-5, n)
    plt.ylim(-1.25, 1.25)
    plt.xticks(())
    plt.yticks(())

    # 加颜色和数据：用facecolor设置主体颜色，edgecolor设置边框颜色为白色
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    # 用函数plt.text分别在柱体上方（下方）加上数值，用%.2f保留两位小数，横向居中对齐ha='center'，纵向底部（顶部）对齐va='bottom'
    for x, y in zip(X, Y1):
        plt.text(x+0.1, y+0.05, '%.2f' % y, ha='center', va='bottom')

    for x, y in zip(X, Y2):
        plt.text(x+0.1, -y-0.05, '%.2f' % y, ha='center', va='top')
    plt.show()


def plt12_contours():
    """
    等高线图
    :return:
    """
    # 等高线函数
    def f(x, y):
        return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)

    # 把x,y数据生成mesh网格状的数据，因为等高线的显示是在网格的基础上添加上高度值
    X, Y = np.meshgrid(x, y)

    # 颜色填充,位置参数分别为：X, Y, f(X,Y)。透明度0.75，并将 f(X,Y) 的值对应到color map的暖色组中寻找对应颜色
    plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

    # 等高线绘制:位置参数为：X, Y, f(X,Y)。颜色选黑色，线条宽度选0.5, 8代表等高线的密集程度
    C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=0.5)

    # 添加高度数字：inline控制是否将Label画在线里面，字体大小为10。并将坐标轴隐藏
    plt.clabel(C, inline=True, fontsize=10)
    plt.xticks(())
    plt.yticks(())

    plt.show()


def plt13_image():
    """
    Image 图片
    :return:
    """
    a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
                  0.365348418405, 0.439599930621, 0.525083754405,
                  0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)

    """
    for the value of "interpolation", check this:
    http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
    for the value of "origin"= ['upper', 'lower'], check this:
    http://matplotlib.org/examples/pylab_examples/image_origin.html
    """
    plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
    plt.colorbar(shrink=.92)  # 使colorbar的长度变短为原来的92%

    plt.xticks(())
    plt.yticks(())
    plt.show()


def plt14_3D():
    """
    3D 图
    :return:
    """
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()  # 定义图像窗口
    ax = Axes3D(fig)    # 添加3D坐标轴

    # X, Y value
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)  # x,y平面的网格
    R = np.sqrt(X**2 + Y**2)
    # height value
    Z = np.sin(R)

    # 做出一个三维曲面，并将一个 colormap rainbow 填充颜色，之后将三维图像投影到 XY 平面上做一个等高线图
    # rstride 和 cstride 分别代表 row 和 column 的跨度。
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, camp=plt.get_cmap('rainbow'))
    plt.show()





# plt9_tick_visibility()
# plt10_scatter()
# plt11_bar()
# plt12_contours()
# plt13_image()
plt14_3D()