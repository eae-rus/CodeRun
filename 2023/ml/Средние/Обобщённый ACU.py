def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
 
    Если это заработает - то будет чудом))
    Надеюсь всё же доразделялся))
    '''
    def calculate_auc(y_true, y_pred, start, end):
        if end - start < 1:
            return 0, 0
        elif end - start == 1:
            if y_true[start] < y_true[end]:
                if y_pred[start] < y_pred[end]:
                    return 1, 1
                elif y_pred[start] == y_pred[end]:
                    return 0.5, 1
                else:
                    return 0, 1
            elif y_true[start] == y_true[end]:
                return 0, 0
            else: # y_true[start] > y_true[end]
                if y_pred[start] > y_pred[end]:
                    return 1, 1
                elif y_pred[start] == y_pred[end]:
                    return 0.5, 1
                else:
                    return 0, 1

        mid = (start + end) // 2

        left_numerator, left_divisor = calculate_auc(y_true, y_pred, start, mid)
        right_numerator, right_divisor = calculate_auc(y_true, y_pred, mid, end)

        numerator = left_numerator + right_numerator
        divisor = left_divisor + right_divisor
        
        for i in range(start, mid):
            for j in range(mid+1, end+1):
                if y_true[i] < y_true[j]:
                    if y_pred[i] < y_pred[j]:
                        numerator += 1
                        divisor += 1
                    elif y_pred[i] == y_pred[j]:
                        numerator += 0.5
                        divisor += 1
                    else: # y_pred[i] > y_pred[j]
                        numerator += 0
                        divisor += 1
                elif y_true[i] == y_true[j]:
                    continue
                else: # y_true[i] > y_true[j]
                    if y_pred[i] > y_pred[j]:
                        numerator += 1
                        divisor += 1
                    elif y_pred[i] == y_pred[j]:
                        numerator += 0.5
                        divisor += 1
                    else: # y_pred[i] < y_pred[j]
                        numerator += 0
                        divisor += 1

        return numerator, divisor
    
    
    sample_size = int(input())
    y_true, y_pred = [0] * sample_size, [0] * sample_size
    for i in range(sample_size):
        y_true_sample, y_pred_sample = map(float, input().split())
        y_true[i] = y_true_sample
        y_pred[i] = y_pred_sample

    # вычисление ROC AUC
    sum_numerator, sum_divisor = calculate_auc(y_true, y_pred, 0, sample_size-1)

    # Вычисление AUC
    auc = sum_numerator / sum_divisor

    print(auc)


if __name__ == '__main__':
    main()