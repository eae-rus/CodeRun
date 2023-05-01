from itertools import *

def main():
    '''
    '''
    text = input()
    
    sum_combinations = 0
    for z in range(1,len(text)+1):
        gen_combinations = (''.join(comb) for comb in permutations(text, z))
        set_combinations = set()
        for comb in gen_combinations:
            if comb not in set_combinations:
                set_combinations.add(comb)
                sum_combinations += 1
        
    print(sum_combinations)

if __name__ == '__main__':
	main()