import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot_surface_xy(x=0.0, y=0.0, z=0.0, length=1.0):
    rx = [x, x + length]
    ry = [y, y + length]
    X, Y = np.meshgrid(rx, ry)
    r_1 = [z, z]
    r_2 = [z + length, z + length]
    p1, _ = np.meshgrid(r_1, r_1)
    p2, _ = np.meshgrid(r_2, r_2)
    return (X, Y, p1), (X, Y, p2)


def plot_surface_yz(x=0.0, y=0.0, z=0.0, length=1.0):
    ry = [y, y + length]
    rz = [z, z + length]
    Y, Z = np.meshgrid(ry, rz)
    r_1 = [x, x]
    r_2 = [x + length, x + length]
    p1, _ = np.meshgrid(r_1, r_1)
    p2, _ = np.meshgrid(r_2, r_2)
    return (p1, Y, Z), (p2, Y, Z)


def plot_surface_xz(x=0.0, y=0.0, z=0.0, length=1.0):
    rx = [x, x + length]
    rz = [z, z + length]
    X, Z = np.meshgrid(rx, rz)
    r_1 = [y, y]
    r_2 = [y + length, y + length]
    p1, _ = np.meshgrid(r_1, r_1)
    p2, _ = np.meshgrid(r_2, r_2)

    return (X, p1, Z), (X, p2, Z)


def plot_cube(corner, length):
    x, y, z = corner[0], corner[1], corner[2]
    a, b = plot_surface_xy(x, y, z, length)
    c, d = plot_surface_yz(x, y, z, length)
    e, f = plot_surface_xz(x, y, z, length)
    return (a, b, c, d, e, f)


def grid_plotter(tree):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.grid(False)
    ax.axis("off")

    corners = [tree.fetchEndNode(i).lowerBounds() for i in range(tree.nEndNodes())]
    lengths = [
        tree.fetchEndNode(i).upperBounds()[0] - tree.fetchEndNode(i).lowerBounds()[0]
        for i in range(tree.nEndNodes())
    ]

    for i in range(tree.nEndNodes()):
        data = plot_cube(corners[i], lengths[i])
        for d in data:
            ax.plot_surface(d[0], d[1], d[2], color="purple", alpha=0.01)
