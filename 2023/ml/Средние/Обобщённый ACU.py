def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
    '''
    sample_size = int(input())
    y_true, y_pred = [], []
    for i in range(sample_size):
        y_true_sample, y_pred_sample  = map(float, input().split())
        y_true.append(y_true_sample)
        y_pred.append(y_pred_sample)

    # Сортировка массивов y_true и y_pred по возрастанию y_true
    y_true_set = list(set(y_true))
    y_true_set.sort()
    dict_pred = {}
    for i in range(sample_size):
        if y_true[i] not in dict_pred:
            dict_pred[y_true[i]] = []
        dict_pred[y_true[i]].append(y_pred[i])
    
    # сортировка внутри словаря
    for y_true_sample in y_true_set:
        dict_pred[y_true_sample].sort()

    # вычисление ROC AUC
    sum_numerator = 0
    sum_divisor = 0
    len_y_true_set = len(y_true_set)
    for y_true_left in range(len_y_true_set-1):
        name_y_true_left = y_true_set[y_true_left]
        for y_true_right in range(y_true_left + 1, len_y_true_set):
            name_y_true_right = y_true_set[y_true_right]
            array_left = dict_pred[name_y_true_left]
            array_right = dict_pred[name_y_true_right]
            len_array_left = len(array_left)
            len_array_right = len(array_right)

            sum_divisor += len_array_left * len_array_right
            right_previous = 0
            for left in range(len_array_left):
                is_first_occurrence = True
                for right in range(right_previous, len_array_right):
                    if array_left[left] < array_right[right]:
                        sum_numerator += len_array_right - right
                        if is_first_occurrence:
                            right_previous = right
                            is_first_occurrence = False
                        break
                    elif array_left[left] == array_right[right]:
                        sum_numerator += 0.5
                        if is_first_occurrence:
                            right_previous = right
                            is_first_occurrence = False

    # Вычисление AUC
    if sum_divisor == 0:
        auc = 0.0
    else:
        auc = sum_numerator / sum_divisor

    print(auc)

if __name__ == '__main__':
    main()