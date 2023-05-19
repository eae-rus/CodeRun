from scipy.optimize import curve_fit
import numpy as np

def main():
    '''
    '''
    # задаем функцию, которую нужно приблизить
    def func(x, a, b, c, d):
        return a * np.tan(x) + (b * np.sin(x) + c * np.cos(x))**2 + d * np.sqrt(x)

    n = int(input())

    x = np.empty(n)
    y = np.empty(n)
    
    for i in range(n):
        x[i], y[i] = map(float, input().split())

    # находим оптимальные значения коэффициентов
    popt, pcov = curve_fit(func, x, y)

    # выводим найденные коэффициенты
    print(" ".join(str(x) for x in popt))

if __name__ == '__main__':
	main()