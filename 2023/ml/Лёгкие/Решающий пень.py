
import numpy as np

def main():
    
    sample_size = int(input())
    x = np.empty(sample_size)
    y = np.empty(sample_size)
        
    for i in range(sample_size):
        sample = list(map(int, input().split()))
        x[i] = sample[0]
        y[i] = sample[1]

    coeffs = find_coeffs(x, y, sample_size)
    print(" ".join(map(str, coeffs)))

def f(x, y, a, b, c, sample_size):
    y_low = y[x < c]
    y_uper = y[x >= c]
    sum = np.sum((y_low - a)**2) + np.sum((y_uper - b)**2)
    return (sum/sample_size)**0.5 

def find_coeffs(x, y, sample_size):
    set_y = set(x)
    a_opt = y[0]
    b_opt = y[0]
    c_opt = x[0]
    f_min = f(x, y, a_opt, b_opt, c_opt, sample_size)

    for c_i in set_y:
        y_low = y[x < c_i]
        y_uper = y[x >= c_i]
        y_sum_low = np.sum(y_low)
        y_sum_uper = np.sum(y_uper)
        y_len_low = len(y_low)
        y_len_uper = len(y_uper)
        a_i = y_sum_low / y_len_low if y_len_low != 0 else 0
        b_i = y_sum_uper / y_len_uper if y_len_uper != 0 else 0
        f_i = f(x, y, a_i, b_i, c_i, sample_size)

        if f_i < f_min:
            a_opt = a_i
            b_opt = b_i
            c_opt = c_i
            f_min = f_i

    return [a_opt, b_opt, c_opt]


if __name__ == '__main__':
	main()