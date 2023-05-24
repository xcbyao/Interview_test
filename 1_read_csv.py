"""
一、
https://iftp.chinamoney.com.cn/english/bdInfo/
1. 从链接页面获取公开数据
2. 需要获取数据的条件: Bond Type=Treasury Bond, Issue Year=2023
3. 解析返回表格数据，列名包括ISIN, Bond Code, Issuer, Bond Type, Issue Date, Latest Rating
4. 保存成有效csv文件。
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 设置请求参数
params = {
    'Bond Type': 'Treasury Bond',
    'Issue Year': '2023'
}

# 发送请求
response = requests.get('https://iftp.chinamoney.com.cn/english/bdInfo/', headers=headers, params=params)

# 解析 HTML
#soup = BeautifulSoup(response.text, 'html.parser')

# 使用 Selenium 模拟浏览器操作，获取动态加载的网页内容
driver = webdriver.Chrome()
driver.get('https://iftp.chinamoney.com.cn/english/bdInfo/')
html = driver.page_source

# 使用 BeautifulSoup 解析网页内容，并获取表格数据
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')
df = pd.read_html(str(table))[0]

# 检查是否读取到了数据
if df.empty:
    print("Error: No tables found.")
else:
    print("Data loaded successfully.")

# 选择需要的列名
df = df[['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating']]

# 保存为 CSV 文件
df.to_csv('bond_info.csv', index=False)
