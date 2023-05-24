"""
二、
一个代码列表长度500，要求以80个为一个批次，
拆分成多个数组打印输出，
测试数据来源：https://edidata.oss-cn-beijing.aliyuncs.com/fyx_chinamoney.csv，
可以下载到本地用做测试数据
"""

import pandas as pd


# 读取本地 CSV 表格
data = pd.read_csv('fyx_chinamoney.csv', names=['col1'])

# 读取在线 CSV 表格
# url = 'https://edidata.oss-cn-beijing.aliyuncs.com/fyx_chinamoney.csv'
# data = pd.read_csv(url, names=['col1'])

# 定义批次大小
batch_size = 80

# 拆分数组
split_data = [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

# 打印输出
for i, batch in enumerate(split_data):
    print(f'Batch {i+1}: {batch}')
