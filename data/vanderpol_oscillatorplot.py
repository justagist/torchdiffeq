import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def vdp1(y,t,mu=-0.1):
    y2 = y[1]
    y1 = y[0]

    return np.array([y2, (mu-y1**2)*y2-y1])

def vdp2(y,t,mu=0.1):
    y2 = y[1]
    y1 = y[0]

    return np.array([y2, (mu-y1**2)*y2-y1])

# def exp_s(y,t,mu=1):
#     y2 = y[1]
#     y1 = y[0]

#     return np.array([y2, (mu-y1**2)*y2-y1])



steps = 20

s1 = np.linspace(-0.2,0.2,steps)
s2 = np.linspace(-0.2,0.2,steps)

x,y = np.meshgrid(s1,s2)

u = np.zeros_like(x)
v = np.zeros_like(x)

# print x.size
# print x
flattened_x = x.flatten('F')
flattened_y = y.flatten('F')

plt.ion()
# for i in range(x.size):

#     y_sol = odeint(vdp1,np.array([flattened_x[i],flattened_y[i]]),np.linspace(0,20))

#     # plt.quiver(y_sol[:,0],y_sol[:,1], np.gradient(y_sol[:,0]), np.gradient(y_sol[:,1]), width = 0.0005, headwidth = 3, color = 'r')
#     plt.plot(y_sol[:,0],y_sol[:,1])
#     plt.pause(0.00001)
#     plt.draw()

# raw_input()

x0 = 0.2
y0 = 0

switch_spiral_count= 150
spiral_in = True
spiral_in_count = 0
spiral_out_count = 0

while True:

    if spiral_in:

        spiral_in_count += 1

        y_sol = odeint(vdp1,np.array([x0, y0]),np.linspace(0,20))

        x1 = x0 + np.gradient(y_sol[:,0])[0]
        y1 = y0 + np.gradient(y_sol[:,1])[0]

    else:

        spiral_out_count += 1

        y_sol = odeint(vdp2,np.array([x0, y0]),np.linspace(0,20))

        x1 = x0 + np.gradient(y_sol[:,0])[0]
        y1 = y0 + np.gradient(y_sol[:,1])[0]


    plt.plot([x0,x1],[y0, y1])
    plt.pause(0.00001)
    plt.draw()

    if (spiral_in_count == 150) and spiral_in:
        spiral_in = False
        spiral_in_count = 0

    if (spiral_out_count == 150) and not spiral_in:
        spiral_in = True
        spiral_out_count = 0

    x0 = x1
    y0 = y1

raw_input()

