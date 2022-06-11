def gauss(x1, y1, x0, y0, sd):
    r = math.sqrt((x1-x0)**2 + (y1-y0)**2);
    return math.exp(-(r/sd)**2)

import matplotlib.pyplot as plt
import numpy as np
import math
x = list(map( lambda a:a*0.2, list(range(0,50,1))))
y = x[:]
z = np.zeros([50,50])

for i in range(0,50,1):
    for j in range(0,50,1): 
        z[i,j] =  1.2*gauss(x[i], y[j], 2.5, 2.5, 3) +  0.8*gauss(x[i], y[j], 7.5, 7.5, 3)

plt.contourf(x,y,z,10)
plt.colorbar()
plt.xlabel('Distance along x')
plt.ylabel('Distance along y')
plt.title('Guassian function')
