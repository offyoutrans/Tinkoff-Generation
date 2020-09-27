# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
r = np.random.choice


# %%
p = np.linspace(0, .75, 1000)
exp_mean = np.zeros(size=p.size)
values = np.array([0, 1])


# %%
def attm(p):
    c = np.array([1])
    el = 1
    while el:
        el=r(a = values, size = 1, p = np.array([1-p, p]))
        c+=1
    return c


# %%
def experiment(n):
    results = np.zeros(size=p.size)
    for i in range(len(p)):
        data = np.zeros(size=1000)
        for j in range(1000):
            data[j] = attm(p[i])
        results[j] = data.mean()


