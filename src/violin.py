'''

琴形图

'''

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white",palette="colorblind",color_codes=True)

tips = sns.load_dataset('tips')
print(tips.head())
sns.set(style="white", color_codes=True)  #设置样式

sns.set(style="whitegrid", color_codes=True)
fig, axes = plt.subplots(1,2,figsize=(10, 5))
# 对数据切分
'''
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips,
               split=True, ax=axes[0])
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips,
               split=True, inner="stick", palette="Set3",ax=axes[1])

'''
sns.violinplot(x="day", y="total_bill", data=tips,
               inner=None, ax=axes[0])
#inner内部不填充
sns.swarmplot(x="day", y="total_bill", data=tips,
              color="w", alpha=.5, ax=axes[0])

sns.boxplot(x="day", y="total_bill", data=tips, ax=axes[1])
sns.stripplot(x="day", y="total_bill", data=tips,
              jitter=True, color="w", alpha=.5, ax=axes[1])
plt.show()