import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 3 ** x


def integrate(x, y, n, osn):
    summ = 0
    if osn == 1:
        plt.title("Интегральная сумма для f(x)=3^x с левым оснащением \n" + "Число точек разбиения: " + str(n))
        for i in range(n):
            summ += 1 / n * f(x[i])

            plt.plot([x[i], x[i]], [0, f(x[i])], color='orange')
            plt.plot([x[i], x[i + 1]], [f(x[i]), f(x[i])], color='orange')
        plt.plot([x[-1], x[-1]], [0, f(x[-2])], color="orange")

    elif osn == 2:
        plt.title("Интегральная сумма для f(x)=3^x с центральным оснащением \n" + "Число точек разбиения: " + str(n))
        for i in range(n):
            x_i = x[i] + 1 / (2 * n)
            y_i = f(x_i)
            summ += 1 / n * y_i

            plt.plot([x[i], x[i]], [0, y_i], color='orange')
            plt.plot([x_i, x_i], [0, y_i], color='orange')
            plt.plot([x[i], x[i + 1]], [y_i, y_i], color='orange')
        plt.plot([x[-1], x[-1]], [0, f(x_i)], color="orange")

    elif osn == 3:
        plt.title("Интегральная сумма для f(x)=3^x с правым оснащением \n" + "Число точек разбиения: " + str(n))
        for i in range(n):
            x_i = x[i]
            y_i = f(x[i + 1])
            summ += 1 / n * y_i

            plt.plot([x_i, x_i], [0, y_i], color="orange")
            plt.plot([x_i, x[i + 1]], [y_i, y_i], color="orange")
        plt.plot([x[-1], x[-1]], [0, f(x[-1])], color="orange")
    else:
        print("Других вариантов оснащение нет")
    return summ


if __name__ == "__main__":

    plt.figure(figsize=(40 / 2.54, 30 / 2.54))
    while True:
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        print('Для выхода из программы нажмите "0"')
        print("Введите количество точек разбиения: ")
        n = int(input())
        if n == 0:
            print("Сеанс завершён")
            break
        print("Выберите оснащение (1 - левые, 2 - центральные, 3 - правые)")
        s = int(input())

        # make data
        x = np.linspace(1, 2, n + 1)
        y = f(x)

        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("y")

        integr_summ = integrate(x, y, n, s)
        print("Интегральная сумма: " + str(integr_summ))
        plt.show()
