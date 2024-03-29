import os
import numpy as np
from functools import lru_cache

def main() -> None:
    '''
    '''
    #file_path = os.path.abspath("input.txt")
    file_path = os.path.abspath("") + '\\2023\\ml\\Средние\\Исчезнувшая\\Пример 2.txt'
    
    with open(file_path, 'r') as f:
        n1, m1 = map(int, f.readline()[:-1].split())
        photo_1 = np.empty((n1, m1))
        for n in range(n1):
            line = f.readline()
            for m in range(m1):
                photo_1[n,m] = ord(line[m])
                
        n2, m2 = map(int, f.readline()[:-1].split())
        photo_2 = np.empty((n2, m2))
        for n in range(n2):
            line = f.readline()
            for m in range(m2):
                photo_2[n,m] = ord(line[m])

    answer: bool = find_foto_in_all_planes(photo_1, photo_2)  

    if answer:
        print("Yes")
    else:
        print("No")

def find_foto_in_all_planes(photo_1: np.ndarray, photo_2: np.ndarray) -> bool:
    '''
    '''
    sum_foto_1 = np.sum(photo_1)
    for _ in range(4):
        if find_foto(photo_1, photo_2, sum_foto_1):
            return True
        else:
            photo_2 = np.transpose(photo_2[::-1,:])
    return False

def find_foto(photo_1: np.ndarray, photo_2: np.ndarray, sum_foto_1: int) -> bool:
    '''
    '''
    n1, m1 = photo_1.shape
    n2, m2 = photo_2.shape

    if (n2 < n1 or m2 < m1):
        return False

    elif (n2 == n1 and m2 == m1):
        if np.array_equal(photo_1, photo_2):
            return True
        else:
            return False

    else:
        sum_foto_2_start = np.sum(photo_2[0:n1,0:m1])
        for i in range(n2 - n1+1):
            if i>0:
                sum_foto_2_start -= np.sum(photo_2[i-1:i,0:m1])
                sum_foto_2_start += np.sum(photo_2[i+n1-1:i+n1,0:m1])
            
            sum_foto_2 = sum_foto_2_start
            for k in range(m2 - m1+1):
                if k>0:
                    sum_foto_2 -= np.sum(photo_2[i:i+n1,k-1:k])
                    sum_foto_2 += np.sum(photo_2[i:i+n1,k+m1-1:k+m1])
                if sum_foto_2 == sum_foto_1:
                    if np.array_equal(photo_1, photo_2[i:i+n1, k:k+m1]):
                        return True
        return False

@lru_cache(maxsize=None)
def array_equal(a: np.ndarray, b: np.ndarray) -> bool:
    return np.array_equal(a, b)

if __name__ == '__main__':
    main()