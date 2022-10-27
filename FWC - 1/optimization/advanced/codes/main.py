import matplotlib.pyplot as plt
import numpy as np

#if using termux
import subprocess
import shlex
#end if

def f(x,r):
    return x*(np.sqrt(4*(r)**2-x**2))

def df(x):
    return (-x**2/(np.sqrt(4*(r)**2-x**2)))+(np.sqrt(4*(r)**2-x**2))

r=5
label_str = "$area=xy$"

#For maxima using gradient ascent
cur_x = 1
alpha = 0.001
precision = 0.000000001
previous_step_size = 1
max_iters = 100000000
iters = 100000

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x
    cur_x += alpha * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1

max_val = f(cur_x,r)
print("Maximum area is",max_val, "at","x =",cur_x)
print('y=',np.sqrt(4*(r)**2-(cur_x)**2))

#Plotting f(x)
#x=np.linspace(-1,5,100)
#y=f(x,r)
#plt.plot(x,y,label=label_str)

#Labelling points
#plt.plot(cur_x,max_val,'o')
#plt.text(cur_x, max_val,f'P({cur_x:.4f},{max_val:.4f})')

#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.grid()
#plt.legend()

#plt.savefig('/sdcard/fwc/optimization/advanced/main.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/fwc/optimization/advanced/main.pdf"))
