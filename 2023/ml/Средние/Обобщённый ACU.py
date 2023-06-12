def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
    
    Через многие терни и подсказку добрался к алгориму "разделяй и властвуй"
    '''
    def auc_divide_conquer(y_true, y_pred):
        """
        Находит обобщенный AUC (Area Under the ROC Curve) с помощью алгоритма "Divide & Conquer".
        """
        n = len(y_true)

        if n <= 1:
            return 0, 0

        sum_numerator, sum_divisor = 0, 0

        left_auc_sum_numerator, left_auc_sum_divisor = auc_divide_conquer(y_true[:n//2], y_pred[:n//2])
        right_auc_sum_numerator, right_auc_sum_divisor = auc_divide_conquer(y_true[n//2:], y_pred[n//2:])

        sum_numerator = left_auc_sum_numerator + right_auc_sum_numerator
        sum_divisor = left_auc_sum_divisor + right_auc_sum_divisor
        for i in range(n//2):
            for j in range(n//2, n):
                if y_true[i] > y_true[j]:
                    sum_divisor += 1
                    if y_pred[i] > y_pred[j]:
                        sum_numerator += 1
                    elif y_pred[i] == y_pred[j]:
                        sum_numerator += 0.5
                elif y_true[i] < y_true[j]:
                    sum_divisor += 1
                    if y_pred[i] < y_pred[j]:
                        sum_numerator += 1
                    elif y_pred[i] == y_pred[j]:
                        sum_numerator += 0.5
                else: # y_true[i] == y_true[j]
                    continue
                
        return sum_numerator, sum_divisor
    
    sample_size = int(input())
    y_true, y_pred = [0] * sample_size, [0] * sample_size
    for i in range(sample_size):
        y_true_sample, y_pred_sample = map(float, input().split())
        y_true[i] = y_true_sample
        y_pred[i] = y_pred_sample
    
    sum_numerator, sum_divisor = auc_divide_conquer(y_true, y_pred)
    auc = sum_numerator / sum_divisor

    print(auc)

if __name__ == '__main__':
    main()