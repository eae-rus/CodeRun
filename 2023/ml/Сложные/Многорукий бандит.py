import sys
import numpy as np

def main():
    '''
    '''
    successes, failures = [], []
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        sys.stdout.flush()
        alpha, beta = map(float, input().split())

        # Инициализируем количество успехов и неудач для каждого автомата
        if successes == []:
            successes = np.full(m, alpha)
            failures = np.full(m, beta)

        # Инициализируем априорные вероятности для каждого автомата
        prob = np.zeros(m)
        for j in range(m):
            prob[j] = successes[j]/ (successes[j] + failures[j])
        prob = prob/prob.sum()

        for i in range(n):
            # Выбираем автомат на основе текущих вероятностей
            chosen_machine = np.random.choice(m, p=prob)
            print(chosen_machine + 1)
            sys.stdout.flush()
            # Получаем результат броска
            result = int(input())
            # Обновляем количество успехов и неудач для выбранного автомата
            if result == 1:
                successes[chosen_machine] += 1
            else:
                failures[chosen_machine] += 1
            # Обновляем вероятности для каждого автомата на основе результатов
            for j in range(m):
                prob[j] = successes[j]/ (successes[j] + failures[j])
            prob = prob/prob.sum()

if __name__ == '__main__':
    main()