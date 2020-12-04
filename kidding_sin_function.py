import math
import random
from matplotlib import pyplot as plt
def sin_func():
  i=0
  wave=[]
  for _ in range (100):
    if (i<1):
      i+=0.1
    else:
      i-=0.5
    wave.append(math.sin(i))
  plt.plot(wave)
  plt.ylabel('some numbers')
  plt.show()
  print(wave)

sin_func()
