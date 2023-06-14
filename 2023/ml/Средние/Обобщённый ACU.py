def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
 
    Если это заработает - то будет чудом))
    '''
    def calculate_sum_numerator(lowwer, lowwer_len, upper, upper_len):
        sum_numerator = 0
        right_previous = 0
        if lowwer_len <= upper_len:
            for left in range(lowwer_len):
                is_first_occurrence = True
                if left > 0 and lowwer[left-1] == lowwer[left]:
                    sum_numerator += local_sum_numerator
                    continue
                local_sum_numerator = 0
                for right in range(right_previous, upper_len):
                    if lowwer[left] < upper[right]:
                        local_sum_numerator += upper_len - right
                        if is_first_occurrence:
                            right_previous = right
                            is_first_occurrence = False
                        break
                    elif lowwer[left] == upper[right]:
                        local_sum_numerator += 0.5
                        if is_first_occurrence:
                            right_previous = right
                            is_first_occurrence = False
                sum_numerator += local_sum_numerator
        else:
            for left in range(upper_len):
                is_first_occurrence = True
                if left > 0 and upper[-left-1] == upper[-left]:
                    sum_numerator += local_sum_numerator
                    continue
                local_sum_numerator = 0
                for right in range(right_previous, lowwer_len):
                    if upper[-left-1] > lowwer[-right-1]:
                        local_sum_numerator += lowwer_len - right
                        if is_first_occurrence:
                            right_previous = right
                            is_first_occurrence = False
                        break
                    elif upper[-left-1] == lowwer[-right-1]:
                        local_sum_numerator += 0.5
                        if is_first_occurrence:
                            right_previous = right
                            is_first_occurrence = False
                sum_numerator += local_sum_numerator
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
        name_upper = unic_name.pop() # идём в обратную сторону, значит name_one > name_two
        unic_name_len -= 1
        
        left_for_divisor += dict_pred_len[name_upper]
        sum_divisor += dict_pred_len[name_upper] * (sample_size - left_for_divisor)
        for name_lowwer in unic_name:      
            sum_numerator += calculate_sum_numerator(dict_pred[name_lowwer], dict_pred_len[name_lowwer],
                                                     dict_pred[name_upper], dict_pred_len[name_upper])

    # Вычисление AUC
    if sum_divisor == 0:
        auc = 0.0
    else:
        auc = sum_numerator / sum_divisor

    print(auc)

if __name__ == '__main__':
    main()