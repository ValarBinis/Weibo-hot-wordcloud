#!/usr/bin/env Python 
# -*- coding:utf-8 -*-
# autuor:DongBin
# time:2020/8/26
"""
-------------分析--------------------
1、数据导入
2、数据处理
3、合并列表
4、绘制词云
"""

import os,re
from wordcloud import WordCloud
import numpy as np
import matplotlib.pylab as plt


def wordcloud(text):
    print("正在生成词云图")
    WordClouding = WordCloud(
        font_path=r'C:\\Windows\Fonts\simkai.ttf',
        background_color='white',
        width=1920,     # 
        height=1080,  # 这里修改图片大小  
    ).generate(text)
    
    WordClouding.to_file('image_cloud.png')


if __name__ == '__main__':
    print("正在读取数据")
    file_list = os.listdir('./saves')  # 读取文件夹下的所有文件列表
    keywords_full = ''
    for file in file_list:
        with open(f'./saves/{file}', 'r', encoding='GBK') as f:
            # print(type(f.readline())) # 发现内容是str类型的，因为我设计的就是列表里嵌套字典，所以我用正则来匹配
            # print(f.readline())  # 查看输出内容，那么正则应该写成 \'keyword\'\:\s\'\w+\'
            file_text = f.readline()
            keyword_list = list(re.findall("\'keyword\'\:\s\'\w+\'", file_text))
            # print(keyword_list[0])
            for i in keyword_list:
                keywords = eval(i.split(':')[1])
                # print(keywords)
                keywords_full = ' '.join([keywords_full, keywords]) # 将keywords添加到keywords_full的结尾，中间用空格分开
    # print(keywords_full) 通过上面的信息用正则清洗了一遍之后获得了我们要的信息
    wordcloud(keywords_full)


