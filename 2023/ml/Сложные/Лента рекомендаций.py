def main():
    '''
    '''
    n, m = list(map(int, input().split()))
    
    dict_r_a = {}
    
    # Считывание данных
    array_a = []
    for i in range(n):
        array_a.append(int(input()))
    
    # Разделение данных в словарь в сортированном порядке
    for i in range(n):
        ai = array_a[-1-i]
        if dict_r_a.get(ai) is None:
            dict_r_a[ai] = []
            dict_r_a[ai].append(i)
        else:
            dict_r_a[ai].append(i)
    
    # формирование выходного массива
    recomendation = []
    previous_key = -1
    for j in range(n):
        a_max = -1
        key_a_max = -1
        for key in dict_r_a.keys():
            if previous_key != key:
                if dict_r_a[key][-1] > a_max:
                    a_max = dict_r_a[key][-1]
                    key_a_max = key
        
        if key_a_max == -1:
            break
        
        recomendation.append(n-1-dict_r_a[key_a_max].pop()) # n-1 так как у нас введена обратная нумерация "ценности"
        previous_key = key_a_max
        if len(dict_r_a[key_a_max]) == 0:
            del dict_r_a[key_a_max]
    
    print(*recomendation)
    

if __name__ == '__main__':
	main()