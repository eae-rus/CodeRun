import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD

def main():
    def predict_rating(user_id, movie_id):
        # получаем вектор пользователя
        user_vector = svd.transform(filled_ratings[user_id].reshape(1, -1) - mean_rating)

        # получаем вектор фильма
        movie_vector = svd.components_.T[movie_id]

        # вычисляем предсказанную оценку
        predicted_rating = mean_rating + user_bias[user_id] + movie_bias[movie_id] + user_vector.dot(movie_vector)
        
        if predicted_rating[0] > k_value:
            return k_value
        elif predicted_rating[0] < 0:
            return 0
        else:
            return predicted_rating[0]
    
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

    # создаем объект SVD
    svd = TruncatedSVD(n_components=3, random_state=42)

    # выполняем SVD разложение
    svd.fit(filled_ratings - mean_rating)

    # получаем смещения по пользователю и фильму
    user_bias = filled_ratings.mean(axis=1) - mean_rating
    movie_bias = filled_ratings.mean(axis=0) - mean_rating

    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = predict_rating(user, movie)
        print(rating)




if __name__ == '__main__':
    main()
