import numpy as np
from sklearn.mixture import GaussianMixture as GMM

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
    X = np.zeros((n, (k-1)*(k+1)), dtype=np.int32)
    for i in range(n):
        string = input()
        index_0 = char_to_index[string[0]]
        X[i, index_0] = 1
        for j in range(1, len(string)):
            char_index_j_1 = char_to_index[string[j-1]]
            char_index_j= char_to_index[string[j]]
            X[i, k-1+char_index_j_1*(k-1)+char_index_j] += 1
        
        index_n = char_to_index[string[len(string)-1]]
        X[i, k*(k-1)+index_n] = 1
    
    np.random.seed(1)
    # Создание модели
    model = GMM(n_components=2, random_state=42, max_iter=1000, covariance_type='full')
    model.fit(X)
    # Кластеризация данных
    preds = model.predict(X)
    
    # Выводим результаты
    for pred in preds:
        print(pred)

if __name__ == '__main__':
	main()