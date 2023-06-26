import numpy as np

def main():
    # чтение входных данных
    k_value, U_value, M_value, D_value, T_value = map(int, input().split())
    U_M_train = np.full((U_value, M_value), np.nan, dtype=np.float32)
    all_ratings = 0
    all_ratings_count = 0
    user_bias = np.zeros(U_value)
    user_bias_count = np.zeros(U_value, dtype=np.int32)
    movie_bias = np.zeros(M_value)
    moveie_bias_count = np.zeros(M_value, dtype=np.int32)
    for _ in range(D_value):
        user, movie, rating = map(int, input().split())
        rating /= k_value
        # занесение данных в матрицу
        U_M_train[user, movie] = rating
        # вычисления средних
        all_ratings += rating
        all_ratings_count += 1
        user_bias[user] += rating
        user_bias_count[user] += 1
        movie_bias[movie] += rating
        moveie_bias_count[movie] += 1

    # вычисляем среднее значение оценок
    mean_rating = all_ratings / all_ratings_count

    # получаем смещения по пользователю и фильму
    user_bias = user_bias / user_bias_count - mean_rating
    movie_bias = movie_bias / moveie_bias_count - mean_rating

    # обработка пропущенных значений
    mean_ratings = np.nanmean(U_M_train, axis=1)
    for i in range(U_value):
        if user_bias_count[i] >= 1:
            for k in range(M_value):
                if np.isnan(U_M_train[i][k]):
                    U_M_train[i][k] = mean_ratings[i]
        else:
            for k in range(M_value):
                if np.isnan(U_M_train[i][k]):
                    U_M_train[i][k] = mean_rating

    # инициализация матриц U и V
    U = np.random.rand(U_value, 10)
    V = np.random.rand(M_value, 10)

    # обучение модели SVD с регуляризацией
    learning_rate = 0.01
    lambda_reg = 0.05
    for epoch in range(100):
        for i in range(U_value):
            for j in range(M_value):
                if not np.isnan(U_M_train[i][j]):
                    prediction = np.dot(U[i], V[j].T) + mean_rating + user_bias[i] + movie_bias[j]
                    error = U_M_train[i][j] - prediction
                    # обновляем значения матриц U и V
                    U[i] += learning_rate * (error * V[j] - lambda_reg * U[i])
                    V[j] += learning_rate * (error * U[i] - lambda_reg * V[j])

    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = np.dot(U[user], V[movie].T) + mean_rating + user_bias[user] + movie_bias[movie]
        rating = min(max(rating * k_value, 0), k_value)
        print(rating)

if __name__ == '__main__':
    main()