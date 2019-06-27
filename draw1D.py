import matplotlib.pyplot as plt # отрисовка
import numpy

DPI = 200 # Плотность пикселей
folder = 'img/'

# Целевая функция
def f(x):
    return 1.0 / x

# Отрисовка
def draw1D():
    titleString = 'Одномерная функция'
    saveName = 'draw1D'
    # Рассчёт значений целевой функции на сетке и отрисовка
    x = numpy.linspace (-12, 12, 50)
    y = f(x)
    plt.plot(x, y)
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


draw1D()