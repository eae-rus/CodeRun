from sklearn.cluster import KMeans
import numpy as np

def main():
    '''
    '''
    n, k = map(int, input().split())
    alphabet = input().strip()
    
    # Создаем словарь, который будет использоваться для кодирования строк
    char_to_index = {}
    for i, char in enumerate(alphabet):
        char_to_index[char] = i
    
    # Создаем матрицу, в которой каждый ряд представляет собой закодированную строку 
    X = np.zeros((n, k))
    for i in range(n):
        string = input().strip()
        for j, char in enumerate(string):
            X[i, j] = char_to_index[char]
        # Заполняем оставшиеся символы алфавита S
        for j in range(len(string), k):
            X[i, j] = char_to_index[alphabet[-1]]
    
    # Кластеризуем строки с помощью k-средних
    kmeans = KMeans(n_clusters=2, random_state=0)
    preds = kmeans.fit_predict(X)
    
    # Выводим результаты
    for pred in preds:
        print(pred)


if __name__ == '__main__':
	main()