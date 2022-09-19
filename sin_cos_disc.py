import numpy as np
import matplotlib.pyplot as plt

x=[]
y=[]
n=1000
turnx=420;turny=69
fig, axs = plt.subplots()
for i in range(1,n):
  a=np.cos(i+turnx)
  b=np.sin(i+turny)
  x.append(a),y.append(b)
axs.scatter(x,y)
