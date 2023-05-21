import os
import random
import numpy as np

def main():
    '''
    '''
    file_path = os.path.abspath("") + '\\2023\\ml\\Средние\\Перестановки\\permutations.in'
    with open(file_path, 'r') as f:
        s = f.readline()[:-1]
        n = int(s)

        good_sets = []
        stupid_sets = []

        for i in range(0, n, 2):
            numeric_matrix_1 = np.zeros((8, 8), dtype=np.uint16)
            for j in range(1000):
                perm = list(map(int, f.readline()[:-1].split()))
                for k in range(8):
                    numeric_matrix_1[k][perm[k]-1] += 1
            standard_deviation_1 = np.std(numeric_matrix_1)

            numeric_matrix_2 = np.zeros((8, 8), dtype=np.uint16)
            for j in range(1000):
                perm = list(map(int, f.readline()[:-1].split()))
                for k in range(8):
                    numeric_matrix_2[k][perm[k]-1] += 1
            standard_deviation_2 = np.std(numeric_matrix_2)
            
            if abs(standard_deviation_1 - standard_deviation_2) > 1:
                if standard_deviation_1 < standard_deviation_2:
                    good_sets.append(i)
                    stupid_sets.append(i+1)
                else:
                    stupid_sets.append(i)
                    good_sets.append(i+1)
            else:
                spread_1 = numeric_matrix_1.max() - numeric_matrix_1.min()
                spread_2 = numeric_matrix_2.max() - numeric_matrix_2.min()
                if spread_1 < spread_2:
                    good_sets.append(i)
                    stupid_sets.append(i+1)
                else:
                    stupid_sets.append(i)
                    good_sets.append(i+1)

        file_path_out = os.path.abspath("") + '\\2023\\ml\\Средние\\Перестановки\\output.txt'
        with open(file_path_out, "w") as f:
            for result in good_sets:
                print(result, file=f)
            for result in stupid_sets:
                print(result, file=f)


def RandomPermutation():
    perm = list(range(8))
    random.shuffle(perm)
    return perm

def StupidPermutation():
    partialSums = [0,1,8,35,111,285,
        628,1230,2191,3606,5546,8039,11056,14506,18242,  
        22078,25814,29264,32281,34774,36714,38129,39090,  
        39692,40035,40209,40285,40312,40319,40320]
    r = random.randint(0, partialSums[-1])
    numInv = 0
    while partialSums[numInv] < r:
        numInv += 1
    perm = list(range(8))
    for step in range(numInv):
        t1 = random.randint(0, 7)
        t2 = random.randint(0, 7)
        perm[t1], perm[t2] = perm[t2], perm[t1]
    return perm

if __name__ == '__main__':
	main()