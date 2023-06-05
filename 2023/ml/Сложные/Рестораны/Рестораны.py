import os
import numpy as np

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
    
	# Загрузка данных
    file_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Рестораны\\restaurants_train.txt'
    #file_path = os.path.abspath("") + '\\Рестораны\\restaurants_train.txt'
    winers = []
    losers = []
    with open(file_path, 'r') as f:
        for i in range(1000):
            winner, r1, r2, d1, d2 = map(float, f.readline()[:-1].split())
            
            if winner == 0:
                winers.append((r1, d1))
                losers.append((r2, d2))
            elif winner == 1:
                winers.append((r2, d2))
                losers.append((r1, d1))
            else:
                continue
    
    len_train = len(winers)
    
    # стартовые значения
    # a0=0.7351901041037813
    # a1=0.8715852184036723
    # a2=0.2923497630477402
    # a3=99.98198590903422
    # a4=1.9207480230338367
    # a5=1.8006310674350638
    a0=0.9516063717141019
    a1=1.0027425085650954
    a2=0.34702781685681094
    a3=99.9938408930363
    a4=1.628246619962428
    a10=1.5310632667517252
    a11=2.4405277818011077
    a12=1.3762525816634232
    a13=100.00930537307289
    
    learning_rate=0.2
    delta = 1e-6
    previos_m = 1
    for epoch in range(10000):
        sum_grad_a0, sum_grad_a1, sum_grad_a2, sum_grad_a3, sum_grad_a4, sum_grad_a10, sum_grad_a11, sum_grad_a12, sum_grad_a13 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        sum_m = 0
        coeff = [a0, a1, a2, a3, a4, a10, a11, a12, a13]
        coeff_a0_delta = [a0+delta, a1, a2, a3, a4, a10, a11, a12, a13]
        coeff_a1_delta = [a0, a1+delta, a2, a3, a4, a10, a11, a12, a13]
        coeff_a2_delta = [a0, a1, a2+delta, a3, a4, a10, a11, a12, a13]
        coeff_a3_delta = [a0, a1, a2, a3+delta, a4, a10, a11, a12, a13]
        coeff_a4_delta = [a0, a1, a2, a3, a4+delta, a10, a11, a12, a13]
        coeff_a10_delta = [a0, a1, a2, a3, a4, a10+delta, a11, a12, a13]
        coeff_a11_delta = [a0, a1, a2, a3, a4, a10, a11+delta, a12, a13]
        coeff_a12_delta = [a0, a1, a2, a3, a4, a10, a11, a12+delta, a13]
        coeff_a13_delta = [a0, a1, a2, a3, a4, a10, a11, a12, a13+delta]
        for i in range(len_train):
            r_loser, d_loser = losers[i][0], losers[i][1]
            r_winer, d_winer = winers[i][0], winers[i][1]
            score_all = score(r_loser, d_loser, coeff) - score(r_winer, d_winer, coeff)
            m = np.log(1 + np.exp(score_all))
            sum_m += m
            
            score_a0 = score(r_loser, d_loser, coeff_a0_delta) - score(r_winer, d_winer, coeff_a0_delta)
            score_a1 = score(r_loser, d_loser, coeff_a1_delta) - score(r_winer, d_winer, coeff_a1_delta)
            score_a2 = score(r_loser, d_loser, coeff_a2_delta) - score(r_winer, d_winer, coeff_a2_delta)
            score_a3 = score(r_loser, d_loser, coeff_a3_delta) - score(r_winer, d_winer, coeff_a3_delta)
            score_a4 = score(r_loser, d_loser, coeff_a4_delta) - score(r_winer, d_winer, coeff_a4_delta)
            score_a10 = score(r_loser, d_loser, coeff_a10_delta) - score(r_winer, d_winer, coeff_a10_delta)
            score_a11 = score(r_loser, d_loser, coeff_a11_delta) - score(r_winer, d_winer, coeff_a11_delta)
            score_a12 = score(r_loser, d_loser, coeff_a12_delta) - score(r_winer, d_winer, coeff_a12_delta)
            score_a13 = score(r_loser, d_loser, coeff_a13_delta) - score(r_winer, d_winer, coeff_a13_delta)
            
            sum_grad_a0 += (m - np.log(1 + np.exp(score_a0))) / delta
            sum_grad_a1 += (m - np.log(1 + np.exp(score_a1))) / delta
            sum_grad_a2 += (m - np.log(1 + np.exp(score_a2))) / delta
            sum_grad_a3 += (m - np.log(1 + np.exp(score_a3))) / delta
            sum_grad_a4 += (m - np.log(1 + np.exp(score_a4))) / delta
            sum_grad_a10 += (m - np.log(1 + np.exp(score_a10))) / delta
            sum_grad_a11 += (m - np.log(1 + np.exp(score_a11))) / delta
            sum_grad_a12 += (m - np.log(1 + np.exp(score_a12))) / delta
            sum_grad_a13 += (m - np.log(1 + np.exp(score_a13))) / delta
                 
        a0 += learning_rate * sum_grad_a0 / len_train
        a1 += learning_rate * sum_grad_a1 / len_train
        a2 += learning_rate * sum_grad_a2 / len_train
        a3 += learning_rate * sum_grad_a3 / len_train
        a4 += learning_rate * sum_grad_a4 / len_train
        a10 += learning_rate * sum_grad_a10 / len_train
        a11 += learning_rate * sum_grad_a11 / len_train
        a12 += learning_rate * sum_grad_a12 / len_train
        a13 += learning_rate * sum_grad_a13 / len_train
                    
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, a0={a0}, a1={a1}, a2={a2}, a3={a3}, a4={a4}, a10={a10}, a11={a11}, a12={a12}, a13={a13},m={sum_m/len_train}, delta_m={sum_m/len_train - previos_m}")
            previos_m = sum_m / len_train
        
            
        if epoch % 3000 == 0:
            learning_rate /= 2            




if __name__ == '__main__':
	main()
