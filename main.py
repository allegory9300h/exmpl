import math

# !!! Импортируем один из пакетов Matplotlib
import pylab

# !!! Импортируем пакет со вспомогательными функциями

# Будем рисовать график этой функции
def func (x):
    """
    sinc (x)
    """
    if x == 0:
        return 1.0
    return math.sin (x) / x

# Интервал изменения переменной по оси X
xmin = -20.0
xmax = 20.0

# Шаг между точками
dx = 0.01

# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = [50,60,65,70,80,87,90,100]

# Вычислим значение функции в заданных точках
ylist = [106.6668,118.52,123.26,127.212,126.422,123.735,120.89,110.619]
pylab.xlabel('a-размер щели')
pylab.ylabel('F-')
#pylab.text(42,28.2, u"I-Насыщености(максимальное значение) ")

# !!! Нарисуем одномерный график
pylab.plot (xlist, ylist)

pylab.show()
