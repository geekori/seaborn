'''

用set方法完成主题，调色板等设置工作

'''

import seaborn as  sns
import numpy as np
import matplotlib.pyplot as plt
# color_codes：True，使用seaborn的调色板，如果为False，不会使用seaborn的调色板
sns.set(style="darkgrid",palette="colorblind",color_codes=True)
values = np.arange(20)
print(values)
plt.plot(values,color="r")
plt.show()