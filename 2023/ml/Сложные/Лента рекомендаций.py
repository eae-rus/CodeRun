import sys
from collections import defaultdict
from collections import deque

def main():
    '''
    '''
    n, m = list(map(int, sys.stdin.readline().strip().split()))

    # Считывание данных
    array_a = []
    for i in range(n):
        array_a.append(int(sys.stdin.readline().strip()))
        
    m_deque = deque(set(array_a))
    r_a = [[] for i in range(m)]

    # Разделение данных в словарь в сортированном порядке
    for i in range(n):
        ai = array_a[-1-i]
        r_a[ai].append(i)

    # формирование выходного массива
    recomendation = []
    previous_key = -1
    for j in range(n):
        a_max = -1
        key_a_max = -1
        for key in m_deque:
            if previous_key != key:
                if r_a[key][-1] > a_max:
                    a_max = r_a[key][-1]
                    key_a_max = key

        if key_a_max == -1:
            break

        recomendation.append(n-1 - r_a[key_a_max].pop()) # n-1 так как у нас введена обратная нумерация "ценности"
        previous_key = key_a_max
        if len(r_a[key_a_max]) == 0:
            m_deque.remove(key_a_max)

    print(*recomendation) # вывод в обратном порядке


if __name__ == '__main__':
    main()