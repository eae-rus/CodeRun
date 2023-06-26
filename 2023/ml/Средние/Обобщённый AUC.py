from collections import defaultdict

def main():
    '''
    '''
    def merge_sort_for_numerator(data):
        if len(data) <= 1:
            return data, 0
        elif len(data) == 2:
            return merge_for_numerator(data[:1], data[1:])
        else:
            mid = len(data) // 2
            left, numerator_left = merge_sort_for_numerator(data[:mid])
            right, numerator_right = merge_sort_for_numerator(data[mid:])
            merged, numerator_merge = merge_for_numerator(left, right)
            numerator = numerator_left + numerator_right + numerator_merge
            return merged, numerator

    def merge_for_numerator(left, right):
        '''
        А теперь отдельно считаю числителя
        '''
        merged = []
        i, j = 0, 0
        no_inversionCount = 0 # счётчик "не инверсий" - надо будет ещё понять... по сути это numerator
        extra_points = defaultdict(float) # отсеивание всякой одинаковости.
        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]: # А здесь сортировка уже по pred
                merged.append(left[i])
                no_inversionCount += len(right) - j
                extra_points[left[i][0]] += 1 
                i += 1
            elif left[i][1] == right[j][1]:
                extra_points_eqaul = defaultdict(float)
                val = left[i][1]
                repeats = 0
                j_start = j
                while j < len(right) and right[j][1] == val:
                    merged.append(right[j])
                    repeats += 1
                    j += 1
                while i < len(left) and left[i][1] == val:
                    no_inversionCount += repeats * 0.5 + len(right) - j
                    merged.append(left[i])
                    extra_points_eqaul[left[i][0]] += 1
                    i += 1
                for t in range(j_start, j):
                    name = right[t][0]
                    no_inversionCount -= 0.5 * extra_points_eqaul[name] + extra_points[name]
                for key, val in extra_points_eqaul.items():
                    extra_points[key] += val 
            else: # left[i][1] > right[j][1]
                merged.append(right[j])
                no_inversionCount -= extra_points[right[j][0]]
                j += 1    

        merged += left[i:]
        while j < len(right):
            merged.append(right[j])
            no_inversionCount -= extra_points[right[j][0]]
            j += 1

        return merged, no_inversionCount

      
    sample_size = int(input())
    data = []
    for _ in range(sample_size):
        t, y  = map(float, input().split())
        data.append((t, y))

    # Сперва выравниваем по true
    data.sort(key=lambda x: x[0])
    divisor = 0
    repeat = 1
    for i in range(1, len(data)):
        if data[i][0] != data[i-1][0]:
            divisor += repeat * (len(data) - i)
            repeat = 1
        else:
            repeat += 1
    # А потом уже по predict
    data, numerator = merge_sort_for_numerator(data)

    # Вычисление AUC
    auc = numerator / divisor

    print(auc)


if __name__ == '__main__':
    main()