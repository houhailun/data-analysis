#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/5/7 15:16
# Author: Hou hailun

import numpy as np
import pandas as pd

# 在日常的数据处理中，经常会对一个DataFrame进行逐行、逐列和逐元素的操作，对应这些操作，Pandas中的map、apply和applymap可以解决绝大部分这样的数据处理需求

boolean=[True,False]
gender=["男","女"]
color=["white","black","yellow"]
data=pd.DataFrame({
    "height":np.random.randint(150,190,100),
    "weight":np.random.randint(40,90,100),
    "smoker":[boolean[x] for x in np.random.randint(0,2,100)],
    "gender":[gender[x] for x in np.random.randint(0,2,100)],
    "age":np.random.randint(15,90,100),
    "color":[color[x] for x in np.random.randint(0,len(color),100) ]
}
)


# series处理
def series_map():
    # map用法
    # 需求：把gender列的男替换为1，女替换为0
    data['gender1'] = data['gender'].map({'男':1,'女':0})
    print(data.head())

    def gender_map(x):
        gender = 1 if x == '男' else 0
        return gender
    data['gender2'] = data['gender'].map(gender_map)
    print(data.head())
    # map方法都是把对应的数据逐个当作参数传入到字典或函数中，得到映射后的值。
    # 注意：map函数只能接受1个参数

    data['gender3'] = data['gender'].apply(gender_map)
    print(data.head())


def series_apply():
    # apply和map类型，区别在于apply嫩巩固传入功能更为复杂的函数
    # 假设在数据统计的过程中，年龄age列有较大误差，需要对其进行调整（加上或减去一个值），由于这个加上或减去的值未知，故在定义函数时，需要加多一个参数bias，此时用map方法是操作不了的（传入map的函数只能接收一个参数），apply方法则可以解决这个问题
    def apply_age(x, bias):
        return x + bias
    # 以元组的形式传入额外的参数
    data['age1'] = data['age'].apply(apply_age, args=(-2,))
    print(data.head())

# series_apply()


# dataframe数据处理
def df_apply():
    # 沿着0轴求和：即沿列，跨行
    print(data[["height","weight","age"]].apply(np.sum, axis=0))

    def BMI(series):
        weight = series['weight']
        height = series['height'] / 100
        BMI = weight / height ** 2
        return BMI
    # 沿着1轴：将每一行数据以Series的形式（Series的索引为列名）传入指定函数，返回相应的结果。
    data['BMI'] = data.apply(BMI, axis=1)
    print(data.head())

    # 总结：
    # 当axis=0时，对每列columns执行指定函数；当axis=1时，对每行row执行指定函数。
    # 无论axis=0还是axis=1，其传入指定函数的默认形式均为Series，可以通过设置raw=True传入numpy数组。
    # 对每个Series执行结果后，会将结果整合在一起返回（若想有返回值，定义函数时需要return相应的值）
    # 当然，DataFrame的apply和Series的apply一样，也能接收更复杂的函数，如传入参数等，实现原理是一样的，具体用法详见官方文档。

# df_apply()


def df_apply_map():
    # aplymap()对df中每个单元格执行指定函数
    df = pd.DataFrame(
        {
            "A": np.random.randn(5),
            "B": np.random.randn(5),
            "C": np.random.randn(5),
            "D": np.random.randn(5),
            "E": np.random.randn(5),
        }
    )

    # 对所有值保留2为小数
    df = df.applymap(lambda x: '%.2f' % x)
    print(df)

# df_apply_map()
