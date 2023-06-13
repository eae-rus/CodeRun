from sklearn.cluster import KMeans
import numpy as np

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
        
    X_new = np.zeros((n, k-1 + (k-1)*(k-1) + k-1 + 1), dtype=np.float32)
    for i in range(n):
        x_len = len(X[i])
        for j in range(x_len):
            char_index_j = X[i][j]
            if j == 0:
                X_new[i, char_index_j] = 1
            if j > 0:
                char_index_j_1 = X[i][j-1]
                X_new[i, k-1 + char_index_j_1+(k-1) + char_index_j] += 1 / (x_len-1)
                
            if j == len(X[i]) - 1:
                X_new[i, k-1 + (k-1)*(k-1) + char_index_j] = 1
        X_new[i, -1] = x_len / X_max_len

    
    # Кластеризуем строки с помощью k-средних
    kmeans = KMeans(n_clusters=2, random_state=0)
    preds = kmeans.fit_predict(X_new)
    
    # Выводим результаты
    for pred in preds:
        print(pred)

if __name__ == '__main__':
	main()