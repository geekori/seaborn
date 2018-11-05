'''

柱状图

'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white",palette="colorblind",color_codes=True)

tips = sns.load_dataset('tips')
print(tips.head())
sns.set(style="white", color_codes=True)  #设置样式
fig,axes = plt.subplots(1,2,figsize=(10,5))

sns.barplot(x="sex",y="total_bill",hue="day",data=tips,ax=axes[0])

sns.countplot(x="size",data=tips,palette="Greens_d",ax=axes[1])

plt.show()