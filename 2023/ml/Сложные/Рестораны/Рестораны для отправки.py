import sys
import numpy as np

def main():
    # Функции
    def score(r, d, coeff):
        if r == -1:
            return score_d(d, coeff)
        else:
            return score_r_d(r, d, coeff)
        
    def score_r_d(r, d, coeff):
        a0, a1, a2, a3, a4 = coeff
        return a0 * np.exp(a1 + a2 * r - a3 * d)
    
    def score_d(d, coeff):
        a0, a1, a2, a3, a4 = coeff
        return a0 * np.exp(a1 - a3 * d)


    # решение
    a0=0.8852600570499823
    a1=0.8843132805329542
    a2=0.1
    a3=99.99933608684898
    a4=1 # этот не используется
    coeff = [a0, a1, a2, a3, a4] # некоторые коеф. лишние, это лишь набросок
    
    answer = []
    n = int(sys.stdin.readline()[:-1])
    for i in range(n):
        r, d = map(float, sys.stdin.readline()[:-1].split())
        score_answer = score(r, d, coeff)
        answer.append(score_answer)
        
    for i in range(n):
        print(answer[i])


if __name__ == '__main__':
	main()
