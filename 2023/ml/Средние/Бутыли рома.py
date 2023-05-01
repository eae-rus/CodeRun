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
                
    result = math.factorial(len(text))
    counts_text = Counter(text)
    for value in counts_text.values():
        result /= math.factorial(value)
    sum_combinations += result
        
    print(int(sum_combinations))

if __name__ == '__main__':
	main()