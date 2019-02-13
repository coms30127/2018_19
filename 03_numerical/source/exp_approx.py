
from math import *
import matplotlib.pyplot as plt


# here we use a class with an overloaded __call__ operator to define the
# functions, a more elegant and pasimonious approach is to use
# a function to define the functions, this is shown in the
# programme less_simple_euler.py

class F:

    def __init__(self,r):
        self.r=r

    def __call__(self,t):
        return exp(self.r*t)

class Dfdt:

    def __init__(self,r):
        self.r=r

    def __call__(self,f):
        return self.r*f


def euler_increment(dfdt,f,delta_t):
    return dfdt(f)*delta_t

def rk_increment(dfdt,f,delta_t):
    k1=dfdt(f)
    k2=dfdt(f+0.5*delta_t*k1)
    k3=dfdt(f+0.5*delta_t*k2)
    k4=dfdt(f+delta_t*k3)

    return (k1+2*k2+2*k3+k4)*delta_t/6


r=0.5

f=F(r)
dfdt=Dfdt(r)

t_final=5.0

delta_t=0.2

f_euler=1.0
f_rk=1.0

t=[0]
f_euler=[1.0]
f_rk=[1.0]
f_v=[f(t[-1])]

while t[-1]<t_final:

    f_euler.append(f_euler[-1]+euler_increment(dfdt,f_euler[-1],delta_t))
    f_rk.append(f_rk[-1]+rk_increment(dfdt,f_rk[-1],delta_t))
    t.append(t[-1]+delta_t)
    f_v.append(f(t[-1]))


plt.plot(t,f_euler)
plt.plot(t,f_rk)
plt.plot(t,f_v)
plt.show()


