#%%
%matplotlib widget
#%%
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plot3d
Axes3D = plot3d.Axes3D
import numpy as np
import sympy as sy
def f(x, y):
    return x**4+2*x**2*y+10*x**2+6*x*y+10*y**2-6*x+4
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs = np.linspace(-10, 10, 100)
ys = np.linspace(-10, 10, 100)
ax.plot(xs, ys, f(xs, ys))