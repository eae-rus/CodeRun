import numpy as np
from scipy.sparse import csr_matrix

def main():
    # чтение входных данных
    k_value, U_value, M_value, D_value, T_value = map(int, input().split())
    
    U_M_train = np.zeros((U_value, M_value))
    user_movie_array = []
    for _ in range(D_value):
        user, movie, rating = map(int, input().split())
        rating /= k_value
        # занесение данных в матрицу
        U_M_train[user, movie] = rating
        user_movie_array.append((user, movie))
    
    min_dim = 10
    
    # задаем зерно для генератора случайных чисел
    np.random.seed(42)
    
    # инициализация матриц U и V
    P = np.random.normal(scale=1./min_dim, size=(U_value, min_dim))
    Q = np.random.normal(scale=1./min_dim, size=(M_value, min_dim))

    user_bias = np.zeros(U_value)
    movie_bias = np.zeros(M_value)
    
    # обучение модели SVD с регуляризацией
    learning_rate  = 0.1
    reg_param  = 0.05
    for epoch in range(9):
        for index in range(len(user_movie_array)):
            user, movie = user_movie_array[index]
            value = U_M_train[user, movie]
            prediction = user_bias[user] + movie_bias[movie] + np.dot(P[user].T, Q[movie])
            error = (value - prediction)
            
            user_bias[user] += learning_rate  * (error - reg_param  * user_bias[user])
            movie_bias[movie] += learning_rate  * (error - reg_param  * movie_bias[movie])
            P[user] += learning_rate  * (error * Q[movie] - reg_param  * P[user])
            Q[movie] += learning_rate  * (error * P[user] - reg_param  * Q[movie])

    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = k_value * (user_bias[user] + movie_bias[movie] + np.dot(P[user].T, Q[movie]))
        rating = min(max(rating, 0), k_value)
        print(rating)

if __name__ == '__main__':
    main()