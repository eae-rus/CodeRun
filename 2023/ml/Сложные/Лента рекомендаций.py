import sys

def main():
    '''
    '''
    n, m = list(map(int, sys.stdin.readline().strip().split()))

    # Считывание данных
    array_a = []
    for i in range(n):
        array_a.append(int(sys.stdin.readline().strip()))
        
    m_set = set(array_a)
    r_a = [[] for i in range(m)]

    # Разделение данных в словарь в сортированном порядке
    for i in range(n):
        ai = array_a[-1-i]
        r_a[ai].append(n-1-i)


    # формирование выходного массива
    recomendation = []
    previous_key = -1
    for j in range(n):
        a_min = n
        key_a_min = -1
        for key in m_set:
            if previous_key != key:
                if r_a[key][-1] < a_min:
                    a_min = r_a[key][-1]
                    key_a_min = key

        if key_a_min == -1:
            break

        recomendation.append(r_a[key_a_min].pop())
        previous_key = key_a_min
        if r_a[key_a_min] == []:
            m_set.discard(key_a_min)

    print(*recomendation) # вывод в обратном порядке


if __name__ == '__main__':
    main()