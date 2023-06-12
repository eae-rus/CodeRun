import numpy as np

def main():
    '''
    '''
    n, m = map(int, input().split())

    # Создание матрицы T
    T = np.zeros((n, n))
    max_T = 1
    for i in range(m):
        a, b = map(int, input().split())
        if T[a-1][b-1] == 0:
            T[a-1][b-1] = 1
        else:
            T[a-1][b-1] += 1
            if T[a-1][b-1] > max_T:
                max_T = T[a-1][b-1]
    
    # корректируем амплитуду
    T = T / max_T
    
    # Инициализация вектора p
    p = np.ones((n, 1)) / n

    # Параметры алгоритма PageRank
    d = 0.99  # Коэффициент затухания
    eps = 1e-6  # Порог сходимости

    # Алгоритм PageRank
    while True:
        p_new = (1 - d) / n + d * (T @ p + (1 - d) / n * np.ones((n, 1)))
        if np.linalg.norm(p_new - p) < eps:
            break
        p = p_new

    # Вывод порядковых номеров объектов, отсортированных по убыванию значений вектора p
    order = np.argsort(-p.flatten())
    for i in order:
        print(i+1)
    


if __name__ == '__main__':
	main()