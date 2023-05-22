import os
import random
import numpy as np

def main():
    '''
    '''
    #file_path_example = os.path.abspath("") + '\\2023\\ml\\Средние\\Перестановки\\example1.txt'
    #WriteExample(file_path_example)
    
    file_path = os.path.abspath("") + '\\2023\\ml\\Средние\\Перестановки\\permutations.in'
    #file_path = os.path.abspath("") + '\\2023\\ml\\Средние\\Перестановки\\example.txt'
    with open(file_path, 'r') as f:
        s = f.readline()[:-1]
        n = int(s)
        good_sets = []
        stupid_sets = []
        for i in range(0, n):
            numeric_matrix_1 = np.zeros((8, 8), dtype=np.uint32)
            for j in range(1000):
                perm = list(map(int, f.readline()[:-1].split()))
                for k in range(8):
                    numeric_matrix_1[k][perm[k]-1] += 1

            #numeric_matrix_2 = np.zeros((8, 8), dtype=np.uint32)
            #for j in range(1000):
            #    perm = list(map(int, f.readline()[:-1].split()))
            #    for k in range(8):
            #        numeric_matrix_2[k][perm[k]-1] += 1
            
            sum_anomaly_1 = (numeric_matrix_1[0][7] + numeric_matrix_1[1][0] + numeric_matrix_1[2][1] +
                             numeric_matrix_1[3][2] + numeric_matrix_1[4][3] + numeric_matrix_1[5][4] +
                             numeric_matrix_1[6][5] + numeric_matrix_1[7][6])
            #sum_anomaly_2 = (numeric_matrix_2[0][7] + numeric_matrix_2[1][0] + numeric_matrix_2[2][1] +
            #                 numeric_matrix_2[3][2] + numeric_matrix_2[4][3] + numeric_matrix_2[5][4] +
            #                 numeric_matrix_2[6][5] + numeric_matrix_2[7][6])
            #x = numeric_matrix_2[0]
            #if (sum_anomaly_1 > sum_anomaly_2):
            #    good_sets.append(i)
            #    stupid_sets.append(i+1)
            #else:
            #    stupid_sets.append(i)
            #    good_sets.append(i+1)
            if sum_anomaly_1 <= 1115: # выявлено экспериментально, граница где-то у 1115-1131
                good_sets.append(i)
            else:
                stupid_sets.append(i)

        #x1 = max(good_sets)
        #x2 = min(good_sets)
        #y1 = max(stupid_sets)
        #y2 = min(stupid_sets)
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

def WriteExample(path):
    """
        Предназначено для выяления аномалий, записывается 1кк точек.
        На основании них был выявлен сильный перекос, а именно, то, что
        0 редко находится на месте 7
        1 редко находится на месте 0
        2 редко находится на месте 1
        и т.д.
    """
    with open(path, "w") as f:
        n = 1
        print(n, file=f)
        for i in range(n):
            print(i)
            for j in range(1000000):
                array_random = RandomPermutation()
                s = " ".join(str(x) for x in array_random)
                print(s, file=f)
            for j in range(1000000):
                array_random = StupidPermutation()
                s = " ".join(str(x) for x in array_random)
                print(s, file=f)

if __name__ == '__main__':
    ## !!!!!!!!! создать самому эти выборки, и посмотреть, какая, куда и как смещена обычно? !!!!!!!!
	main()