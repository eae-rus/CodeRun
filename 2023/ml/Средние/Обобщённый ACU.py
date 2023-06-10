import numpy as np

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

    y_pred_diff = np.subtract.outer(y_pred, y_pred)
    y_true_diff = np.subtract.outer(y_true, y_true)

    numerator = np.sum((np.sign(y_pred_diff) > 0) & (np.sign(y_true_diff) > 0))
    numerator += 0.5 * np.sum((np.sign(y_pred_diff) == 0) & (np.sign(y_true_diff) > 0))
    numerator += np.sum((np.sign(y_pred_diff) < 0) & (np.sign(y_true_diff) < 0))
    numerator += 0.5 * np.sum((np.sign(y_pred_diff) == 0) & (np.sign(y_true_diff) < 0))

    denominator = sample_size*sample_size - np.sum(y_true_diff == 0)

    if denominator == 0:
        return 0.0
    else:
        auc = numerator / denominator
        print(auc)

if __name__ == '__main__':
    main()