def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
 
    Если это заработает - то будет чудом))
    "сортировка в сортировке"
    '''
    def calculate_numerator(lowwer, upper):
        sum_numerator = 0
        
        lowwer.sort()
        upper.sort()
        i, j = 0, 0
        lowwer_len = len(lowwer)
        upper_len = len(upper)
        is_first = True
        previous_j = 0
        
        while i < lowwer_len and j < upper_len:
            y_i = lowwer[i]
            y_j = upper[j]
            
            if y_i == y_j:
                sum_numerator += 0.5
                if is_first:
                    is_first = False
                    previous_j = j
                j += 1
                if not is_first and j == upper_len:
                    is_first = True
                    j = previous_j
                    i += 1
            elif y_i < y_j:
                sum_numerator += upper_len - j
                if not is_first:
                    is_first
                    j = previous_j
                i += 1
            else:
                j += 1
            
        return sum_numerator
    
    
    sample_size = int(input())
    dict_pred = {}
    dict_pred_len = {}
    unic_name = []
    for i in range(sample_size):
        y_true_sample, y_pred_sample  = map(float, input().split())
        if y_true_sample not in dict_pred:
            dict_pred[y_true_sample] = []
            dict_pred_len[y_true_sample] = 0
            unic_name.append(y_true_sample)
        dict_pred[y_true_sample].append(y_pred_sample)
        dict_pred_len[y_true_sample] += 1

    pred = []
    pred_len = []
    unic_name.sort()
    # Создание единого массива
    for name in unic_name:
        for x in dict_pred[name]:
            pred.append(x)
        pred_len.append(dict_pred_len[name])

    # вычисление ROC AUC
    sum_numerator = 0
    sum_divisor = 0
    
    coordinates = 0
    for iteration in range(len(pred_len)-1):
        coordinates += pred_len[iteration]
        sum_divisor += pred_len[iteration] * (sample_size - coordinates)
        sum_numerator += calculate_numerator(pred[coordinates-pred_len[iteration]: coordinates],
                                             pred[coordinates: sample_size])


    # Вычисление AUC
    auc = sum_numerator / sum_divisor

    print(auc)


if __name__ == '__main__':
    main()