
import matplotlib.pyplot as plt

from math import *

# df/dt=G(f)
# df/dt=-rf

def big_g(r,f):
    return r*f

f=[1]
t=[0]
solution=[1]

delta_t=0.1

r=0.5

t_final=5.0

while t[-1]<=t_final:
    f_new=f[-1]+delta_t*big_g(r,f[-1])
    t_new=t[-1]+delta_t
    solution_new=exp(r*t_new)

    f.append(f_new)
    t.append(t_new)
    solution.append(solution_new)

plt.plot(t,f)
plt.plot(t,solution)
plt.show()
