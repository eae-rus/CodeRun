def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
 
    Если это заработает - то будет чудом))
    '''
    def calculate_numerator(array_1, start_1, end_1, array_2, start_2, end_2):
        if end_1 - start_1 < 1 and end_2 - start_2 < 1:
            return 0
        elif end_1 - start_1 <= 1 and end_2 - start_2 <= 1:
            if array_1[start_1] < array_2[start_2]:
                return 1
            elif array_1[start_1] == array_2[start_2]:
                return 0.5
            else:
                return 0

        mid_1 = (start_1 + end_1) // 2
        mid_2 = (start_2 + end_2) // 2

        left_numerator = calculate_numerator(array_1, start_1, mid_1, array_2, start_2, mid_2)
        right_numerator = calculate_numerator(array_1, mid_1, end_1, array_2, mid_2, end_2)

        numerator = left_numerator + right_numerator

        if end_1 - start_1 > 1 and end_2 - start_2 > 1:
            for i in range(start_1, mid_1):
                for j in range(mid_2, end_2):
                    if array_1[i] < array_2[j]:
                        numerator += 1
                    elif array_1[i] == array_2[j]:
                        numerator += 0.5

            for i in range(mid_1, end_1):
                for j in range(start_2, mid_2):
                    if array_1[i] < array_2[j]:
                        numerator += 1
                    elif array_1[i] == array_2[j]:
                        numerator += 0.5

        return numerator
    
    
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
        sum_numerator += calculate_numerator(pred[coordinates-pred_len[iteration]: coordinates], 0, pred_len[iteration],
                                             pred[coordinates: sample_size], 0, sample_size - coordinates)
        #for i in range(coordinates-pred_len[iteration], coordinates):
        #    for j in range(coordinates, sample_size):
        #        if pred[i] == pred[j]:
        #            sum_numerator += 0.5
        #        elif pred[i] < pred[j]:
        #            sum_numerator += 1

    # Вычисление AUC
    auc = sum_numerator / sum_divisor

    print(auc)


if __name__ == '__main__':
    main()