import sys
import math


def main():
    
    sample_size = int(input())
    x = [None] * sample_size
    y = [None] * sample_size
        
    for i in range(sample_size):
        sample = list(map(int, input().split()))
        x[i]=sample[0]
        y[i]=sample[1]

    coeffs = find_coeffs(x, y)
    print(" ".join(map(str, coeffs)))

def f(x, y, a, b, c):
    if x < c:
        return (y - a)**2
    else:
        return (y - b)**2

def objective(coeffs, x, y):
    a, b, c = coeffs
    error = 0
    for i in range(len(x)):
        error += (y[i] - f(x[i], a, b, c))**2
    return error

def gradient(coeffs, x, y):
    a, b, c = coeffs
    grad_a = 0
    grad_b = 0
    grad_c = 0
    delta = (1e-3)/2
    n = len(x)
    for i in range(n):
        grad_a += -2*((f(x[i], y[i], a, b, c) - f(x[i], y[i], a+delta, b, c))/delta)
        grad_b += -2*((f(x[i], y[i], a, b, c) - f(x[i], y[i], a, b+delta, c))/delta)
        grad_c += -2*((f(x[i], y[i], a, b, c) - f(x[i], y[i], a, b, c+delta))/delta)
    return [grad_a/n, grad_b/n, grad_c/n]

def find_coeffs(x, y, learning_rate=0.1, max_iterations=1000):
    coeffs = [1, 1, 1.5]

    for i in range(max_iterations):
        grad = gradient(coeffs, x, y)
        coeffs[0] -= learning_rate * grad[0]
        coeffs[1] -= learning_rate * grad[1]
        coeffs[2] -= learning_rate * grad[2]
        if i % 100 == 0:
            learning_rate /= 2
    
    return coeffs


if __name__ == '__main__':
	main()