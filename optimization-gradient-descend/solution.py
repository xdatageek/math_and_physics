import pandas as pd
import numpy as np
import copy

def get_cp(c):
    cp = np.zeros_like(c,dtype=float)
    for i in range(1,len(c)):
        cp[i] = c[i] - c[i-1]
    return cp

def goal(c):
    cp = get_cp(c)
    z = np.zeros_like(c,dtype=float)
    W = np.zeros_like(c,dtype=float)

    for i in range(len(t)):
        z[i] = D[i] + min(0,cp[i])
        W[i] = P[i] * (max(z[i],0) + max(cp[i],0))
    return np.sum(W) + 0.2 * np.max(z) + 0.05 * np.max(c)

def gradient(c,step=1):
    grad = np.zeros_like(c,dtype=float)
    for i in range(len(c)):
        cnew = copy.deepcopy(c)
        cnew[i] += step
        grad[i] = (goal(cnew) - goal(c)) / step
    return grad

df = pd.read_csv('data.csv')
t = df['time'].values
D = df['demand'].values
P = df['price'].values

# init c profile
c = np.zeros_like(t)
c[:14] = np.sin(np.linspace(0,np.pi,num=14,endpoint=True)) * 8000

# gradient descend
step=1; rate=10; steps=6000
for i in range(steps):
    cnew = np.clip(c - gradient(c,step=step) * rate,0,1.2e4)
    
    if i % 600 == 0:
        print('goal = {}'.format(goal(cnew)))
    c = cnew
    
    cp = get_cp(c)
    if np.max(cp)>1.2e4 or np.min(cp)<-8.e3 or np.min(c) < 0:
        break

 # updata cp, z profiles
cp = get_cp(c)

z = np.zeros_like(cp)
for i in range(len(t)):
    z[i] = D[i] + min(0,cp[i])
    
