from mpl_toolkits.mplot3d import Axes3D # отрисовка в 3D
import matplotlib.pyplot as plt # отрисовка
from matplotlib import cm # цветовая схема
import numpy

DPI = 200 # Плотность пикселей
folder = 'img/'

# Целевая функция
def f(x, y):
    C = [1, 2, 10, 5, 7, 9]
    a = [0, 0, 3, -7, 6, 6]
    b = [-1, -4, -2, -6, -10, 1]
    result = 0
    for i in range(6):
        result += C[i] / (1 + (x-a[i])**2 + (y-b[i])**2)
    return result

# Отрисовка
def draw3D():
    titleString = 'Трёхмерная функция'
    saveName = 'draw3D'
    # Рассчёт значений целевой функции на сетке и отрисовка
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = numpy.linspace (-12, 12, 50)
    y = numpy.linspace (-12, 12, 50)
    x, y = numpy.meshgrid(x, y)
    z = f(x, y)
    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, antialiased=True)
    # Оси координат и заголовок
    plt.colorbar(surf, shrink=0.5, aspect=5)
    plt.title(titleString, fontsize=19)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(alpha=0.4)
    plt.savefig(folder + saveName + '.png', dpi=DPI)
    plt.clf()


draw3D()