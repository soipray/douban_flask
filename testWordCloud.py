# -*- codeing = utf8 -*-
# @Time 2020/9/15 16:25
# @Author : xxx
# @File : testWordCloud.py
# @Software: PyCharm

import jieba  # 分词
from matplotlib import pyplot as plt  # 绘图数据可视化
from wordcloud import WordCloud  # 词云
from PIL import Image  # 图片处理
import numpy as np  # 矩阵计算
import sqlite3  # 数据库

#准备词云需要文字
con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = "select instroduction from movie250"
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
con.close()

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
#print(string)
print(len(string))

img = Image.open(r".\static\assets\img\tree.jpg")
img_array = np.array(img) #将图片转换为数组
wc = WordCloud (
    background_color='white',
    mask=img_array,
    font_path="simsun.ttc"    # C:\windows\fonts 需要支持中文
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') #是否显示坐标轴

#plt.show() #显示词云图片
plt.savefig(r'.\static\assets\img\word.jpg', dpi=500)

