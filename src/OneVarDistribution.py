'''

绘制单变量分布图


分布图：用于观察数据值的变化趋势。

分布图种类：
1. 直方图：hist
2. 密度图：kde
3. 毛毯图：rug

'''

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white",palette="colorblind",color_codes=True)

tips = sns.load_dataset('tips')
print(tips.head())
# 绘制分布图，默认绘制了直方图和密度图
#sns.distplot(tips['total_bill'],kde=False)
#sns.distplot(tips['total_bill'],kde=True,hist=False)
#sns.distplot(tips['total_bill'],kde=True,rug=True)

fig,axes = plt.subplots(1,2,figsize= (10,5))
sns.distplot(tips['total_bill'],ax=axes[0],kde=True,rug=True)

sns.kdeplot(tips['total_bill'],ax = axes[1],shade=True)
sns.rugplot(tips['total_bill'],ax = axes[1])
plt.show()