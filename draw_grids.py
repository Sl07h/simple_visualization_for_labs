import matplotlib.pyplot as plt # отрисовка
from matplotlib import cm # цветовая схема
import numpy as np

DPI = 200 # Плотность пикселей
folder = 'img/'


# Отрисовка
def draw_grid(name, int_nodes_file, ext_nodes_file):
    # считывание внутренних и внешних точек сетки
    x, y = np.loadtxt('grids/' + int_nodes_file, unpack=True)
    plt.scatter(x, y, s=4, marker='s', color='grey')
    x, y = np.loadtxt('grids/' + ext_nodes_file, unpack=True)
    plt.scatter(x, y, s=4, marker='s', color='black')
    # Оси координат и заголовок
    plt.title(name, fontsize=19)
    plt.xlabel('X', fontsize=10)
    plt.ylabel('Y', fontsize=10)
    plt.tick_params(axis='both', labelsize=8)
    plt.grid(alpha=0.4)
    plt.savefig(folder + name + '.png', dpi=DPI)
    plt.clf()


draw_grid('Uniform0', 'Uniform_0.txt', 'BorderUniform_0.txt')
draw_grid('Uniform3', 'Uniform_3.txt', 'BorderUniform_3.txt')

draw_grid('NonUniform0', 'NonUniform_0.txt', 'BorderNonUniform_0.txt')
draw_grid('NonUniform3', 'NonUniform_3.txt', 'BorderNonUniform_3.txt')