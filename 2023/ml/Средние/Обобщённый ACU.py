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
    new_y_true = []
    new_y_pred = []
    for i in range(sample_size):
        if dict_pred.get(y_true[i]) == None:
            dict_pred[y_true[i]] = []
            dict_pred[y_true[i]].append(y_pred[i])
        else:
            dict_pred[y_true[i]].append(y_pred[i])

    for y_true_sample in y_true_set:
        for y_pred_sample in dict_pred[y_true_sample]:
            new_y_true.append(y_true_sample)
            new_y_pred.append(y_pred_sample)
                
        # TODO: Добавить сортировку по pred, и потом использовать это в следующем массиве

    # Итерация по отсортированным массивам с двумя указателями
    left, right = 0, 1
    sum_numerator = 0
    sum_divisor = 0
    while right < sample_size:
        if new_y_true[right] != new_y_true[left]:
            # Вычисление числителя и знаменателя для пары left-right
            divisor = (right - left) * (sample_size - right)
            numerator = 0
            for i in range(left, right):
                for j in range(right, sample_size):
                    if new_y_pred[i] < new_y_pred[j]:
                        numerator += 1
                    elif new_y_pred[i] == new_y_pred[j]:
                        numerator += 0.5
            sum_divisor += divisor
            sum_numerator += numerator
            left = right
        right += 1

    # Вычисление AUC
    if sum_divisor == 0:
        auc = 0.0
    else:
        auc = sum_numerator / sum_divisor

    print(auc)

if __name__ == '__main__':
    main()