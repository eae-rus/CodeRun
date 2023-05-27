def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
    '''
    sample_size = int(input())
    dict_pred = {}
    dict_pred_len = {}
    unic_name_dict_pred = []
    for i in range(sample_size):
        y_true_sample, y_pred_sample  = map(float, input().split())
        if y_true_sample not in dict_pred:
            dict_pred[y_true_sample] = []
            dict_pred_len[y_true_sample] = 0
            unic_name_dict_pred.append(y_true_sample)
        dict_pred[y_true_sample].append(y_pred_sample)
        dict_pred_len[y_true_sample] += 1

    # вычисление ROC AUC
    sum_numerator = 0
    sum_divisor = 0
    len_unic_name_dict_pred = len(unic_name_dict_pred)
    while len_unic_name_dict_pred > 1:
        name_one = unic_name_dict_pred.pop()
        len_unic_name_dict_pred -= 1
        array_one = dict_pred[name_one]
        
        for name_two in unic_name_dict_pred:
            array_two = dict_pred[name_two]
            sum_divisor += dict_pred_len[name_one] * dict_pred_len[name_two]

            if name_one < name_two:
                for i in range(dict_pred_len[name_one]):
                    for j in range(dict_pred_len[name_two]):
                        if array_one[i] < array_two[j]:
                            sum_numerator += 1
                        elif array_one[i] == array_two[j]:
                            sum_numerator += 0.5
            else: # name_one > name_two, вариант "==" невозможен
                for i in range(dict_pred_len[name_one]):
                    for j in range(dict_pred_len[name_two]):
                        if array_one[i] > array_two[j]:
                            sum_numerator += 1
                        elif array_one[i] == array_two[j]:
                            sum_numerator += 0.5

    # Вычисление AUC
    if sum_divisor == 0:
        auc = 0.0
    else:
        auc = sum_numerator / sum_divisor

    print(auc)

if __name__ == '__main__':
    main()