import math
# from itertools import permutations
from collections import Counter
from functools import reduce


def main():
    '''
    '''
    text = input()

    # Приведённый ниже алгоритм гарантировано работает, но не оптимален по памяти
    # он используется как проверочный / тестирование
    
    # sum_combinations = 0
    # #pre_sum_combinations = 0
    # for z in range(1, len(text) + 1):
    #     gen_combinations = (''.join(comb) for comb in permutations(text, z))
    #     set_combinations = set()
    #     for comb in gen_combinations:
    #         if comb not in set_combinations:
    #             set_combinations.add(comb)
    #             sum_combinations += 1
    #     #print(sum_combinations - pre_sum_combinations)
    #     #pre_sum_combinations = sum_combinations
    #     
    # print(int(sum_combinations))

    len_text = len(text)
    len_set = len(set(text))
    if len_text == 1:
        print(1)
    elif len_text == 2:
        print(2*len_set)
    elif len_text == 3:
        sum_combinations_v2 = len_set # первая точка
        dict_text = dict(Counter(text))
        # вторая и третья точки
        sum_combinations_v2 += 2 * calculat_combination_later(dict_text, len_text)
        print(int(sum_combinations_v2))
    else:
        # первая точка
        sum_combinations_v2 = len_set
        
        # Все точки между ними (не нашёл комбинаторной формулы)
        dict_text = dict(Counter(text))
        cache = {}
        for i in range(2, len_text - 1):
            sum_combinations_v2 += combination(dict_text, i, cache)

        # предпоследняя и последняя точки с учётом лишних
        sum_combinations_v2 += 2 * calculat_combination_later(dict_text, len_text)
        print(int(sum_combinations_v2))


def combination(dict_text: dict, i: int, cache: dict) -> int:
    if i > 0:
        key = (tuple(sorted(dict_text.items())), i)
        if key in cache:
            return cache[key]
        else:
            sum = 0
            for value in dict_text.keys():
                dict_copy = dict_text.copy()
                dict_copy[value] -= 1
                if dict_copy[value] == 0:
                    del dict_copy[value]
                sum += combination(dict_copy, i - 1, cache)
            cache[key] = sum
            return sum
    else:
        return 1

def calculat_combination_later(dict_text: dict, len_text: int) -> int:
    return reduce(lambda x, y: x // y, (math.factorial(value) for value in dict_text.values()), math.factorial(len_text))

    

if __name__ == '__main__':
	main()