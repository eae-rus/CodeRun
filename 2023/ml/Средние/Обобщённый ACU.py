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
    y_true_set = sorted(set(y_true))
    dict_pred = {}
    for i in range(sample_size):
        if dict_pred.get(y_true[i]) == None:
            dict_pred[y_true[i]] = []
            dict_pred[y_true[i]].append(y_pred[i])
        else:
            dict_pred[y_true[i]].append(y_pred[i])
    
    # сортировка внутри словаря
    for y_true_sample in y_true_set:
        dict_pred[y_true_sample] = sorted(dict_pred[y_true_sample])

    # вычисление ROC AUC
    sum_numerator = 0
    sum_divisor = 0
    for y_true_left in range(y_true_set.__len__()-1):
        name_y_true_left = y_true_set[y_true_left]
        for y_true_right in range(y_true_left + 1, y_true_set.__len__()):
            name_y_true_right = y_true_set[y_true_right]
            array_left = dict_pred[name_y_true_left]
            array_right = dict_pred[name_y_true_right]
            len_array_left = array_left.__len__()
            len_array_right = array_right.__len__()

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