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
        a0, a1, a2, a3, a4 = coeff
        #return a0 * (1 + 9* r/10) * ( 10 ** (1 - d) )
        return a0 * np.exp(a1 + a2 * r - a3 * d)
    
    def score_d(d, coeff):
        a0, a1, a2, a3, a4 = coeff
        #return a0 * (a1) * ( 10 ** (1 - d) )
        return a0 * np.exp(a1 - a3 * d)
    
	# Загрузка данных
    file_path = os.path.abspath("") + '\\2023\\ml\\Сложные\\Рестораны\\restaurants_train.txt'
    #file_path = os.path.abspath("") + '\\Рестораны\\restaurants_train.txt'
    winers = []
    losers = []
    r_avarage = 0
    avarage_count = 0
    with open(file_path, 'r') as f:
        for i in range(1000):
            winner, r1, r2, d1, d2 = map(float, f.readline()[:-1].split())
            
            if r1 != -1:
                r_avarage += r1
                avarage_count += 1
            if r2 != -1:
                r_avarage += r2
                avarage_count += 1
            
            if winner == 0:
                winers.append((r1, d1))
                losers.append((r2, d2))
            elif winner == 1:
                winers.append((r2, d2))
                losers.append((r1, d1))
            else:
                continue # ничью "игнорим"
    
    len_train = len(winers)
    r_avarage = r_avarage / avarage_count
    
    # стартовые значения
    a0=1
    a1=1
    a2=0.1
    a3=100
    a4=1
    
    learning_rate=0.5
    delta = 1e-6
    for epoch in range(10000):
        sum_grad_a0, sum_grad_a1, sum_grad_a2, sum_grad_a3, sum_grad_a4 = 0, 0, 0, 0, 0
        sum_m = 0
        coeff = [a0, a1, a2, a3, a4]
        coeff_a0_delta = [a0+delta, a1, a2, a3, a4]
        coeff_a1_delta = [a0, a1+delta, a2, a3, a4]
        coeff_a2_delta = [a0, a1, a2+delta, a3, a4]
        coeff_a3_delta = [a0, a1, a2, a3+delta, a4]
        coeff_a4_delta = [a0, a1, a2, a3, a4+delta]
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
            
            sum_grad_a0 = - (m - np.log(1 + np.exp(score_a0))) / delta
            sum_grad_a1 = - (m - np.log(1 + np.exp(score_a1))) / delta
            sum_grad_a2 = - (m - np.log(1 + np.exp(score_a2))) / delta
            sum_grad_a3 = - (m - np.log(1 + np.exp(score_a3))) / delta
            sum_grad_a4 = - (m - np.log(1 + np.exp(score_a4))) / delta            
                    
        a0 += learning_rate * sum_grad_a0 / len_train
        a1 += learning_rate * sum_grad_a1 / len_train
        a2 += learning_rate * sum_grad_a2 / len_train
        a3 += learning_rate * sum_grad_a3 / len_train
        a4 += learning_rate * sum_grad_a4 / len_train
        
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, a0={a0}, a1={a1}, a2={a2}, a3={a3}, m={sum_m/len_train}")
        
            
        #if epoch % 1000 == 0:
        #    learning_rate /= 2            




if __name__ == '__main__':
	main()
