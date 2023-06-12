def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
    '''
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

    unic_name.sort()
    # сортировка внутри словаря
    for name in unic_name:
        dict_pred[name].sort()

    # вычисление ROC AUC
    sum_numerator = 0
    sum_divisor = 0
    left_for_divisor = 0
    
    unic_name_len = len(unic_name)
    while unic_name_len > 1:
        name_one = unic_name.pop()
        unic_name_len -= 1
        
        left_for_divisor += dict_pred_len[name_one]
        sum_divisor += dict_pred_len[name_one] * (sample_size - left_for_divisor)
        for name_two in unic_name:      
            right_previous = 0
            for left in range(dict_pred_len[name_one]):
                is_first_occurrence = True
                if left > 0 and dict_pred[name_one][left-1] == dict_pred[name_one][left]:
                    sum_numerator += local_sum_numerator
                    continue
                local_sum_numerator = 0
                for right in range(right_previous, dict_pred_len[name_two]):
                    if dict_pred[name_one][left] < dict_pred[name_two][right]:
                        local_sum_numerator += dict_pred_len[name_two] - right
                        if is_first_occurrence:
                            right_previous = right
                            is_first_occurrence = False
                        break
                    elif dict_pred[name_one][left] == dict_pred[name_two][right]:
                        local_sum_numerator += 0.5
                        if is_first_occurrence:
                            right_previous = right
                            is_first_occurrence = False
                sum_numerator += local_sum_numerator

    # Вычисление AUC
    if sum_divisor == 0:
        auc = 0.0
    else:
        auc = 1 - sum_numerator / sum_divisor

    print(auc)

if __name__ == '__main__':
    main()