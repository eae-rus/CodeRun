import sys


def main():
    '''
    '''
    s1 = input()
    s2 = input()
    n = int(input())
    d = {}
    
    for _ in range(n):
        a, b = input().split()
        d[a] = b
    
    if s1 == s2:
        print(0)
        sys.exit()
    
    if len(s1) != len(s2):
        print(-1)
        sys.exit()
    
    matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    for i in range(len(s1) + 1):
        matrix[i][0] = i
    
    for j in range(len(s2) + 1):
        matrix[0][j] = j
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            deletion = matrix[i-1][j] + 1
            insertion = matrix[i][j-1] + 1
            substitution = matrix[i-1][j-1] + (0 if s1[i-1] == s2[j-1] else 1)
            transposition = float("inf")
            if i > 1 and j > 1 and s1[i-2:i] == s2[j-1:j+1][::-1]:
                transposition = matrix[i-2][j-2] + 1
            if s1[i-1:i+1] in d:
                substitution = min(substitution, matrix[i-1][j-1] + 1)
                transposition = min(transposition, matrix[i-2][j-2] + 1)
                insertion = min(insertion, matrix[i][j-1] + 1)
                deletion = min(deletion, matrix[i-1][j] + 1)
    
            matrix[i][j] = min(deletion, insertion, substitution, transposition)
    
    if matrix[-1][-1] > 4:
        print(-1)
    else:
        print(matrix[-1][-1])
    


if __name__ == '__main__':
	main()