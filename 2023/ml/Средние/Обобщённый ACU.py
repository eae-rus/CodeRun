import numpy as np

def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
    '''
    sample_size = int(input())
    y_true, y_pred = [0] * sample_size, [0] * sample_size
    for i in range(sample_size):
        y_true_sample, y_pred_sample = map(float, input().split())
        y_true[i] = y_true_sample
        y_pred[i] = y_pred_sample
    
    sum_numerator = 0
    sum_divisor = 0
    for i in range(sample_size-1):
        for j in range(i+1, sample_size):
            if y_true[i] == y_true[j]:
                continue
            elif y_true[i] < y_true[j]: # прямой случай
                sum_divisor += 1
                if y_pred[i] < y_pred[j]:
                    sum_numerator += 1
                elif y_pred[i] == y_pred[j]:
                    sum_numerator += 0.5
            else: # обратный случай
                sum_divisor += 1
                if y_pred[j] < y_pred[i]:
                    sum_numerator += 1
                elif y_pred[j] == y_pred[i]:
                    sum_numerator += 0.5
    
    auc = sum_numerator / sum_divisor

    print(auc)

if __name__ == '__main__':
    main()