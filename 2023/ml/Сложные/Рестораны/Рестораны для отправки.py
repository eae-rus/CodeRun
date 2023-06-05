import sys

def main():
    # Функции
    def score(r, d, coeff):
        if r == -1:
            return score_d(d, coeff)
        else:
            return score_r_d(r, d, coeff)
        
    def score_r_d(r, d, coeff):
        a0, a1, a2, a3, a4, a10, a11, a12, a13 = coeff
        return a0 * a4 ** (a1 + a2 * r - a3 * d)
    
    def score_d(d, coeff):
        a0, a1, a2, a3, a4, a10, a11, a12, a13 = coeff
        return a10 * a11 ** (a12 - a13 * d)


    # решение
    a0=0.9516063717141019
    a1=1.0027425085650954
    a2=0.34702781685681094
    a3=99.9938408930363
    a4=1.628246619962428
    a10=1.5310632667517252
    a11=2.4405277818011077
    a12=1.3762525816634232
    a13=100.00930537307289
    coeff = [a0, a1, a2, a3, a4, a10, a11, a12, a13] # некоторые коеф. лишние, это лишь набросок
    
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
