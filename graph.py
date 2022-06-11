import matplotlib.pyplot as plt
import math

x = list(range(0,100,1))
y = list(map(lambda a:math.sin(0.1*a)*math.sin(0.1*a),x))

p1 = plt.plot(x,y,'bo-',label='y=sin(x)')

plt.legend()
plt.xlabel('values of x')
plt.ylabel('values 0f sin(a)')
plt.title('my first plot in python')
