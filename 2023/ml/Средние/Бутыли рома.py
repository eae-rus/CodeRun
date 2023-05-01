import math
from itertools import *
from collections import Counter

def main():
    '''
    '''
    text = input()
    
    sum_combinations = 0
    for z in range(1,len(text)):
        gen_combinations = (''.join(comb) for comb in permutations(text, z))
        set_combinations = set()
        for comb in gen_combinations:
            if comb not in set_combinations:
                set_combinations.add(comb)
                sum_combinations += 1
    text_list = [char for char in text]
    dict_text = count_occurrences(set(text_list), text_list)
    result = math.factorial(len(text))
    for key, value in dict_text.items():
        result /= math.factorial(value)
    sum_combinations+=result
        
    print(int(sum_combinations))


def count_occurrences(elements, lst):
    counts = Counter(lst)
    result = {}
    for e in elements:
        result[e] = counts.get(e, 0)
    return result

if __name__ == '__main__':
	main()