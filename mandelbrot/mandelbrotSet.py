import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

N = 256
x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)
xv, yv = np.meshgrid(x, y, indexing="ij")

c = xv + 1j*y

z = np.zeros((N, N), dtype=np.complex128)
m = np.ones((N, N))

fig = plt.figure()
plt.axis('off')
im = plt.imshow(m, animated=True)


def updatefig(*args):
    global z
    z = z**2 + c
    m[np.abs(z) <= 2] = 0.0
    im.set_array(m)
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=100, frames=100, blit=True)


plt.show()
