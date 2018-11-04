'''
绘制分类散点图

分类图：散点图、箱线图、琴形图和柱状图

group by

'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white",palette="colorblind",color_codes=True)

tips = sns.load_dataset('tips')
print(tips.head())
sns.set(style="white", color_codes=True)  #设置样式
#sns.stripplot(x="day",y="total_bill",data=tips,jitter=False)
sns.swarmplot(x="day",y="total_bill",data=tips,hue="sex")
plt.show()