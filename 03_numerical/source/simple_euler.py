
from math import *

# df/dt=G(f)
# df/dt=-rf

def big_g(r,f):
    return r*f

f=1
t=0

delta_t=0.01

r=2.0

t_final=5.0

while t<=t_final:
    print t,f,exp(r*t)
    f=f+delta_t*big_g(r,f)
    t=t+delta_t

    
