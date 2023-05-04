
import numpy as np

def main():
    
    sample_size = int(input())
    x, y = np.empty(sample_size), np.empty(sample_size)
    for i in range(sample_size):
        x[i], y[i] = map(int, input().split())

    coeffs = find_coeffs(x, y)
    print(" ".join(map(str, coeffs)))

def f(x, y, a, b, c):
    y_low = y[x < c]
    y_uper = y[x >= c]
    sum = np.sum((y_low - a)**2) + np.sum((y_uper - b)**2)
    return sum

def find_coeffs(x, y):
    set_x = np.unique(x)
    a_opt, b_opt, c_opt = y[0], y[0], x[0]
    f_min = f(x, y, a_opt, b_opt, c_opt)

    for c_i in set_x:
        y_low = y[x < c_i]
        y_uper = y[x >= c_i]
        a_i = np.mean(y_low) if len(y_low) != 0 else 0
        b_i = np.mean(y_uper) if len(y_uper) != 0 else 0
        f_i = f(x, y, a_i, b_i, c_i)

        if f_i < f_min:
            a_opt, b_opt, c_opt, f_min = a_i, b_i, c_i, f_i

    return [a_opt, b_opt, c_opt]


if __name__ == '__main__':
	main()