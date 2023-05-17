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
    U_M_train = np.full((U_value, M_value), np.nan)
    U_M_train = np.full((U_value, M_value), np.nan, dtype=np.float32)
    for _ in range(D_value):
        user, movie, rating = map(int, input().split())
        U_M_train[user, movie] = rating

    # вычисляем среднее значение оценок
    mean_rating = np.nanmean(U_M_train)

    # получаем смещения по пользователю и фильму
    user_bias = np.nanmean(U_M_train, axis=1) - mean_rating
    movie_bias = np.nanmean(U_M_train, axis=0) - mean_rating

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
    # P = U.dot(np.diag(sigma))

    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = predict_rating(user, movie)
        print(rating)


if __name__ == '__main__':
    main()