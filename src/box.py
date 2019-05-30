'''
箱线图
hello world
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white",palette="colorblind",color_codes=True)

tips = sns.load_dataset('tips')
print(tips.head())
sns.set(style="white", color_codes=True)  #设置样式
sns.boxplot(x="day",y="total_bill",hue="sex",data=tips)
plt.show()
