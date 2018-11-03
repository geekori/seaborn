'''
绘制离散点


建议使用Anaconda Python环境

'''

import matplotlib.pyplot as plt
import seaborn as sns
years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [431.2,657.4,1233.1,2976.3,6743,11201,16323.1]
#sns.set_style("whitegrid")
sns.set_style("dark")

plt.scatter(years,gdp)
plt.show()
