import numpy as np

def main():
    # чтение входных данных
    k_value, U_value, M_value, D_value, T_value = map(int, input().split())

    U_M_train = []
    all_ratings = 0
    for _ in range(D_value):
        user, movie, rating = map(int, input().split())
        rating /= k_value
        # занесение данных в матрицу
        U_M_train.append((user, movie, rating))
        # вычисления средних
        all_ratings += rating

    # вычисляем среднее значение оценок
    mean_rating = all_ratings / D_value

    if U_value < 5:
        min_dim = 10
        n_epoch  = 1000
    else:
        min_dim = 20
        n_epoch = 10
        
    # задаем зерно для генератора случайных чисел
    np.random.seed(42)

    # инициализация матриц U и V
    P = np.random.normal(scale=1./min_dim, size=(U_value, min_dim))
    Q = np.random.normal(scale=1./min_dim, size=(M_value, min_dim))

    user_bias = np.zeros(U_value)
    movie_bias = np.zeros(M_value)

    # обучение модели SVD с регуляризацией
    learning_rate  = 0.01
    reg_param  = 0.02
    for epoch in range(n_epoch):
        for user, movie, value in U_M_train:
            prediction = mean_rating + user_bias[user] + movie_bias[movie] + np.dot(P[user].T, Q[movie])
            error = (value - prediction)
            
            user_bias[user] += learning_rate  * (error - reg_param  * user_bias[user])
            movie_bias[movie] += learning_rate  * (error - reg_param  * movie_bias[movie])
            P[user] += learning_rate  * (error * Q[movie] - reg_param  * P[user])
            Q[movie] += learning_rate  * (error * P[user] - reg_param  * Q[movie])

    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = k_value * (mean_rating + user_bias[user] + movie_bias[movie] + np.dot(P[user].T, Q[movie]))
        rating = min(max(rating, 0), k_value)
        print(rating)


if __name__ == '__main__':
    main()