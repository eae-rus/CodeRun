import numpy as np
from sklearn.preprocessing import PolynomialFeatures


def main():
    '''
    '''
    train_data = np.empty((1000, 6))
    test_data = np.empty((1000, 5))
    
    for i in range(1000):
        train_data[i, :] = np.array(list(map(float, input().split('\t'))))
    
    for i in range(1000):
        test_data[i, :] = np.array(list(map(float, input().split('\t'))))
    
    # Разделение данных на признаки и целевую переменную
    X_train = train_data[:, :5]
    y_train = train_data[:, 5]
    X_test = test_data[:, :5]
    #y_test = test_data[:, 5]
    
    # Создание полиномиальных признаков
    poly = PolynomialFeatures(degree=2)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    # Решение задачи с помощью полиномиальной регрессии
    XTX = np.dot(X_train_poly.T, X_train_poly)
    XTy = np.dot(X_train_poly.T, y_train)
    if np.linalg.det(XTX) == 0:
        print("Матрица XTX вырождена!")
        return
    w = np.linalg.solve(XTX, XTy)
    
    # Предсказание значений на тестовых данных
    y_pred = np.dot(X_test_poly, w)
    
    for y in y_pred:
        print(y)


if __name__ == '__main__':
	main()