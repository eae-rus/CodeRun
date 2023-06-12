from sklearn.tree import DecisionTreeClassifier
import numpy as np

def main():
    '''
    '''
    # Загрузка данных
    n, m = map(int, input().split())
    T = np.zeros((n, n))

    for i in range(m):
        ai, aj = map(int, input().split())
        T[ai-1, aj-1] += 1

    # Обучение дерева решений
    model = DecisionTreeClassifier()
    model.fit(T, np.arange(n))

    # Получение предсказаний и вывод результата
    predictions = model.predict(T)
    sorted_indices = np.argsort(predictions)

    for index in sorted_indices:
        print(index+1)
    


if __name__ == '__main__':
	main()