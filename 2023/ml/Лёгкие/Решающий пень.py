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
    len_x = len(x)
    sum = 0
    for i in range(len_x):
        if x[i] < c:
            sum += (y[i] - a)**2
        else:
            sum += (y[i] - b)**2
    return (sum/len_x)**0.5 

def gradient(x, y, f_value, a, b, c, delta_c, learning_rate):
    grad_a = 0
    grad_b = 0
    grad_c = 0
    delta = (1e-7)/2
    n = len(x)
    if delta_c == 0:
        grad_a += -2*((f_value - f(x, y, a+delta, b, c))/delta)
        grad_b += -2*((f_value - f(x, y, a, b+delta, c))/delta)
        return [grad_a/n, grad_b/n, 0]
    else:
        delta_c = delta_c * 5 * learning_rate
        grad_a += -2*((f_value - f(x, y, a+delta, b, c))/delta)
        grad_b += -2*((f_value - f(x, y, a, b+delta, c))/delta)
        grad_c += -2*((f_value - f(x, y, a, b, c+delta_c))/delta_c)
        return [grad_a, grad_b, grad_c]

def find_start_coeffs(x, y):
    n = len(x)
    c = 1.01*sum(x)/n
    delta_c = max(x) - min(x)
    sum_mid = sum(y)/n
    sum_error = 0
    for i in range(n):
        if x[i] < c:
            sum_error += y[i] - sum_mid

    if sum_error > 0:
        a = max(y)+1
        b = min(y)-1
    else:
        a = min(y)-1
        b = max(y)+1

    return [a, b, c, delta_c]

def find_coeffs(x, y, learning_rate=0.1, max_iterations=2000):
    coeffs = find_start_coeffs(x, y)
    a, b, c, delta_c = coeffs

    f_value = f(x, y, a, b, c)
    for i in range(max_iterations):
        grad = gradient(x, y, f_value, a, b, c, delta_c, learning_rate)
        a -= learning_rate * grad[0]
        b -= learning_rate * grad[1]
        c -= learning_rate * grad[2]
        f_value = f_value = f(x, y, a, b, c)
        if i % 100 == 0:
            learning_rate /= 2
    
    return [a, b, c]


if __name__ == '__main__':
	main()