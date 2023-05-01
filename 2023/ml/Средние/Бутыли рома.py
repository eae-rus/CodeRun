from itertools import *

def main():
    '''
    '''
    text = input()
    
    sum_combinations = 0
    for z in range(1,len(text)+1):
        list_combinations = []
        for i in permutations(text,z):
            list_combinations.append(''.join(i))
        set_combinations = list(set(list_combinations))
        #print(set_combinations)
        sum_combinations += len(set_combinations)
        
    print(sum_combinations)

if __name__ == '__main__':
	main()