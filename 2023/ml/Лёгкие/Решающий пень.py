import numpy as np

def main():
    
    sample_size = int(input())
    x, y = np.empty(sample_size), np.empty(sample_size)
    for i in range(sample_size):
        x[i], y[i] = map(int, input().split())

    coeffs = find_coeffs(x, y, sample_size)
    print(" ".join(map(str, coeffs)))


def f(x, y, c, sample_size):
    y_low = y[x < c]
    y_uper = y[x >= c]
    len_y_low = len(y_low)
    len_y_upper = sample_size - len_y_low
    a = np.mean(y_low) if len_y_low != 0 else 0
    b = np.mean(y_uper) if len_y_upper != 0 else 0
    f_value = np.square(y_low - a).sum() + np.square(y_uper - b).sum()
    return [a, b, f_value]

def find_coeffs(x, y, sample_size):
    set_x = np.unique(x)
    c_opt = set_x[0]
    a_opt, b_opt, f_min = f(x, y, c_opt, sample_size)

    for c_i in set_x:
        a_i, b_i, f_i = f(x, y, c_i, sample_size)
        if f_i < f_min:
            a_opt, b_opt, c_opt, f_min = a_i, b_i, c_i, f_i
    return [a_opt, b_opt, c_opt]

if __name__ == '__main__':
	main()