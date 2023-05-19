import numpy as np


def main():
    """
    """
    # считываем данные из стандартного потока ввода
    n, m = map(int, input().split())
    X = np.zeros((n, m))
    y = np.zeros(n)
    for i in range(n):
        row = input().split()
        X[i, :] = [float(x) for x in row[:-1]]
        y[i] = int(row[-1])

    # инициализируем вектор весов случайным образом
    w = np.random.normal(size=m)

    # обучаем персептрон
    max_iter = 1000
    for epoch in range(max_iter):
        errors = 0
        for i in range(n):
            xi = X[i, :]
            yi = y[i]
            if yi * np.dot(w, xi) <= 0:
                w += yi * xi
                errors += 1
        if errors == 0:
            break

    # выводим вектор весов
    print(" ".join(str(x) for x in w))

if __name__ == '__main__':
	main()