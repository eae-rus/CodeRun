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
    sorted_indices = sorted(range(sample_size), key=lambda k: y_true[k])
    y_true = [y_true[i] for i in sorted_indices]
    y_pred = [y_pred[i] for i in sorted_indices]

    # Итерация по отсортированным массивам с двумя указателями
    left, right = 0, 1
    sum_numerator = 0
    sum_divisor = 0
    while right < sample_size:
        if y_true[right] != y_true[left]:
            # Вычисление числителя и знаменателя для пары left-right
            divisor = (right - left) * (sample_size - right)
            numerator = 0
            for i in range(left, right):
                for j in range(right, sample_size):
                    if y_pred[i] < y_pred[j]:
                        numerator += 1
                    elif y_pred[i] == y_pred[j]:
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