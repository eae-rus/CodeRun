import numpy as np
from scipy.sparse import csr_matrix

def main():
    # чтение входных данных
    k_value, U_value, M_value, D_value, T_value = map(int, input().split())
    
    U_M_train = np.zeros((U_value, M_value))
    all_ratings = 0
    all_ratings_count = 0
    for _ in range(D_value):
        user, movie, rating = map(int, input().split())
        rating /= k_value
        # занесение данных в матрицу
        U_M_train[user, movie] = rating
        # вычисления средних
        all_ratings += rating
        all_ratings_count += 1

    # вычисляем среднее значение оценок
    # mean_rating = all_ratings / all_ratings_count
    mean_rating = 0
    
    # ДОБАВИТЬ КОРРЕКТИРОВКУ U_M_train
    # for user, movie in zip(*U_M_train.nonzero()):
    #     U_M_train[user, movie] -= (mean_rating)
    
    min_dim = 10
    # if U_value <= 10 or M_value <= 10:
    #     min_dim = min(U_value, M_value) - 1
    
    # задаем зерно для генератора случайных чисел
    np.random.seed(42)
    
    # инициализация матриц U и V
    P = np.random.normal(scale=1./min_dim, size=(U_value, min_dim)) # - 0.5/min_dim
    Q = np.random.normal(scale=1./min_dim, size=(M_value, min_dim)) # - 0.5/min_dim

    user_bias = np.zeros(U_value)
    movie_bias = np.zeros(M_value)
    
    # обучение модели SVD с регуляризацией
    learning_rate  = 0.5
    reg_param  = 0.02
    for epoch in range(200):
        for user in range(U_value):
            for movie in range(M_value):
                value = U_M_train[user, movie]
                if value > 0:
                    prediction = mean_rating + user_bias[user] + movie_bias[movie] + np.dot(P[user, :], Q[movie, :])
                    error = (value - prediction)
                    
                    user_bias[user] += learning_rate  * (error - reg_param  * user_bias[user])
                    movie_bias[movie] += learning_rate  * (error - reg_param  * movie_bias[movie])
                    P[user, :] += learning_rate  * (error * Q[movie, :] - reg_param  * P[user, :])
                    Q[movie, :] += learning_rate  * (error * P[user, :] - reg_param  * Q[movie, :])

    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = k_value * (mean_rating + user_bias[user] + movie_bias[movie] + np.dot(P[user, :], Q[movie, :]))
        rating = min(max(rating, 0), k_value)
        print(rating)

if __name__ == '__main__':
    main()