def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
 
    Если это заработает - то будет чудом))
    Новая версия "двойные словари"
    '''
      
    sample_size = int(input())
    t_dict = {}
    t_len_dict = {}
    t_unic = []
    for i in range(sample_size):
        t, y  = map(float, input().split())
        if t not in t_dict:
            t_dict[t] = {}
            t_len_dict[t] = 0
            t_unic.append(t)
        if y not in t_dict[t]:
            t_dict[t][y] = 0
        t_dict[t][y] += 1
        t_len_dict[t] += 1

    # сортировка уникальных "t"
    t_unic.sort()
    # Создание словаря уникальных "y" в каждом подмасиве "t" и их сортировка
    y_unic = {}
    y_len_dict = {}
    for name in t_unic:
        y_unic_keys = list(t_dict[name].keys())
        y_unic_keys.sort()
        y_unic[name] = y_unic_keys
        y_len_dict[name] = len(y_unic[name])

    # вычисление ROC AUC
    sum_numerator = 0
    sum_divisor = 0
    for t_low_index in range(len(t_unic)-1):
        t_low_name = t_unic[t_low_index]
        for t_up_index in range(t_low_index+1, len(t_unic)):
            t_up_name = t_unic[t_up_index]
            sum_divisor += t_len_dict[t_low_name] * t_len_dict[t_up_name]
            
            i, j = 0, 0
            y_up_len_sum = 0
            while i < y_len_dict[t_low_name] and j < y_len_dict[t_up_name]:
                y_i = y_unic[t_low_name][i]
                y_j = y_unic[t_up_name][j]
                
                if y_i == y_j:
                    sum_numerator += 0.5 * t_dict[t_low_name][y_i] * t_dict[t_up_name][y_j]
                    y_up_len_sum += t_dict[t_up_name][y_j]
                    j += 1
                elif y_i < y_j:
                    sum_numerator += t_dict[t_low_name][y_i] * (t_len_dict[t_up_name] - y_up_len_sum)
                    i += 1
                else:
                    y_up_len_sum += t_dict[t_up_name][y_j]
                    j += 1

    # Вычисление AUC
    auc = sum_numerator / sum_divisor

    print(auc)


if __name__ == '__main__':
    main()