x=[1]

n=int(input())
i=0
y=[n]
while(n!=1):
  if(n%2==0):
    n/=2
  else:
   n=3*n+1
  i+=1
  x.append(i+1)
  y.append(n)  
 
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.xlabel("steps")
plt.ylabel("value")
plt.title("Collatz Conjecture")
plt.show()
