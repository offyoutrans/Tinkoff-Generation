# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import sympy as sy
import numpy as np
import matplotlib

# %%
x = sy.Symbol('x')
y = sy.Symbol('y')

# %% [markdown]
f = x^4
# %%
f = x**4+2*x**2*y+10*x**2+6*x*y+10*y**2-6*x+4


# %%
f


# %%
dx = sy.Derivative(f, x).doit()


# %%
dx


# %%
dy = sy.Derivative(f, y).doit()


# %%
dy


# %%
res = sy.solve(dy, y)


# %%
res[0]


# %%
res


# %%
dx.replace(y, res[0])


# %%
el = sy.simplify(dx.replace(y, res[0]))


# %%
el


# %%
res1 = sy.solve(el, x)


# %%
res1[0]


# %%
res1[1]


# %%
res1
# %%
def f(x, y):
    return x**4+2*x**2*y+10*x**2+6*x*y+10*y**2-6*x+4