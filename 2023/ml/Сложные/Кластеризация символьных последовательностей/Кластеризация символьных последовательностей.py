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
        X_max_len = 1
        for i in range(n):
            string = f.readline()[:-1]
            if len(string) > X_max_len:
                X_max_len = len(string)
            X.append([char_to_index[char] for char in string])

        X_new = np.zeros((n, k*(k+1) + 1), dtype=np.float32)
        for i in range(n):
            x_len = len(X[i])
            X_local = np.zeros((k, k+1), dtype=np.float32)
            
            for j in range(x_len):
                char_index_j = X[i][j]
                if j == 0:
                    X_local[0, char_index_j] = 1
                if j > 0:
                    char_index_j_1 = X[i][j-1]
                    X_local[char_index_j_1, char_index_j] += 1
                    
                if j == len(X[i]) - 1:
                    X_local[char_index_j, k] = 1
                    
            for j in range(k):
                sum_x_j = X_local[j, :].sum() + 1
                for k in range(k+1):
                    if X_local[j, k] > 0:
                        X_local[j, k] /= sum_x_j
                    else:
                        X_local[j, k] = -1

            for j in range(k):
                for z in range(k+1):
                    X_new[i, j*(k+1) + z] = X_local[j, z]
                
            X_new[i, -1] = x_len / X_max_len
        
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