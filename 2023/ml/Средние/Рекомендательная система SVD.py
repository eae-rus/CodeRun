import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds

def main():
    def predict_rating(user_id, movie_id):
        # получаем вектор пользователя
        user_vector = U[user_id, :].reshape(1, -1)

        # получаем вектор фильма
        movie_vector = V[:, movie_id].reshape(-1, 1)

        # вычисляем предсказанную оценку
        predicted_rating = user_vector.dot(movie_vector)[0, 0]
        predicted_rating += mean_rating
        predicted_rating += user_bias[user_id] + movie_bias[movie_id]
        # predicted_rating = mean_rating + user_bias[user_id] + movie_bias[movie_id] + user_vector.dot(movie_vector)[0, 0]
        # predicted_rating = mean_rating + user_vector.dot(movie_vector)[0, 0]

        if predicted_rating > k_value:
            return k_value
        elif predicted_rating < 0:
            return 0
        else:
            return predicted_rating

    k_value, U_value, M_value, D_value, T_value = map(int, input().split())
    U_M_train = pd.DataFrame(np.nan, index=range(U_value), columns=range(M_value))
    for _ in range(D_value):
        user, movie, rating = map(int, input().split())
        U_M_train.iloc[user, movie] = rating

    # обработка пропущенных значений
    mean_ratings = np.nanmean(U_M_train, axis=0)
    filled_ratings = np.where(np.isnan(U_M_train), mean_ratings, U_M_train)

    # вычисляем среднее значение оценок
    mean_rating = np.nanmean(filled_ratings)

    # выполняем SVD разложение
    min_dim = 10
    if U_value <= 10 or M_value <= 10:
        min_dim = min(U_value, M_value)-1
    U, sigma, V = svds(filled_ratings - mean_rating, k=min_dim)

    # получаем смещения по пользователю и фильму
    user_bias = filled_ratings.mean(axis=1) - mean_rating
    movie_bias = filled_ratings.mean(axis=0) - mean_rating

    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = predict_rating(user, movie)
        print(rating)


if __name__ == '__main__':
    main()