import random

def main():
    # чтение входных данных
    k_value, U_value, M_value, D_value, T_value = map(int, input().split())

    U_M_train = []
    for _ in range(D_value):
        user, movie, rating = map(int, input().split())
        rating /= k_value
        # занесение данных в матрицу
        U_M_train.append((user, movie, rating))

    min_dim = 10

    # задаем зерно для генератора случайных чисел
    random.seed(42)

    # инициализация матриц U и V
    P = [[random.normalvariate(0, 1./min_dim) for _ in range(min_dim)] for _ in range(U_value)]
    Q = [[random.normalvariate(0, 1./min_dim) for _ in range(min_dim)] for _ in range(M_value)]

    user_bias = [0] * U_value
    movie_bias = [0] * M_value

    # обучение модели SVD с регуляризацией
    learning_rate  = 0.6
    reg_param  = 0.2
    for epoch in range(33):
        for index in range(D_value):
            user, movie, value = U_M_train[index]
            prediction = user_bias[user] + movie_bias[movie] + dot_product(P[user], Q[movie])
            error = (value - prediction)

            user_bias[user] += learning_rate  * (error - reg_param  * user_bias[user])
            movie_bias[movie] += learning_rate  * (error - reg_param  * movie_bias[movie])
            update_vector(P[user], [learning_rate * (error * Q[movie][i] - reg_param * P[user][i]) for i in range(min_dim)])
            update_vector(Q[movie], [learning_rate * (error * P[user][i] - reg_param * Q[movie][i]) for i in range(min_dim)])
        if epoch % 10 == 0:
            learning_rate = learning_rate / 2

    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = k_value * (user_bias[user] + movie_bias[movie] + dot_product(P[user], Q[movie]))
        rating = min(max(rating, 0), k_value)
        print(rating)

def dot_product(vector1, vector2):
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

def update_vector(vector, updates):
    for i, update in enumerate(updates):
        vector[i] += update

if __name__ == '__main__':
    main()