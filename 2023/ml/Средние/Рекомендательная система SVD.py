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
    grad_U = np.zeros((U_value, min_dim))
    V = np.random.rand(M_value, min_dim)
    grad_V = np.zeros((M_value, min_dim))

    # обучение модели SVD с регуляризацией
    learning_rate = 0.1
    eps = 1e-7
    lambda_reg = 0.01
    for epoch in range(1000):
        for i, j, value in zip(U_M_train.nonzero()[0], U_M_train.nonzero()[1], U_M_train.data):
            prediction_before = np.dot(U[i], V[j].T) #+ mean_rating + user_bias[i] + movie_bias[j]
            error_before = (value - prediction_before) ** 2
            error_reg = ((U[i] ** 2).sum() + (V[j] ** 2).sum())
            error_before += lambda_reg * error_reg
            
            # вычисляем градиент функции ошибки по U[i] и V[j]
            U_for_grad = U[i]
            V_for_grad = V[j]
            for k in range(min_dim):
                U_for_grad[k] += eps
                prediction = np.dot(U_for_grad, V_for_grad.T) #+ mean_rating + user_bias[i] + movie_bias[j]
                error = (value - prediction) ** 2
                diference =  - U[i][k]**2 + U_for_grad[k]**2
                error += lambda_reg * (error_reg + diference)
                U_for_grad[k] -= eps
                grad_U[i][k] += error - error_before
                
                V_for_grad[k] += eps
                prediction = np.dot(U_for_grad, V_for_grad.T) #+ mean_rating + user_bias[i] + movie_bias[j]
                error = (value - prediction) ** 2
                diference =  - V[j][k]**2 + V_for_grad[k]**2
                error += lambda_reg * (error_reg + diference)
                V_for_grad[k] -= eps
                grad_V[j][k] += error - error_before
        if epoch % 100 == 0:
            lambda_reg /= 2  
        for i in range(U_value):
            grad_U[i] /= user_bias_count[i]
            
        for j in range(M_value):
            grad_V[j] /= moveie_bias_count[j]
        # обновляем значения матриц U и V
        U -= learning_rate * grad_U / eps 
        V -= learning_rate * grad_V / eps

    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = np.dot(U[user], V[movie].T) #+ mean_rating + user_bias[user] + movie_bias[movie]
        rating = min(max(rating * k_value, 0), k_value)
        print(rating)

if __name__ == '__main__':
    main()