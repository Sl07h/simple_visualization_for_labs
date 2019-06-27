import matplotlib.pyplot as plt # отрисовка
from matplotlib import cm # цветовая схема
import numpy

DPI = 200 # Плотность пикселей
folder = 'img/'

x_steps = [1, 2, 5, -1]
y_steps = [2, 4, 2, -1]

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
def draw2D():
    titleString = 'Двумерная функция'
    saveName = 'draw2D'
    # Рассчёт значений целевой функции на сетке и отрисовка
    x = numpy.linspace (-12, 12, 50)
    y = numpy.linspace (-12, 12, 50)
    x, y = numpy.meshgrid(x, y)
    z = f(x, y)
    plt.contourf(x, y, z, 25, cmap=cm.coolwarm)
    # Сходимость решения
    plt.plot(x_steps, y_steps, linewidth=0.8, color='orange')
    for i in range(len(x_steps)):
        plt.scatter(x_steps[i], y_steps[i], s=2, color='black')
    # Оси координат и заголовок
    plt.title(titleString, fontsize=19)
    plt.xlabel('X', fontsize=10)
    plt.ylabel('Y', fontsize=10)
    plt.xticks(numpy.linspace(-10, 10, 21))
    plt.yticks(numpy.linspace(-10, 10, 21))
    plt.tick_params(axis='both', labelsize=8)
    plt.grid(alpha=0.4)
    plt.savefig(folder + saveName + '.png', dpi=DPI)
    plt.clf()


draw2D()