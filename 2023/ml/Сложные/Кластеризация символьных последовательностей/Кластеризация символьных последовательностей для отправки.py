import numpy as np
from sklearn.mixture import GaussianMixture

def main():
    '''
    '''
    n, k = map(int, input().split())
    alphabet = input()
    # Создаем словарь, который будет использоваться для кодирования строк
    char_to_index = {}
    for i, char in enumerate(alphabet):
        char_to_index[char] = i
        
    # Создаем матрицу, в которой каждый ряд представляет собой закодированную строку 
    X = []
    X_max_len = 1
    for i in range(n):
        string = input()
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

    
    # Создание модели
    gmm = GaussianMixture(n_components=2, random_state=0)
    # Оценка параметров модели
    gmm.fit(X_new)
    # Кластеризация данных
    preds = gmm.predict(X_new)
    
    # Выводим результаты
    for pred in preds:
        print(pred)

if __name__ == '__main__':
	main()