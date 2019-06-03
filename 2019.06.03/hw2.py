import numpy as np
import random
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# https://carbon.now.sh

a = 1
b = 2
std = 5
size = 100000

x = np.random.randint(0,100,size=size)
y = a * x + b + np.random.normal(0,std,size=size)

print(x)

sns.jointplot(x=x,y=y,kind='kde')
plt.show()

# 计算平均值
mx = x.mean()
my = y.mean()

print(mx,my)
# 计算标准差
stdx = x.std()
stdy = y.std()

print(stdx,stdy)
# 计算协方差矩阵
# covxy = np.cov(x, y)
# print(covxy)
# covx等于covxy[0, 0], covy等于covxy[1, 1]
# 我们这里的计算结果应该是约等于，因为我们在计算的时候是使用的总体方差(总体方差和样本方差是稍微有点区别的)
covx = np.mean((x - x.mean()) ** 2)
covy = np.mean((y - y.mean()) ** 2)
print(covx)
print(covy)
# 这里计算的covxy等于上面的covxy[0, 1]和covxy[1, 0]，三者相等
covxy = np.mean((x - x.mean()) * (y - y.mean()))
print(covxy)

coefxy = np.corrcoef(x, y)
print(coefxy)
