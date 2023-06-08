import sys
import numpy as np
from abc import ABC, abstractmethod
import scipy.stats as stats

class Strategy(ABC):
  def __init__(self, n_arms, epsilon):
    self.Q = np.zeros(n_arms)
    self.n = [0 for _ in range(n_arms)]
    self.epsilon = epsilon
    self.n_arms = n_arms
    
  @abstractmethod
  def make_action(self):
    pass
    
  def update(self, action, reward):
    self.n[action] += 1
    self.Q[action] = (self.Q[action] * (self.n[action]-1) + reward)/self.n[action]

class BayesianStrategy_Bin(Strategy):
  def __init__(self, n_arms, alpha, beta):
    self.n_arms = n_arms
    self.a = np.full(n_arms, alpha)
    self.b = np.full(n_arms, beta)
    self.disr = stats.distributions.beta
        
  def make_action(self):
    samples = self.disr.rvs(self.a, self.b)
    return np.argmax(samples)
    
  def update(self, action, reward):
    if reward:
      self.a[action] += 1
    else:
      self.b[action] += 1

def main():
    '''
    '''
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        sys.stdout.flush()
        alpha, beta = map(float, input().split())
        
        bayesianStrategy_Bin = BayesianStrategy_Bin(m, alpha, beta)
        for i in range(n):
            # Выбираем автомат на основе текущих вероятностей
            chosen_machine = bayesianStrategy_Bin.make_action()
            print(chosen_machine + 1)
            sys.stdout.flush()
            # Получаем результат броска
            result = int(input())
            # Обновляем количество успехов и неудач для выбранного автомата
            bayesianStrategy_Bin.update(chosen_machine, result)


if __name__ == '__main__':
    main()