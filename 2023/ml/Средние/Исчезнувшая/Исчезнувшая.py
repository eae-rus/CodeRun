import os
import numpy as np

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
    for _ in range(4):
        if find_foto(photo_1, photo_2):
            return True
        else:
            photo_2 = np.transpose(photo_2[::-1,:])
    return False

def find_foto(photo_1: np.ndarray, photo_2: np.ndarray) -> bool:
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
        for i in range(n2 - n1+1):
            for k in range(m2 - m1+1):
                if np.array_equal(photo_1, photo_2[i:i+n1, k:k+m1]):
                    return True
        return False


if __name__ == '__main__':
    main()