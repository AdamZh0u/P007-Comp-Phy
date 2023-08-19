import numpy as np
import matplotlib.pyplot as plt


def pg_analytic(a=10,b=3, N0 = 1000, step = 0.01):
    time = np.arange(0, 10+step, step)
    k = 1+a/(b*N0)
    for t in time:
        m = k*np.exp(-b*t)
        l =  (-a/b)
        N =  l/(1 - m)
    return N

fig,ax = plt.subplots(figsize=(3.60236, 3.5), dpi=100)

t,N = pg_analytic(a=10, b=0.01, N0 = 1000, step = 0.01)
ax.scatter(t, N, s=1, marker='.', label = 'A')


ax.legend(frameon=False)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Number of Nuclei (N)")
ax.set_title("Two-State System")