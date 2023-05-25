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
    
    sum_numerator = 0
    sum_divisor = 0
    for i in range(sample_size):
        for j in range(sample_size):
            # расчёт I_pred
            if y_pred[i] > y_pred[j]:
                I_pred = 0
            elif y_pred[i] == y_pred[j]:
                I_pred = 0.5
            else:
                I_pred = 1
            # расчёт I_true
            if y_true[i] >= y_true[j]:
                I_true = 0
            else:
                I_true = 1
                
            sum_numerator += I_pred * I_true
            sum_divisor += I_true
    
    auc = sum_numerator / sum_divisor
    print(auc)

if __name__ == '__main__':
	main()