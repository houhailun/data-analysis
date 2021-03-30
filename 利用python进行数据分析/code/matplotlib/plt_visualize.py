#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
数据可视化：使用matplotlib模块绘制图
"""

import matplotlib.pyplot as plt
import numpy as np
from random import choice


def draw():
    fig = plt.figure()  # 生成画布，图片都是在figure对象中

    ax1 = fig.add_subplot(2, 2, 1)  # 空fig不能绘图，必须创建subplot
    ax2 = fig.add_subplot(2, 2, 2)  # fig分为4份，占用第二份
    ax3 = fig.add_subplot(2, 2, 3)

    plt.plot(np.random.randn(50).cumsum(), 'k--')  # plot()画图，k--是线型选择，表示虚线
    _ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)  # 绘制柱状图
    ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))  # 绘制散列点

    fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
    for i in range(2):
        for j in range(2):
            axes[i, j].hist(np.random.randn(50), bins=50, color='k', alpha=0.5)
    plt.subplots_adjust(wspace=0, hspace=0)  # 调整图片间距

    # 颜色、标记、线性
    # plt.plot(np.random.randn(30), 'ko--')
    # plt.plot(np.random.rand(50), color='k', linestyle='--', marker='o')  # 带标记，强调实际数据点

    data = np.random.rand(30).cumsum()
    # plt.plot(data, 'k--', label='steps-post')
    # plt.legend(loc='best')

    # 刻度、标签和图例


    plt.show()


def draw_line_chart():
    """绘制折线图"""
    # 绘制折线图
    # plot()可以接收输入参数和输出参数，线条粗细等参数，如果至指定输出参数，那么输入参数默认由0开始
    # case1: plot函数指定输出参数
    squares = [1, 4, 9, 16, 25]
    plt.plot(squares, linewidth=5)
    plt.title("squares numbers", fontsize=24)  # 指定标题，设置标题字体大小
    plt.xlabel('values', fontsize=14)  # 指定X坐标轴的标签，设置标签字体大小
    plt.ylabel('squares of values', fontsize=14)  # 执行Y坐标轴的标签，设置标签字体大小
    plt.tick_params(axis='both', labelsize=14)  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为14
    plt.show()

    # case2: plot函数指定输入参数和输出参数
    input_values = [1, 2, 3, 4, 5]
    output_values = [1, 4, 9, 16, 25]
    plt.plot(input_values, output_values, linewidth=5)
    plt.title("squares numbers", fontsize=24)  # 指定标题，设置标题字体大小
    plt.xlabel('values', fontsize=14)  # 指定X坐标轴的标签，设置标签字体大小
    plt.ylabel('squares of values', fontsize=14)  # 执行Y坐标轴的标签，设置标签字体大小
    plt.tick_params(axis='both', labelsize=14)  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为14
    plt.show()


def draw_sactter():
    """
    绘制散点图
    参数说明:
        x_values: 横坐标数据列表
        y_values: 纵坐标数据列表
        s: 设置点大小
        edgecolors: 数据点的轮廓，默认为‘none’，表示删除轮廓
    """

    # x_values = [1, 2, 3]
    # y_values = [1, 4, 9]
    x_values = list(range(1, 11))
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, s=20, edgecolors='red')  # 传递一对x,y坐标，绘制若干个点，s设置点大小(注意两个数组元素数量必须相等)
    plt.title('squares numbers', fontsize=10)
    plt.xlabel('values', fontsize=14)
    plt.ylabel('squares value', fontsize=14)
    plt.show()


def color_map():
    """颜色映射"""
    x_values = list(range(1, 11))
    y_values = [x ** 2 for x in x_values]
    # 模块pyplot内置了一组颜色映射，通过设置c参数为y列表的值（这个y列表的是[1,2,3,4,5]）
    # 根据y列表的值大小进行颜色映射的，值大的颜色深，值小的颜色浅。如果y列表的值按顺序，并且映射到按顺序的点，那么自然颜色也是从浅到深。
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=100)
    plt.title('square numbers', fontsize=24)
    plt.xlabel('values', fontsize=14)
    plt.ylabel('squares values', fontsize=14)
    plt.show()
    # plt.savefig('./1.png', bbox_inches='tight')  # bbox_inches='tight'：将图标多余的空白区裁剪掉


class RandomWalk:
    """随机漫步类"""
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """获取随机方向和步数的乘积"""
        return choice([1, -1]) * choice([0, 1, 2, 3, 4])

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # 原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一步的位置
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # 保存下一步
            self.x_values.append(next_x)
            self.y_values.append(next_y)


def plt_draw():
    # draw_line_chart

    # draw_sactter()

    # color_map()

    while True:
        rw = RandomWalk(5000)
        rw.fill_walk()

        plt.figure(figsize=(20, 6))  # 设置画布大小

        # 颜色映射就是用列表赋值给c，而这个列表的值可以随意，大的代表颜色深，小的代表颜色浅。
        point_number = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, s=4)

        # 突出起点和终点，用不同颜色
        plt.scatter(0, 0, c='green', s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

        # 隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()

        keep_running = input("make another walk?(y/n)")
        if keep_running == 'n':
            break


def test():
    """数据可视化练习"""
    # 1、折线图
    # x = np.linspace(0, 2, 100)
    #
    # plt.plot(x, x, label='linear')
    # plt.plot(x, x**2, label='quadratic')
    # plt.plot(x, x**3, label='cubic')
    #
    # plt.xlabel('x labels')
    # plt.ylabel('y lables')
    # plt.title('simplt plot')
    # plt.legend()
    # plt.show()

    # 2、散点图
    # x = np.arange(0, 5, 0.2)
    # plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')
    # # plt.scatter(x, x)
    # plt.show()

    # 3、直方图
    # np.random.seed(19680801)
    # mu1, sigma1 = 100, 15
    # mu2, sigma2 = 80, 15
    # x1 = mu1 + sigma1 * np.random.randn(10000)
    # x2 = mu2 + sigma2 * np.random.randn(10000)
    #
    # # 50: 把数据分为50组
    # # color: 颜色, alpha: 透明度， density: 是密度而非具体数值
    # # 返回值 n: 概率值    bins: 具体数据  patches:直方图对象
    # n1, bins1, patches1 = plt.hist(x1, 100, density=True, color='g', alpha=1)
    # n2, bins2, patches2 = plt.hist(x2, 100, density=True, color='r', alpha=0.2)
    #
    # plt.xlabel('smart')
    # plt.ylabel('probablity')
    # plt.title('histogram of iq')
    # plt.text(110, .025, r'$\mu=100,\ \sigma=15$')   # 设置均值、方差
    # plt.text(50, .025, r'$\mu=80,\ \sigma=15$')
    #
    # plt.axis([40, 160, 0, 0.03])    # 设置x、y轴具体范围
    # plt.grid(True)                  # 添加网格
    # plt.show()

    # 4、柱状图 -- 并列柱状图
    size = 5
    a = np.random.random(size)
    b = np.random.random(size)
    c = np.random.random(size)
    x = np.arange(size)
    #
    # total_width, n = 0.8, 3
    # width = total_width / n
    #
    # x = x - (total_width - width) / 2
    # print(x)
    # # 这里使用的是偏移
    # plt.bar(x, a, width=width, label='a')
    # plt.bar(x+width, b, width=width, label='b')
    # plt.bar(x+2*width, c, width=width, label='c')
    # plt.legend()
    # plt.show()

    # 柱状图 --叠加柱状图
    # 使用偏移
    # plt.bar(x, a, width=0.5, label='a', fc='r')
    # plt.bar(x, b, bottom=a, width=0.5, label='b', fc='g')
    # plt.bar(x, b, bottom=a+b, width=0.5, label='c', fc='b')
    #
    # plt.ylim(0, 2.5)
    # plt.legend()
    # plt.grid(True)
    # plt.show()

    # 5、饼图 --普通饼图
    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    # sizes = [15, 30, 45, 10]
    # explode = (0, 0.1, 0, 0)  # 设置分离的距离，0表示不分离
    # plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    # plt.axis('equal')  # equal aspect ratio 保证画出的图是正圆形
    # plt.show()

    # 饼图--嵌套饼图
    # size = 0.3
    # vals = np.array([[60, 32], [37, 40], [29, 10]])
    #
    # cmap = plt.get_cmap('tab20c')  # 通过get_camp随机获取颜色
    # outer_colors = cmap(np.arange(3)*4)
    # inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))
    #
    # # 外部饼图: 数据有3个，radius:饼图半径，colors: 设置颜色，wedgeprops:参数字典传递给wedge对象用来画一个饼图
    # print(vals.sum(axis=1))  # [92, 77, 39]
    # plt.pie(vals.sum(axis=1), radius=1, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'))
    #
    # # 内部饼图
    # print(vals.flatten())  # [60. 32. 37. 40. 29. 10.]
    # plt.pie(vals.flatten(), radius=1-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))
    #
    # plt.axis('equal')
    # plt.show()

    # 6、三维图
    # 6.1 绘制三维散点图
    from mpl_toolkits.mplot3d import Axes3D
    # data = np.random.randint(0, 255, size=[40, 40, 40])  # 三维数据:40X40X40
    # x, y, z = data[0], data[1], data[2]
    # ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
    #
    # # 将数据点分为三部分画，并作颜色区分
    # ax.scatter(x[:10], y[:10], z[:10], c='y')
    # ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
    # ax.scatter(x[30:], y[30:], z[30:], c='g')
    # ax.set_zlabel('Z')  # 坐标轴
    # ax.set_ylabel('Y')
    # ax.set_xlabel('X')
    # plt.show()

    # 6.2 绘制三维平面图
    # fig = plt.figure()
    # ax = Axes3D(fig)
    # # 初始化散点数据为网格数据
    # X = np.arange(-4, 4, 0.25)
    # Y = np.arange(-4, 4, 0.25)
    # X, Y = np.meshgrid(X, Y)
    #
    # R = np.sqrt(X**2 + Y**2)
    # Z = np.sin(R)
    #
    # # 三维曲面函数:rstride-行步长 cstride-列步长 cmap-渐变颜色
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    # plt.show()


def test_sin_cos():
    """绘制正弦和余弦函数"""

    # 1、简单绘图
    # x = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # 在指定的间隔内返回均匀间隔的数字
    # C, S = np.cos(x), np.sin(x)
    #
    # plt.plot(x, C)
    # plt.plot(x, S)
    # plt.show()

    # 2、设置基本元素：线的颜色、粗细、线形   刻度和标签   图例
    plt.figure(figsize=(10, 6), dpi=80)  # 设置画布
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(x), np.sin(x)

    # 设置线的颜色，粗细，线形
    plt.plot(x, C, color='blue', linewidth=2.5, linestyle='-', label=r'sin(x)')
    plt.plot(x, S, color='red', linewidth=2.5, linestyle='-', label=r'cos(x)')

    # 如果觉得线条离边界太近，可以加大距离
    plt.xlim(x.min()*1.2, x.max()*1.2)
    plt.ylim(C.min()*1.2, C.max()*1.2)

    # 当前刻度不清晰，重新设定，加上直观的标签
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
               [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])  # $\$ 实际上是转义操作
    plt.yticks([-1, 0, 1], [r'-1', r'0', r'1'])

    # plt.legend()  # 添加图例

    # 3、移动轴线
    # 只需要两轴线(x,y轴)，把顶部和右边的轴线隐藏起来，在移动x，y轴到指定位置
    ax = plt.gca()  # 获取当前子图
    ax.spines['right'].set_color('none')  # 把顶部和右边的轴线隐藏起来
    ax.spines['top'].set_color('none')

    ax.spines['bottom'].set_position('zero')  # 在移动x，y轴到指定位置
    ax.spines['left'].set_position('zero')
    # plt.show()

    # 4、添加注释
    # 使用annotate命令注释,选择2π/3作为我们想要注解的正弦和余弦值。我们将在曲线上做一个标记和一个垂直的虚线。然后，使用annotate命令来显示一个箭头和一些文本
    t = 2 * np.pi / 3

    # plt.plot()绘制向下的一条垂直曲线，plt.scatter()绘制一个点
    plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle='--')
    plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

    # annotate参数说明: annotate(s='str' ,xy=(x,y) ,xytext=(l1,l2) ,..)
    # s:注释文本内容  xy:对哪一点进行注释 xytext:注释文字的坐标位置 xycoords:指定类型，data表示基于数值来定位
    # textcoords='offset points'表示相对位置  fontsize:注释大小  arrowprops:对箭头的一些设置
    plt.annotate(s=r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
                 xy=(t, np.sin(t)), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # 利用plt.plot绘制向上的一条垂直的线，利用plt.scatter绘制一个点。
    plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
    plt.scatter([t, ], [np.sin(t), ], 50, color='red')

    plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                 xy=(t, np.cos(t)), xycoords='data',
                 xytext=(-90, -50), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    plt.show()


def test_subplot():
    """
    子图与子区
    subplot: 子区，基于网格grid来规划
    axes:子图
    """
    # 1、子区
    # plt.subplot(2, 2, 1)  # 把figure分按2行2列的布局进行分区，然后取索引为1的子图(索引从0开始)

    # def fig(t):
    #     return np.exp(-t) * np.cos(2*np.pi*t)
    # t1 = np.arange(0.0, 5.0, 0.1)
    # t2 = np.arange(0.0, 5.0, 0.02)
    # plt.figure(1)
    #
    # plt.subplot(211)  # 等同于plt.subplot(2,2,1)
    # plt.plot(t1, fig(t1), 'bo', t2, fig(t2), 'k')
    #
    # plt.subplot(212)  # 等同于plt.subplot(2,2,2)
    # plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    # plt.show()

    # 2、子图axes
    # 一个子图可能有一个或多个子区域构成，更加灵活
    # axes1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # 分为3X3的区域，axes1有3行个区域构成
    # axes2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    # axes3 = plt.subplot2grid((3, 3), (1, 2), rowspan=3)  # xes1有3列个区域构成
    # axes4 = plt.subplot2grid((3, 3), (2, 0))
    # axes5 = plt.subplot2grid((3, 3), (2, 1))

    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 3.0, 0.01)
    ax1 = plt.subplot(212)
    ax1.margins(0.05)
    ax1.plot(t1, f(t1), 'k')

    ax2 = plt.subplot(221)
    # ax2.margins(2, 2)
    ax2.plot(t1, f(t1), 'r')
    ax2.set_title('Zoomed out')

    ax3 = plt.subplot(222)
    ax3.margins(x=0.0, y=0.25)  # x,y必须0到1之间
    ax3.plot(t1, f(t1), 'g')
    ax3.set_title('Zoomed in')
    plt.show()


def test_gif():
    """
    GIF动态图：matplotlib只能对静态图进行绘制显示；动态图是由一帧一帧的画面组合的，由ImageMagick完成
    动图绘制路线：初始化图像-> FuncAnimation() -> 不断改变原始曲线值
    """
    from matplotlib.animation import FuncAnimation
    from IPython.display import Image
    from matplotlib.animation import ImageMagickFileWriter
    writer = ImageMagickFileWriter()

    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = ax.plot([], [], 'r-', animated=False)

    # 生成数据(用于传入update函数)
    def data_gen():
        pass

    # 初始化图像
    def init():
        ax.set_xlim(0, 2*np.pi)  # 设置x轴范围
        ax.set_ylim(-1.1, 1.1)
        return ln,

    # 将更新后的数据添加到图像中
    def update(data):
        xdata.append(data)
        ydata.append(np.sin(data))
        ln.set_data(xdata, ydata)  # 重新设置曲线的值
        return ln,

    # 核心方法入口
    # 参数说明:
    ani = FuncAnimation(fig,  # 画布
                        update,  # 我们每个时刻要更新图形对象的函数
                        frames=np.linspace(0, 2*np.pi, 50),  # 相当于时刻t，要模拟多少帧图画，不同时刻的t相当于animat的参数
                        interval=50,  # 刷新频率，毫秒
                        init_func=init,  # 初始化函数，其返回值就是每次都要更新的对象
                        blit=True)  # blit是一个非常重要的关键字，它告诉动画只重绘修改的部分，结合上面保存的时间,true会使动画显示得会非常非常快

    # 需要安装ImageMagick
    # ani.save('ming.gif', writer='imagemagick')

    plt.show()


if __name__ == "__main__":
    # draw()

    # plt_draw()

    # test()

    # test_sin_cos()

    # test_subplot()

    test_gif()