import numpy as np


class SVD:
    def __init__(self, n_factors=10, n_epochs=20, lr=0.005, reg=0.02, k_max=10):
        self.n_factors = n_factors  # число скрытых факторов
        self.n_epochs = n_epochs  # число эпох обучения
        self.lr = lr  # скорость обучения
        self.reg = reg  # коэффициент регуляризации
        self.k_max = k_max  # максимальная оценка

    def fit(self, X, n_users, n_items):
        self.mean = np.mean(X[:, 2]) / self.k_max  # среднее значение оценок
        self.user_ids, self.item_ids = np.arange(n_users), np.arange(n_items)
        self.n_users, self.n_items = n_users, n_items

        # инициализируем веса
        self.b_u = np.zeros(self.n_users)
        self.b_i = np.zeros(self.n_items)
        self.q_i = np.random.normal(scale=1. / self.n_factors, size=(self.n_items, self.n_factors))
        self.p_u = np.random.normal(scale=1. / self.n_factors, size=(self.n_users, self.n_factors))

        # обучение
        for epoch in range(self.n_epochs):
            for u, i, r in X:
                # обновляем веса
                dot = np.dot(self.q_i[i], self.p_u[u])
                err = r / self.k_max - (self.mean + self.b_u[u] + self.b_i[i] + dot)
                self.b_u[u] += self.lr * (err - self.reg * self.b_u[u])
                self.b_i[i] += self.lr * (err - self.reg * self.b_i[i])
                self.p_u[u, :] += self.lr * (err * self.q_i[i] - self.reg * self.p_u[u, :])
                self.q_i[i, :] += self.lr * (err * self.p_u[u] - self.reg * self.q_i[i, :])
                
    def predict(self, u, i):
        dot = np.dot(self.q_i[i], self.p_u[u])
        pred_rating = self.k_max * (self.mean + self.b_u[u] + self.b_i[i] + dot)
        pred_rating = pred_rating if pred_rating <= self.k_max else self.k_max
        pred_rating = pred_rating if pred_rating >= 0 else 0
        return pred_rating

def main():
    # чтение входных данных
    k_value, U_value, M_value, D_value, T_value = map(int, input().split())
    # TODO: Подумать о реализации разреженной матрицы
    U_M_train = np.full((D_value, 3), np.nan, dtype=np.int32)
    for i in range(D_value):
        user, movie, rating = map(int, input().split())
        rating
        # занесение данных в матрицу
        U_M_train[i, 0] = user
        U_M_train[i, 1] = movie
        U_M_train[i, 2] = rating
    
    min_dim = 10
    if U_value <= 10 or M_value <= 10:
        min_dim = min(U_value, M_value) - 1
    
    svd = SVD(n_factors=min_dim, lr=0.05, reg=0.1, n_epochs=50, k_max=k_value)
    
    svd.fit(U_M_train, U_value, M_value)

    
    # вычисление предсказаний и вывод результатов
    for _ in range(T_value):
        user, movie = map(int, input().split())
        rating = svd.predict(user, movie)
        print(rating)


if __name__ == '__main__':
    main()