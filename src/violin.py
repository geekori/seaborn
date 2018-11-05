'''

琴形图

'''

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white",palette="colorblind",color_codes=True)

tips = sns.load_dataset('tips')
print(tips.head())
sns.set(style="white", color_codes=True)  #设置样式
fig,axes = plt.subplots(2,2,figsize=(10,10))

sns.violinplot(x="day",y="total_bill",hue="sex",split=True,data=tips,ax=axes[0,0])
# inner:box、stick、None
sns.violinplot(x="day",y="total_bill",hue="sex",split=True,inner=None,data=tips,ax=axes[0,1])

sns.violinplot(x="day",y="total_bill",inner=None,data=tips,ax=axes[1,0])

sns.swarmplot(x="day",y="total_bill",data=tips,color="w",alpha=0.5,ax=axes[1,0])

sns.boxplot(x="day",y="total_bill",data=tips,ax=axes[1,1])

sns.swarmplot(x="day",y="total_bill",data=tips,color="w",alpha=0.5,ax=axes[1,1])



plt.show()