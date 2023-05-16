import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
from sklearn.decomposition import TruncatedSVD


def main():
    k_value, U_value, M_value, D_value, T_value = map(int, input().split())
    U_M_train = pd.DataFrame(np.nan, index=range(U_value), columns=range(M_value))
    for _ in range(D_value):
        user, movie, raiting = map(int, input().split())
        U_M_train.iloc[user,movie] = raiting
        
    # вычисляем среднее значение оценок
    mean_rating = U_M_train.mean().mean()

    # создаем объект SVD
    svd = TruncatedSVD(n_components=10)
    
    # выполняем SVD разложение
    svd.fit(U_M_train - mean_rating)
    
    # получаем смещения по пользователю и фильму
    user_bias = U_M_train.mean(axis=1) - mean_rating
    movie_bias = U_M_train.mean(axis=0) - mean_rating
    
    for _ in range(T_value):
        user, movie = map(int, input().split())
        raiting = predict_rating(user, movie)
        print(raiting)
    
    def predict_rating(user_id, movie_id):
        # получаем вектор пользователя
        user_vector = svd.transform(U_M_train.loc[user_id].values.reshape(1, -1) - mean_rating)
    
        # получаем вектор фильма
        movie_vector = svd.components_.T[movie_id]
    
        # вычисляем предсказанную оценку
        predicted_rating = mean_rating + user_bias[user_id] + movie_bias[movie_id] + user_vector.dot(movie_vector)
    
        return predicted_rating


if __name__ == '__main__':
	main()