import numpy as np
from scipy.sparse.linalg import svds

def main():
    def predict_rating(user_id, movie_id):
        # получаем вектор пользователя
        
        user_vector = np.multiply(U[user_id, :], sigma.T)

        # получаем вектор фильма
        movie_vector = V[:, movie_id]

        # вычисляем предсказанную оценку
        predicted_rating = user_vector.dot(movie_vector)
        predicted_rating += mean_rating
        predicted_rating += user_bias[user_id] + movie_bias[movie_id]

        if predicted_rating > k_value:
            return k_value
        elif predicted_rating < 0:
            return 0
        else:
            return predicted_rating

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
        for k in range(M_value):
            if np.isnan(U_M_train[i][k]):
                U_M_train[i][k] = mean_ratings[i]

    # выполняем SVD разложение
    min_dim = 10
    if U_value <= 10 or M_value <= 10:
        min_dim = min(U_value, M_value) - 1
    U, sigma, V = svds(U_M_train - mean_rating, k=min_dim)

    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = predict_rating(user, movie)
        print(rating)


if __name__ == '__main__':
    main()