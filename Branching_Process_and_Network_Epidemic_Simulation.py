from scipy.stats import binom
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

simulations = 1000
total_N = []
G = 100

for times in range(simulations):
    N = []
    R = 0.95
    N.append(1)
    for g in range(G-1):
        if int(N[g]) == 0:
            break
        N.append(0)
        for i in range(int(N[g])):
            dist_2 = poisson(R)
            y = dist_2.rvs()
            N[g+1] += y
    plt.plot(N)
    total_N.append(sum(N))
print(sum(total_N) / simulations)
plt.show()

r_sum = 1/(1-0.95)
print(r_sum)

N = 100
m = np.zeros([100,100])
m[1,0] = 1
m[0,1] = 1
node_list = []

for i in range(1,N):
    deg = np.sum(m, axis=1)
    p = deg / np.sum(deg)
    rand = np.random.choice(N, p=p)
    m[rand, i] = 1
    m[i, rand] = 1
    
G = nx.from_numpy_matrix(m)
nx.draw(G)
plt.show()

plt.hist(list(dict(G.degree()).values()))
plt.show()