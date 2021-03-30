#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/5/7 15:54
# Author: Hou hailun

import numpy as np
import pandas as pd

# 文章介绍groupby的基本原理及对应的agg、transform和apply操作。
company=["A","B","C"]
data=pd.DataFrame({
    "company":[company[x] for x in np.random.randint(0,len(company),10)],
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(15,50,10)
}
)

# 一、groupby的基本原理
#
group = data.groupby('company')
print(group)  # <pandas.core.groupby.DataFrameGroupBy object at 0x000002CBE6A71780>
print(list(group))  # 列表由3个元组构成，每个元组中，第一个元素是组别，第二个元素下的df
# 总结来说，groupby的过程就是将原有的DataFrame按照groupby的字段（这里是company），
# 划分为若干个分组DataFrame，被分为多少个组就有多少个分组DataFrame。
# 所以说，在groupby之后的一系列操作（如agg、apply等），均是基于子DataFrame的操作

print(' - ' * 40)
# 二、agg聚合操作
# 聚合操作是groupby后非常常见的操作，聚合操作可以用来求最大，最小，平均，求和等等
print(data.groupby('company').agg('mean'))  # 不同公司员工的平均年龄和平均薪水
# 对不同的列求不同的值
print(data.groupby('company').agg({'salary': 'median', 'age': 'mean'}))

# 三、transform
avg_salary_dict = data.groupby('company')['salary'].mean().to_dict()  # {'A': 26.5, 'B': 42.0, 'C': 31.6}
data['avg_salary'] = data['company'].map(avg_salary_dict)

data['avg_salary'] = data.groupby('company')['salary'].transform('mean')
# transform与agg的区别
# transform
# agg 会计算到A，B，C公司对应的值并直接返回
# transform 会对每一条数据求的响应的结果，同一组内的样本会有相同的值，组内求完后会按照原索引的顺序返回结果

# 四、apply
# 对于groupby后的apply，以分组后的子DataFrame作为参数传入指定函数的，基本操作单位是DataFrame，而之前介绍的apply的基本操作单位是Series

