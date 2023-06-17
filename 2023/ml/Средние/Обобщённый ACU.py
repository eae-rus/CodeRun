def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
 
    Если это заработает - то будет чудом))
    источник
    https://www.geeksforgeeks.org/inversion-count-in-array-using-merge-sort/
    '''
    def merge_sort(data):
        if len(data) <= 1:
            return data, 0, 0
        elif len(data) == 2:
            return merge(data[:1], data[1:])
        else:
            mid = len(data) // 2
            left, numerator_left, divisor_left = merge_sort(data[:mid])
            right, numerator_right, divisor_right = merge_sort(data[mid:])
            merged, numerator_merge, divisor_merge = merge(left, right)
            numerator = numerator_left + numerator_right + numerator_merge
            divisor = divisor_left + divisor_right + divisor_merge
            return merged, numerator, divisor

    def merge(left, right):
        merged = []
        i, j, numerator, divisor = 0, 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                merged.append(left[i])
                divisor += len(right) - j
                for k in range(j, len(right)):
                    if left[i][1] < right[k][1]:
                        numerator += 1
                    elif left[i][1] == right[k][1]:
                        numerator += 0.5
                i += 1
            elif left[i][0] == right[j][0]:
                merged.append(left[i])
                for z in range(j, len(right)):
                    if left[i][0] < right[z][0]:
                        divisor += len(right) - z
                        for k in range(z, len(right)):
                            if left[i][1] < right[k][1]:
                                numerator += 1
                            elif left[i][1] == right[k][1]:
                                numerator += 0.5
                        break
                
                merged.append(right[j])
                for z in range(i, len(left)):
                    if left[z][0] > right[j][0]:
                        divisor += len(left) - z
                        for k in range(z, len(left)):
                            if left[k][1] > right[j][1]:
                                numerator += 1
                            elif left[k][1] == right[j][1]:
                                numerator += 0.5
                        break
                                 
                i += 1
                j += 1 
            else: # left[i][0] > right[j][0]
                merged.append(right[j])
                divisor += len(left) - i
                for k in range(i, len(left)):
                    if left[k][1] > right[j][1]:
                        numerator += 1
                    elif left[k][1] == right[j][1]:
                        numerator += 0.5
                j += 1
                

        merged += left[i:]
        merged += right[j:]
        return merged, numerator, divisor

      
    sample_size = int(input())
    data = []
    for _ in range(sample_size):
        t, y  = map(float, input().split())
        data.append((t, y))

    data, numerator, divisor = merge_sort(data)
    # Вычисление AUC
    auc = numerator / divisor

    print(auc)


if __name__ == '__main__':
    main()