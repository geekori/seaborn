'''

绘制多变量分布图


'''

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white",palette="colorblind",color_codes=True)

tips = sns.load_dataset('tips')
#sns.jointplot(x="tip",y="total_bill", data=tips, kind='kde')
# 用于绘制数据集中所有数值类型列两两之间的关系，如果数值类型列有n个，那么就会绘制n*n个分布图
sns.pairplot(tips)
print(tips.head())


plt.show()