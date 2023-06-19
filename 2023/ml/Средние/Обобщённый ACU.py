from collections import defaultdict

def main():
    '''
    Сперва бы разобраться, как это вообще считается...
    Вроде бы с горем-пополам, разобрался...
 
    Если это заработает - то будет чудом, наконец-то свершилось!!))
    https://www.techiedelight.com/merge-sort/
    Но вся пляска была с тем, как исключить лишнее при подсчёте слияний.
    Над этим было много помощи / подсказок...
    '''
    def merge_sort_for_divisor(data, new_data, start, end):
        if end - start + 1 <= 1:
            return data, 0
        elif end - start + 1 == 2:
            mid = (start + end) // 2
            return merge_for_divisor(data, new_data, start, mid, end)
        else:
            mid = (start + end) // 2
            data, divisor_left = merge_sort_for_divisor(data, new_data, start, mid)
            data, divisor_right = merge_sort_for_divisor(data, new_data, mid+1, end)
            data, divisor_merge = merge_for_divisor(data, new_data, start, mid, end)
            divisor = divisor_left + divisor_right + divisor_merge
            return data, divisor

    def merge_for_divisor(data, new_data, start, mid, end):
        '''
        Пока прост выкинул расчёт числителя, оптимизировать потом можно будет
        '''
        i = start
        k = start
        j = mid + 1
        equal_right = start
        divisor = 0
        while i <= mid and j <= end:
            if data[i][0] < data[j][0]:
                new_data[k] = data[i]
                divisor += end + 1 - j
                i += 1
                k += 1
            elif data[i][0] == data[j][0]:
                new_data[k] = data[i]
                if equal_right < j: # счётчик, чтобы не пересчитывать
                    equal_right = j
                z = equal_right
                while z <= end:
                    if data[i][0] < data[z][0]:
                        divisor += end + 1 - z
                        equal_right = z - 1
                        break
                    z += 1          
                i += 1
                k += 1
            else: # data[i][0] > data[j][0]
                new_data[k] = data[j]
                divisor += mid + 1 - i
                j += 1
                k += 1

        while i <= mid:
            new_data[k] = data[i]
            i += 1
            k += 1
        while j <= end:
            new_data[k] = data[j]
            j += 1
            k += 1

        for z in range(start, end+1):
            data[z] = new_data[z]

        return data, divisor

    def merge_sort_for_numerator(data, new_data, start, end):
        if end - start + 1 <= 1:
            return data, 0
        elif end - start + 1 == 2:
            mid = (start + end) // 2
            return merge_for_numerator(data, new_data, start, mid, end)
        else:
            mid = (start + end) // 2
            data, numerator_left = merge_sort_for_numerator(data, new_data, start, mid)
            data, numerator_right = merge_sort_for_numerator(data, new_data, mid+1, end)
            data, numerator_merge = merge_for_numerator(data, new_data, start, mid, end)
            numerator = numerator_left + numerator_right + numerator_merge
            return data, numerator

    def merge_for_numerator(data, new_data, start, mid, end):
        '''
        А теперь отдельно считаю числителя
        '''
        i = start
        k = start
        j = mid + 1
        no_inversionCount = 0 # счётчик "не инверсий" - надо будет ещё понять... по сути это numerator
        extra_points = defaultdict(float) # отсеивание всякой одинаковости.
        while i <= mid and j <= end:
            if data[i][1] < data[j][1]: # А здесь сортировка уже по pred
                new_data[k] = data[i]
                no_inversionCount += end + 1 - j
                extra_points[data[i][0]] += 1 
                i += 1
                k += 1
            elif data[i][1] == data[j][1]:
                extra_points_eqaul = defaultdict(float)
                val = data[i][1]
                repeats = 0
                j_start = j
                while j <= end and data[j][1] == val:
                    new_data[k] = data[j]
                    repeats += 1
                    j += 1
                    k += 1
                while i <= mid and data[i][1] == val:
                    no_inversionCount += repeats * 0.5 + end + 1 - j
                    new_data[k] = data[i]
                    extra_points_eqaul[data[i][0]] += 1
                    i += 1
                    k += 1
                for t in range(j_start, j):
                    name = data[t][0]
                    no_inversionCount -= 0.5 * extra_points_eqaul[name] + extra_points[name]
                for key, val in extra_points_eqaul.items():
                    extra_points[key] += val 
            else: # data[i][1] > data[j][1]
                new_data[k] = data[j]
                no_inversionCount -= extra_points[data[j][0]]
                j += 1
                k += 1  

        while i <= mid:
            new_data[k] = data[i]
            i += 1
            k += 1
        while j <= end:
            new_data[k] = data[j]
            no_inversionCount -= extra_points[data[j][0]]
            j += 1
            k += 1

        for z in range(start, end+1):
            data[z] = new_data[z]

        return data, no_inversionCount

      
    sample_size = int(input())
    data = []
    for _ in range(sample_size):
        t, y  = map(float, input().split())
        data.append((t, y))

    # Сперва выравниваем по true
    new_data = data.copy()
    len_data = len(data)
    data, divisor = merge_sort_for_divisor(data, new_data, 0, len_data - 1)
    # А потом уже по predict
    data, numerator = merge_sort_for_numerator(data, new_data, 0, len_data - 1)

    # Вычисление AUC
    auc = numerator / divisor

    print(auc)


if __name__ == '__main__':
    main()