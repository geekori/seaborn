'''

移除坐标轴

'''


import seaborn as  sns
import numpy as np
import matplotlib.pyplot as plt
# color_codes：True，使用seaborn的调色板，如果为False，不会使用seaborn的调色板
sns.set(style="white",palette="colorblind",color_codes=True)
values = np.arange(20)

plt.plot(values,color="r")
#sns.despine()
sns.despine(offset=30,trim=True)
#sns.despine(left=True,bottom=True)
plt.show()