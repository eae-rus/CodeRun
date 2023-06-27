import numpy as np
from scipy.sparse import csr_matrix

def main():
    # чтение входных данных
    k_value, U_value, M_value, D_value, T_value = map(int, input().split())
    
    U_M_train = csr_matrix((U_value, M_value), dtype=np.float32)
    # all_ratings = 0
    # all_ratings_count = 0
    # user_bias = np.zeros(U_value)
    user_bias_count = np.zeros(U_value, dtype=np.int32)
    # movie_bias = np.zeros(M_value)
    moveie_bias_count = np.zeros(M_value, dtype=np.int32)
    for _ in range(D_value):
        user, movie, rating = map(int, input().split())
        rating /= k_value
        # занесение данных в матрицу
        U_M_train[user, movie] = rating
        # вычисления средних
        # all_ratings += rating
        # all_ratings_count += 1
        # user_bias[user] += rating
        user_bias_count[user] += 1
        # movie_bias[movie] += rating
        moveie_bias_count[movie] += 1

    # вычисляем среднее значение оценок
    # mean_rating = all_ratings / all_ratings_count

    # получаем смещения по пользователю и фильму
    # user_bias = user_bias / user_bias_count - mean_rating
    # movie_bias = movie_bias / moveie_bias_count - mean_rating
    
    # !!!!!!!!!!!!!!!
    # ДОБАВИТЬ КОРРЕКТИРОВКУ U_M_train
    # for i, j in zip(*U_M_train.nonzero()):
    #     U_M_train[i, j] -= (mean_rating + user_bias[i] + movie_bias[j])
    
    min_dim = 10
    if U_value <= 10 or M_value <= 10:
        min_dim = min(U_value, M_value) - 1
    
    # задаем зерно для генератора случайных чисел
    np.random.seed(42)
    
    # инициализация матриц U и V
    U = np.random.rand(U_value, min_dim)
    V = np.random.rand(M_value, min_dim)

    # обучение модели SVD с регуляризацией
    alpha = 0.01
    betta = 0.02
    for epoch in range(100):
        for i, j, value in zip(U_M_train.nonzero()[0], U_M_train.nonzero()[1], U_M_train.data):
            prediction = np.dot(U[i], V[j].T) #+ mean_rating + user_bias[i] + movie_bias[j]
            error = (value - prediction)

            for k in range(min_dim):
                U[i][k] += alpha * (2* error * V[j][k] - betta * U[i][k])
                V[j][k] += alpha * (2* error * U[i][k] - betta * V[j][k])

    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = np.dot(U[user], V[movie].T) #+ mean_rating + user_bias[user] + movie_bias[movie]
        rating = min(max(rating * k_value, 0), k_value)
        print(rating)

if __name__ == '__main__':
    main()