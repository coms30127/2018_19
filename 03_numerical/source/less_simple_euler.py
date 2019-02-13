
import matplotlib.pyplot as plt

from math import *

# df/dt=G(f)
# df/dt=-rf


# the simple version has the virtue of being simple but
# from a mathematical point of view it is annoying
# because you have to write big_g(r,f) where r is a
# parameter, something that defines the function
# whereas f is the variable, the thing that the function
# is a function of
# in this version a function is used to make the big_g function
# so when define_big_g defines big_g the value of r is used in the
# definition

def define_big_g(r):

    def big_g(f):
        return r*f

    return big_g

    
f=[1]
t=[0]
solution=[1]

delta_t=0.1

r=0.5

big_g=define_big_g(r)

t_final=5.0

while t[-1]<=t_final:
    f_new=f[-1]+delta_t*big_g(f[-1])
    t_new=t[-1]+delta_t
    solution_new=exp(r*t_new)

    f.append(f_new)
    t.append(t_new)
    solution.append(solution_new)

plt.plot(t,f)
plt.plot(t,solution)
plt.show()
