import numpy as np

def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
    '''
    sample_size = int(input())
    y_true, y_pred = np.zeros(sample_size), np.zeros(sample_size)
    for i in range(sample_size):
        y_true[i], y_pred[i]  = map(float, input().split())

    sample_size = len(y_true)
    dict_pred = {}
    unic_name_dict_pred = np.unique(y_true)
    for i, name in enumerate(unic_name_dict_pred):
        dict_pred[name] = y_pred[np.where(y_true == name)[0]]
        dict_pred[name].sort()
    sum_numerator = 0
    sum_divisor = 0
    left_for_divisor = 0
    for i in range(len(unic_name_dict_pred)):
        len_array_left = len(dict_pred[unic_name_dict_pred[i]])
        left_for_divisor += len_array_left
        sum_divisor += len_array_left * (sample_size - left_for_divisor)
        array_i = dict_pred[unic_name_dict_pred[i]]
        for j in range(i + 1, len(unic_name_dict_pred)):
            len_array_right = len(dict_pred[unic_name_dict_pred[j]])
            array_j = dict_pred[unic_name_dict_pred[j]]
            right = np.searchsorted(array_j, array_i)
            for index in range(len(right)):
                if right[index] == len_array_right:
                    continue
                if array_i[index] != array_j[right[index]]:
                    sum_numerator += len_array_right - right[index]
                else:
                    while right[index] < len_array_right and array_i[index] == array_j[right[index]]:
                        sum_numerator += 0.5
                        right[index] += 1
                    sum_numerator += len_array_right - right[index]
    auc = sum_numerator / sum_divisor

    print(auc)

if __name__ == '__main__':
    main()