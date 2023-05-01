from itertools import *

def main():
    '''
    '''
    text = input()
    
    sum_combinations = 0
    for z in range(1,len(text)+1):
        set_combinations = set(''.join(comb) for comb in permutations(text, z))
        sum_combinations += len(set_combinations)
        
    print(sum_combinations)

if __name__ == '__main__':
	main()