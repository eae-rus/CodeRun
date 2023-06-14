def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
 
    Если это заработает - то будет чудом))
    Надеюсь всё же доразделялся))
    '''
    def calculate_auc(y_true, y_pred):
        if len(y_true) < 2:
            return 0, 0
        elif len(y_true) == 2:
            if y_true[0] == y_true[1]:
                return 0, 0
            elif y_true[0] < y_true[1]:
                if y_pred[0] < y_pred[1]:
                    return 1, 1
                elif y_pred[0] == y_pred[1]:
                    return 0.5, 1
                else:
                    return 0, 1
            else: # y_true[start] > y_true[end]
                if y_pred[0] > y_pred[1]:
                    return 1, 1
                elif y_pred[0] == y_pred[1]:
                    return 0.5, 1
                else:
                    return 0, 1

        mid = len(y_true) // 2

        left_numerator, left_divisor = calculate_auc(y_true[:mid], y_pred[:mid])
        right_numerator, right_divisor = calculate_auc(y_true[mid:], y_pred[mid:])

        numerator = left_numerator + right_numerator
        divisor = left_divisor + right_divisor
        
        for i in range(mid):
            for j in range(mid, len(y_true)):
                if y_true[i] == y_true[j]:
                    continue
                elif y_true[i] < y_true[j]:
                    if y_pred[i] < y_pred[j]:
                        numerator += 1
                        divisor += 1
                    elif y_pred[i] == y_pred[j]:
                        numerator += 0.5
                        divisor += 1
                    else: # y_pred[i] > y_pred[j]
                        numerator += 0
                        divisor += 1
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
    sum_numerator, sum_divisor = calculate_auc(y_true, y_pred)

    # Вычисление AUC
    auc = sum_numerator / sum_divisor

    print(auc)


if __name__ == '__main__':
    main()