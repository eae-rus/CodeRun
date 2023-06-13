import os
from sklearn.cluster import KMeans
import numpy as np

def main():
    '''
    '''
    file_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Кластеризация символьных последовательностей\\\\test.txt'
    preds = []
    with open(file_path, 'r') as f:
        n, k = map(int, f.readline()[:-1].split())
        alphabet = f.readline()[:-1]

        # Создаем словарь, который будет использоваться для кодирования строк
        char_to_index = {}
        for i, char in enumerate(alphabet):
            char_to_index[char] = i

        # Создаем матрицу, в которой каждый ряд представляет собой закодированную строку 
        X = []
        X_len_max = 1
        for i in range(n):
            string = f.readline()[:-1]
            if len(string) > X_len_max:
                X_len_max = len(string)
            X.append([char_to_index[char] for char in string])

        X_new = np.zeros((n, X_len_max * (k - 1)))
        for i in range(n):
            for j, char_index in enumerate(X[i]):
                X_new[i, j*(k - 1) + char_index] = 1

        # Кластеризуем строки с помощью k-средних
        kmeans = KMeans(n_clusters=2, random_state=0)
        preds = kmeans.fit_predict(X_new)
        
        # Выводим результаты
        for pred in preds:
            print(pred)

        file_path_out = os.path.abspath("") + '\\2023\\ml\\Сложные\\Кластеризация символьных последовательностей\\\\out.txt'
        with open(file_path_out, "w") as f:
            # Выводим результаты
            for pred in preds:
                print(pred, file=f)


if __name__ == '__main__':
	main()