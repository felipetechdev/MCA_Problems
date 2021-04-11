import numpy as np
from matplotlib import pyplot as plt

x0=1
y0=20
xf=100
n=10001
dx=(xf-x0)/(n-1)
x=np.linspace(x0, xf, n)
y=np.zeros([n])
y[0]=y0
for i in range(1,n):
    y[i] = dx*(-3*y[i-1]/x[i-1]+0.2*x[i-1]*np.sin(x[i-1]))+y[i-1]
plt.plot(x,y,'o')