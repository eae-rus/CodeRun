from collections import defaultdict

def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
 
    Если это заработает - то будет чудом))
    ещё долго плясал над сливанием. Блин, добавил слияние, но не назанчил equal
    источник
    https://www.geeksforgeeks.org/inversion-count-in-array-using-merge-sort/
    '''
    def merge_1(merged):
        merged_len = len(merged)
        merged_new = []
        i = 0
        mid = len(merged) // 2 
        j = mid
        no_inversionCount = 0
        dct_all = defaultdict(float)
        while i < mid and j < merged_len:
            if merged[i][1] < merged[j][1]:
                no_inversionCount += merged_len - j 
                merged_new.append(merged[i])
                dct_all[merged[i][0]] += 1 
                i += 1
            elif merged[i][1] == merged[j][1]:
                dct_t2 = defaultdict(float)
                val = merged[i][1]
                cnt = 0
                j_start = j
                while j <= merged_len and merged[j][1] == val:
                    merged_new.append(merged[j])
                    cnt += 1
                    j += 1
                while i <= mid and merged[i][1] == val:
                    no_inversionCount += cnt * 0.5 + merged_len - j
                    merged_new.append(merged[i])
                    dct_t2[merged[i][0]] += 1
                    i += 1
                for t in range(j_start, j):
                    no_inversionCount -= 0.5 * dct_t2[merged[t][0]] + dct_all[merged[t][0]]
                for key, val in dct_t2.items():
                    dct_all[key] += val 
            else:
                merged_new.append(merged[j])
                no_inversionCount -= dct_all[merged[j][0]]
                j += 1
        while i < mid:
            merged_new.append(merged[i])
            i += 1
        while j < merged_len:
            merged_new.append(merged[j])
            no_inversionCount -= dct_all[merged[j][0]]
            j += 1     

        return no_inversionCount

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
        left_len = len(left)
        right_len = len(right)
        i, j, equal_right, numerator, divisor = 0, 0, 0, 0, 0
        while i < left_len and j < right_len:
            if left[i][0] < right[j][0]:
                merged.append(left[i])
                divisor += right_len - j
                for k in range(j, right_len):
                    if left[i][1] < right[k][1]:
                        numerator += 1
                    elif left[i][1] == right[k][1]:
                        numerator += 0.5
                i += 1
            elif left[i][0] == right[j][0]:
                merged.append(left[i])
                if equal_right < j: # счётчик, чтобы не пересчитывать
                    equal_right = j
                for z in range(equal_right, right_len):
                    if left[i][0] < right[z][0]:
                        equal_right = z
                        divisor += right_len - z
                        for k in range(z, right_len):
                            if left[i][1] < right[k][1]:
                                numerator += 1
                            elif left[i][1] == right[k][1]:
                                numerator += 0.5
                        break
                                 
                i += 1
            else: # left[i][0] > right[j][0]
                merged.append(right[j])
                divisor += left_len - i
                for k in range(i, left_len):
                    if left[k][1] > right[j][1]:
                        numerator += 1
                    elif left[k][1] == right[j][1]:
                        numerator += 0.5
                j += 1
                

        merged += left[i:]
        merged += right[j:]

        merged, numerator = merge_1(merged)

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


